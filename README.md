# Academic OS

> Personal AI Operating System untuk S2 Statistika dan Sains Data IPB.

Repo ini adalah **knowledge base + workflow orchestrator** pribadi: semua aktivitas akademik — kuliah, riset, paper, eksperimen, dosen, sampai evaluasi harian/mingguan — diorganisir dalam struktur folder yang konsisten, diproses oleh agen AI spesialis (Command Code skills), dan dipantau lewat dashboard/radar.

---

## Ringkasan

- **North Star:** Menjadi AI Engineer berbasis Statistika dengan kemampuan nyata.
- **Bahasa kerja:** Indonesia (dokumen, jurnal, dan catatan menggunakan Bahasa Indonesia).
- **Bentuk:** Repo markdown-first (bukan codebase aplikasi). Isinya dokumen pengetahuan + skrip otomasi PowerShell + definisi skill AI.
- **Cara pakai utama:** Berinteraksi dengan asisten AI (Command Code) di folder ini — AI membaca konteks dari struktur folder dan skill, lalu memproses input sesuai alur kerja di bawah.

---

## Struktur Folder

| Folder | Isi & Fungsi |
| :--- | :--- |
| `courses/<KODE_MK>/` | Catatan kuliah per mata kuliah (STA501, STA511, STA561, STA581). Format `YYYY-MM-DD-topic.md` (template: `templates/lecture.md`). |
| `research/` | Pipeline riset: `papers/<slug>/` (summary.md, notes.md, experiment.md), `summaries/`, `lecturers/<slug>/profile.md`, `datasets/`, `literature-map.md`, `pipeline.md`. |
| `radar/` | Watchlist & pemantauan: `papers.md` (antrean baca), `professors.md` (dosen/lab), `opportunities.md` (ide riset), `datasets.md`. |
| `knowledge/` | Indeks 3 entitas inti: `concepts.md`, `methods.md`, `datasets.md` + `cross-links.md` (ontologi di `knowledge-schema.md`). |
| `journal/` | Log aktivitas: `daily/`, `weekly/`, `monthly/`. |
| `memory/` | Konteks permanen pengguna: `goals.md`, `preferences.md`, `semester.md`. |
| `thesis/` | Modul tesis dinamis: `proposal.md`, `hypotheses.md`, `questions.md`, `roadmap.md`. |
| `experiments/` | Scaffolding proyek eksperimen modular (mis. `xgboost-poverty/`, `sample-baseline/`). |
| `templates/` | Template markdown standar: `daily.md`, `lecture.md`, `paper.md`, `weekly.md`. |
| `scripts/` | Otomasi PowerShell: setup, scaffolding, sync, health check (lihat tabel skrip). |
| `project/` | Manajemen pengembangan sistem itu sendiri: `backlog.md` (fitur ber-ID seperti FD-01, EH-04), `sprint-01.md`, dll. |
| `dashboard/` | Status ringkas progres (di-sync otomatis saat shutdown). |
| `.commandcode/skills/` | Definisi skill/agen AI (15 skill, lihat arsitektur di bawah). |
| `AGENTS.md` | Routing layer: aturan delegasi prompt ke agen spesialis. |
| `knowledge-schema.md` | Ontologi & konvensi metadata (entity, relationship, frontmatter). |
| `commands.md` | Daftar slash commands untuk alur kerja harian. |

> **Konvensi utama:** setiap file markdown memakai **YAML frontmatter** (type, date, status, dst.) sesuai `knowledge-schema.md`, dan **cross-link** antardokumen memakai sintaks `[[path/tanpa-ekstensi]]`.

---

## Cara Menggunakan

Alur kerja harian dirancang mengikuti siklus: **Pagi → Proses → Evaluasi → Sinkronisasi**.

### 1. Pagi — Start Day
- Buka `dashboard/` dan `radar/` untuk konteks, target, dan watchlist.
- Jalankan skill **morning-brief** untuk menyusun 3 target utama hari ini.

