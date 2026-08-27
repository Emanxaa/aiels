# Scraper Lecturer & Publikasi (EH-04)

Modul Python untuk menarik daftar dosen dari halaman **SSMI IPB** dan publikasinya dari
**ORCID**, **Google Scholar**, dan **ResearchGate**, lalu menuliskannya ke struktur Academic OS
(`radar/professors.md` + kartu di `research/lecturers/<slug>/profile.md`).

## Cara Pakai

```bash
cd scripts
pip install -r scrape_lecturers/requirements.txt
python -m scrape_lecturers
```

Hasil:
- `scrape_lecturers/data/faculty_raw.json` — nama dosen hasil parsing halaman fakultas.
- `scrape_lecturers/data/orcid_<id>.json` — publikasi via ORCID Public API.
- `scrape_lecturers/data/summary.json` — ringkasan eksekusi.
- `research/lecturers/<slug>/profile.md` — kartu tiap dosen (tabel publikasi per sumber).
- `radar/professors.md` — tabel radar diperbarui (naikkan `last_updated`).

## Keterbatasan yang Diketahui

- **Google Scholar & ResearchGate** agresif memblokir request polos (CAPTCHA/`403`/`429`).
  Akses ini bersifat *best-effort*: jika terblokir, modul mencatat `{"blocked": true, ...}`
  dan **selalu melanjutkan** (tidak pernah melempar error). Tautan profil tetap tersimpan.
- **ORCID Public API** adalah sumber terstruktur yang paling andal (JSON, tanpa CAPTCHA).
- Parsing halaman fakultas bergantung pada struktur HTML yang bisa berubah; bila gagal,
  modul `fallback` ke daftar `lecturers` di `config.yaml`.

## Konfigurasi (`config.yaml`)

- `faculty_url` — URL halaman fakultas SSMI IPB.
- `request_delay_seconds` — jeda sopan antar request (hormati server).
- `lecturers` — seed per dosen: `slug`, `name`, `orcid`, `scholar_user`, `researchgate_id`.
  Tambahkan baris baru bila ingin memperluas cakupan. Bila kosong, modul memakai hasil parsing
  halaman fakultas (tanpa kunci publikasi).

## Kebijakan Etika

Gunakan jeda sopan, hormati `robots.txt` dan ketentuan layanan masing-masing situs. Data diambil
sebagai metadata penelitian akademik pribadi, bukan untuk disebarluaskan massal.