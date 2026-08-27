"""Scraper Lecturer & Publikasi untuk Academic OS (EH-04).

Alur kerja:
  1. Parsing nama dosen dari halaman SSMI IPB (stat.ipb.ac.id/faculty-member/).
  2. Ambil daftar publikasi via ORCID Public API (andal, JSON terstruktur).
  3. Probe Google Scholar & ResearchGate secara best-effort (HTML) — jika
     terblokir (403/429) dicatat {blocked: true} dan dilanjutkan, tidak pernah raise.
  4. Render output: kartu per dosen (research/lecturers/<slug>/profile.md)
     dan tabel radar/professors.md.

Jalankan:  cd scripts;  python -m scrape_lecturers
"""

from __future__ import annotations

import json
import logging
import re
import time
from datetime import date
from pathlib import Path

import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("scrape_lecturers")

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_CONFIG = BASE_DIR / "config.yaml"

ORCID_API = "https://pub.orcid.org/v3.0/{oid}/works"
SCHOLAR_URL = "https://scholar.google.com/citations?user={uid}&hl=id"
RESEARCHGATE_URL = "https://www.researchgate.net/scientific-contributions/{pid}"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/125.0 Safari/537.36 AcademicOS/0.1"
    ),
    "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
}


# ----------------------------------------------------------------------
# Utilitas
# ----------------------------------------------------------------------
def _slugify(name: str) -> str:
    """Ubah nama dosen menjadi slug path yang aman."""
    s = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return s or "lecturer"


def _polite_delay(seconds: float) -> None:
    if seconds > 0:
        time.sleep(seconds)


def _save_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


# ----------------------------------------------------------------------
# 1. SSMI IPB faculty page
# ----------------------------------------------------------------------
def fetch_faculty(config: dict) -> list[dict]:
    """Parsing nama + bidang dosen dari halaman fakultas SSMI IPB.

    Best-effort: selector halaman bisa berubah; bila gagal ekstrak, fallback
    pada daftar `lecturers` dari config agar runs tetap bermakna.
    """
    url = config["faculty_url"]
    delay = config["request_delay_seconds"]
    try:
        resp = requests.get(url, headers=HEADERS, timeout=config["timeout_seconds"])
        _polite_delay(delay)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        # Heuristik berbagai markup; dikumpulkan nama dari elemen yang menyerupai kartu dosen.
        names = []
        selectors = (
            ".entry-title,"
            ".elementor-widget-heading .elementor-heading-title,"
            "h3, h4, .vc_tta-title-text"
        )
        for el in soup.select(selectors):
            text = el.get_text(" ", strip=True)
            if text and ("Prof" in text or "Dr" in text or re.search(r"\bS\.\w*\.?", text)):
                names.append(text)

        # Dedup, awet urutan kemunculan.
        seen, unique = set(), []
        for n in names:
            if n and n not in seen:
                seen.add(n)
                unique.append(n)
        return [{"name": n, "source": url} for n in unique]
    except requests.RequestException as exc:
        log.warning("Faculty page gagal diambil (%s); fallback ke config.lecturers", exc)
        return [{"name": lec["name"], "source": url} for lec in config["lecturers"]]


# ----------------------------------------------------------------------
# 2. ORCID Public API
# ----------------------------------------------------------------------
def fetch_orcid(orcid_id: str, config: dict) -> dict:
    """Ambil daftar publikasi dari ORCID Public API (JSON, andal)."""
    url = ORCID_API.format(oid=orcid_id)
    try:
        resp = requests.get(url, headers=HEADERS, timeout=config["timeout_seconds"])
        _polite_delay(config["request_delay_seconds"])
        resp.raise_for_status()
        payload = resp.json()
    except (requests.RequestException, ValueError) as exc:
        log.warning("ORCID %s gagal (%s)", orcid_id, exc)
        return {"orcid": orcid_id, "blocked": True, "error": str(exc), "works": []}

    works = []
    for group in payload.get("group", []):
        for summary in group.get("work-summary", []):
            title = (summary.get("title") or {}).get("title") or {}
            year = None
            pub = summary.get("publication-date")
            if pub and pub.get("year"):
                year = pub["year"].get("value")
            works.append(
                {
                    "title": title.get("value", ""),
                    "year": year,
                    "type": summary.get("type"),
                    "doi": (summary.get("external-ids") or {}).get("external-id"),
                }
            )
    log.info("ORCID %s: %d works terambil", orcid_id, len(works))
    return {"orcid": orcid_id, "blocked": False, "works": works}


