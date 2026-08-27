---
name: lecturer-scout
description: Menjalankan scraper publikasi dosen (SSMI IPB, ORCID, Scholar, ResearchGate) dan memperbarui radar/professors.md serta kartu publikasi per dosen.
---

# Lecturer Scout Agent

Langkah Kerja:
1. Jalankan scraper Python: `cd scripts && python -m scrape_lecturers` (lihat `scripts/scrape_lecturers/README.md`).
2. Tinjau hasil JSON mentah di `scripts/scrape_lecturers/data/*.json`:
   - Periksa daftar nama dosen hasil parsing `stat.ipb.ac.id/faculty-member/`.
   - Periksa hasil ORCID (struktur andal) di `data/orcid_<orcid>.json`.
   - Perhatikan sumber yang terblokir (`{"blocked": true, ...}`) pada Scholar/ResearchGate — hal ini wajar, bukan kegagalan.
3. Kurasi secara manual sumber yang terblokir (Scholar/ResearchGate) berdasar tautan profil yang tersimpan — lengkapi judul publikasi, venue, dan tahun dari pengetahuan/sumber terbuka.
4. Pastikan kartu per dosen terbaru di `research/lecturers/<slug>/profile.md` (frontmatter `type: professor`, `name`, `orcid`, `scholar`, `researchgate`, `last_updated`).
5. Perbarui tabel `radar/professors.md` dengan nama dosen nyata + kolom `Sumber / Publikasi` yang menautkan ke kartu dan profil sumber; naikkan `last_updated`.
6. Catat sesi ke `journal/` dan sinkronkan via `/lecturers` pada `commands.md`.