### 2. Proses — Selama Hari
- **Kuliah:** tempel catatan mentah/slide → skill **course-mentor / lecture-process** menghasilkan catatan 6-artefak di `courses/<MK>/`.
- **Paper:** serahkan PDF/teks → skill **paper-intake / research-assistant** menghasilkan summary, gap analysis, dan update `thesis/` + `radar/`.
- **Kode/eksperimen:** minta skrip modular → skill **coding-copilot / experiment-generate**.
- **Dosen & publikasi:** minta data dosen → skill **lecturer-scout** (scraper SSMI/ORCID/Scholar/RG) memperbarui `radar/professors.md` dan kartu di `research/lecturers/<slug>/profile.md`.
- **Karier/beasiswa:** skill **career-scout** mencatat peluang di `radar/`.

### 3. Evaluasi — Sore/Malam
- Jalankan skill **shutdown** (tutup hari, sync `dashboard/`) dan **weekly-research** (evaluasi mingguan, agregasi insight, sinkronisasi proposal).

### 4. Otomasi Skrip PowerShell

| Skrip | Fungsi |
| :--- | :--- |
| `scripts/setup.ps1` | Bootstrap awal: cek Git/VS Code/Command Code & buat struktur folder. |
| `scripts/doctor.ps1` | Health check komponen sistem (status siap operasional?). |
| `scripts/new-day.ps1` | Buat jurnal harian `journal/daily/<tanggal>.md` dari template. |
| `scripts/new-lecture.ps1 -Course STA501 -Topic "..."` | Scaffold catatan kuliah baru. |
| `scripts/new-paper.ps1 -PaperSlug <slug>` | Buat folder paper + summary/notes/experiment. |
| `scripts/daily-sync.ps1` | `git add . && commit && push` (auto-sync harian). |
| `scripts/sync.ps1` | Sinkronisasi tambahan (variasi daily-sync). |

---

## Arsitektur Multi-Agent (Routing Layer)

Setiap prompt yang masuk diarahkan ke agen spesialis sesuai domain (detail di `AGENTS.md`):

| Domain Permintaan | Agen | Output / Artefak |
| :--- | :--- | :--- |
| Kuliah & Teori | **Course Mentor** | Catatan di `courses/` |
| Paper & Riset | **Research Assistant** | Summary, gap, update `thesis/` |
| Kode & Pipeline | **Coding Copilot** | Skrip modular, config, template repo |
| Karier & Beasiswa | **Career Scout** | Peluang & deadline di `radar/` |
| Dosen & Publikasi | **Lecturer Scout** | Data dosen & kartu publikasi di `radar/` & `research/lecturers/` |
| Evaluasi Harian/Mingguan | **Review Coach** | Jurnal & sinkronisasi dashboard |

Tugas kompleks bisa dirantai berurutan, misal *baca paper lalu buat script baseline* → Research Assistant → Coding Copilot.

---

## Riset: Pipeline & Standar

Alur 4 tahap (detail di `research/pipeline.md`):
1. **Discovery** — paper masuk watchlist `radar/papers.md`.
2. **Deep Reading** — pembacaan kritis (problem, asumsi, batasan, kontribusi).
3. **Artifact Extraction** — ringkasan standar di `research/summaries/` (frontmatter + LaTeX + minimal 1 cross-link).
4. **Knowledge Synthesis** — hubungkan ke `courses/`, `knowledge/`, `radar/opportunities.md`.

Setiap paper diproses menghasilkan **4 artefak wajib**: summary document, concept/method link, recall & critique cards, dan research opportunity entry.

Contoh kartu dosen: [`research/lecturers/farit-mochamad-afendi/profile.md`](research/lecturers/farit-mochamad-afendi/profile.md) — berisi frontmatter ORCID/Scholar/ResearchGate, tabel publikasi dari ORCID/Scholar (dikurasi manual bila sumber diblokir), dan profil terkait.

---

## Status Progres (per semester)

Update rutin lewat `dashboard/` dan skill review. Lihat juga `project/backlog.md` untuk roadmap fitur sistem (epic Foundation, Memory, Knowledge, Radar, Research, Agents, Enhancement ber-ID seperti EH-04 Lecturer & Publication Radar).

---

## Changelog & Dokumentasi Terkait

- `CHANGELOG.md` — riwayat versi sistem (v0.1.0: foundation, memory, knowledge, research pipeline, multi-agent, DX).
- `commands.md` — pintasan slash commands (`/start-day`, `/lecture`, `/paper`, `/weekly`, `/lecturers`, `/shutdown`, dst).
- `knowledge-schema.md` — ontologi entitas & relasi.
- `AGENTS.md` — routing layer multi-agent.