# ----------------------------------------------------------------------
# 3. Scholar & ResearchGate (best-effort)
# ----------------------------------------------------------------------
def probe_scholar(scholar_user: str | None, config: dict) -> dict:
    """Probe best-effort profil Google Scholar."""
    if not scholar_user:
        return {"blocked": False, "works": []}
    url = SCHOLAR_URL.format(uid=scholar_user)
    return _probe_html(url, "scholar", config)


def probe_researchgate(rg_id: str | None, config: dict) -> dict:
    """Probe best-effort profil ResearchGate."""
    if not rg_id:
        return {"blocked": False, "works": []}
    url = RESEARCHGATE_URL.format(pid=rg_id)
    return _probe_html(url, "researchgate", config)


def _probe_html(url: str, source: str, config: dict) -> dict:
    """Request HTML dan ekstrak judul publikasi bila memungkinkan; tak pernah raise."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=config["timeout_seconds"])
        _polite_delay(config["request_delay_seconds"])
        if resp.status_code in (403, 429):
            log.warning("%s terblokir (%d)", source, resp.status_code)
            return {"source": source, "blocked": True, "url": url, "works": []}
        resp.raise_for_status()
    except requests.RequestException as exc:
        log.warning("%s gagal (%s)", source, exc)
        return {"source": source, "blocked": True, "url": url, "works": [], "error": str(exc)}

    soup = BeautifulSoup(resp.text, "html.parser")
    titles = []
    # Heuristik heksa: kumpulkan heading/teks menyerupai judul publikasi (fallback tak mengganggu).
    for el in soup.select("h2 a, h2, h3, .nova-e-text a"):
        text = el.get_text(" ", strip=True)
        if text and 15 <= len(text) <= 250:
            titles.append({"title": text, "url": url})
    seen, unique = set(), []
    for t in titles:
        key = t["title"].lower()
        if key not in seen:
            seen.add(key)
            unique.append(t)
    return {"source": source, "blocked": False, "url": url, "works": unique[:30]}


# ----------------------------------------------------------------------
# 4. Render output
# ----------------------------------------------------------------------
def _sources_blocked(result: dict) -> str:
    if result.get("blocked") and result.get("url"):
        return result["url"] if isinstance(result.get("url"), str) else "(tautan profil)"
    return "-"


def build_lecturer_card(lec: dict, faculty_name: str, orcid, scholar, rg, config: dict) -> Path:
    slug = lec["slug"] or _slugify(faculty_name or lec["name"])
    out_dir = BASE_DIR / config["lecturers_dir"] / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    profile = out_dir / "profile.md"

    lines = [
        "---",
        "type: professor",
        f"name: {faculty_name or lec['name']}",
        f"orcid: {lec.get('orcid') or '-'}",
        f"scholar: {lec.get('scholar_user') or '-'}",
        f"researchgate: {lec.get('researchgate_id') or '-'}",
        f"last_updated: {date.today().isoformat()}",
        "---",
        "",
        f"# Profil & Publikasi: {faculty_name or lec['name']}",
        "",
    ]

    lines += ["## Publikasi — ORCID", ""]
    if orcid.get("works"):
        lines += ["| Judul | Tahun | Jenis | DOI |", "| :--- | :--- | :--- | :--- |"]
        for w in orcid["works"][:50]:
            doi = ""
            for ext in w.get("doi") or []:
                if ext.get("external-id-type") == "doi":
                    doi = ext.get("external-id-value", "")
            lines.append(f"| {w.get('title') or '-'} | {w.get('year') or '-'} | {w.get('type') or '-'} | {doi} |")
    else:
        lines += ["_Tidak ada data / terblokir._"]

    lines += ["", "## Publikasi — Google Scholar", ""]
    if scholar.get("works"):
        lines += ["| Judul | Tautan |", "| :--- | :--- |"]
        for w in scholar["works"]:
            lines.append(f"| {w['title']} | {w['url']} |")
    else:
        lines += [f"_Best-effort; profil: {_sources_blocked(scholar)}._"]

    lines += ["", "## Publikasi — ResearchGate", ""]
    if rg.get("works"):
        lines += ["| Judul | Tautan |", "| :--- | :--- |"]
        for w in rg["works"]:
            lines.append(f"| {w['title']} | {w['url']} |")
    else:
        lines += [f"_Best-effort; profil: {_sources_blocked(rg)}._"]

    profile.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return profile


def render_radar(lecturers: list[dict], config: dict, radar_path: Path) -> Path:
    radar_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "---",
        "type: radar",
        "category: professors",
        f"last_updated: {date.today().isoformat()}",
        "---",
        "",
        "# Professor & Research Lab Radar",
        "",
        "Pemetaan dosen, kelompok keahlian, dan topik riset potensial untuk bimbingan tesis/proyek "
        "(diisi otomatis oleh EH-04; sumber yang terblokir dikurasi manual via `lecturer-scout`).",
        "",
        "| Dosen | Sumber / Publikasi | Status Kontak | Catatan & Potensi Kolaborasi |",
        "| :--- | :--- | :--- | :--- |",
    ]
    for lec in lecturers:
        slug = lec["slug"] or _slugify(lec["name"])
        card = f"[[research/lecturers/{slug}/profile.md|Kartu]]"
        lines.append(f"| {lec['name']} | {card} • ORCID `{lec.get('orcid') or '-'}` • Scholar `{lec.get('scholar_user') or '-'}` • RG `{lec.get('researchgate_id') or '-'}` | Belum Dihubungi | Dikurasi otomatis EH-04 |")
    radar_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return radar_path


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
def main() -> None:
    import yaml

    cfg_path = Path(DEFAULT_CONFIG)
    if cfg_path.exists():
        config = yaml.safe_load(cfg_path.read_text(encoding="utf-8"))
    else:
        config = {
            "faculty_url": "https://stat.ipb.ac.id/faculty-member/",
            "request_delay_seconds": 2.0,
            "timeout_seconds": 20,
            "output_dir": "data",
            "radar_output": "../../radar/professors.md",
            "lecturers_dir": "../../research/lecturers",
            "lecturers": [],
        }
    data_dir = BASE_DIR / config.get("output_dir", "data")
    data_dir.mkdir(parents=True, exist_ok=True)

    # 1. Faculty page
    faculty = fetch_faculty(config)
    _save_json(data_dir / "faculty_raw.json", faculty)
    log.info("Faculty: %d name terambil", len(faculty))

    # Merged lecturer list (config seed menang bila ada; tanpa config gunakan hasil faculty).
    lec_rows = config.get("lecturers") or []
    if not lec_rows:
        lec_rows = [{"slug": _slugify(f["name"]), "name": f["name"]} for f in faculty]

    results = []
    for lec in lec_rows:
        orcid = fetch_orcid(lec["orcid"], config) if lec.get("orcid") else {"works": []}
        scholar = probe_scholar(lec.get("scholar_user"), config)
        rg = probe_researchgate(lec.get("researchgate_id"), config)
        _save_json(data_dir / f"orcid_{lec.get('orcid', 'none')}.json", orcid)
        profile = build_lecturer_card(lec, lec.get("name", ""), orcid, scholar, rg, config)
        results.append({"lecturer": lec.get("name"), "card": str(profile),
                        "orcid_works": len(orcid.get("works", [])),
                        "scholar_blocked": scholar.get("blocked", False),
                        "rg_blocked": rg.get("blocked", False)})
        log.info("Kartu dibuat: %s", profile)

    radar_path = BASE_DIR / config.get("radar_output", "../../radar/professors.md")
    render_radar(
        [dict(lec, name=lec["name"]) for lec in lec_rows],
        config,
        radar_path,
    )
    log.info("radar/professors.md diperbarui: %s", radar_path)
    _save_json(data_dir / "summary.json", results)


if __name__ == "__main__":
    main()