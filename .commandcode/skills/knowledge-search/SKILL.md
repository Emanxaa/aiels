---
name: knowledge-search
description: Mesin pencari internal untuk sintesis lintas folder (knowledge, courses, research, radar, journal).
---

# Knowledge Search

Langkah Kerja:
1. Terima kata kunci query (konsep, metode, algoritma, atau topik) dari user.
2. Cari definisi dan relasi konsep di folder `knowledge/` (`concepts.md`, `methods.md`, `datasets.md`).
3. Cari catatan kuliah yang memuat materi tersebut di folder `courses/`.
4. Cari ringkasan paper ilmiah terkait di folder `research/` dan antrean di `radar/papers.md`.
5. Cari ide riset atau peluang terkait di `radar/opportunities.md`.
6. Cari catatan refleksi atau progres harian yang pernah membahas topik tersebut di `journal/`.
7. Susun output dalam bentuk sintesis terstruktur dengan format berikut:

## Sintesis Pengetahuan: [Topik/Keyword]

- **Konsep & Definisi:** [Ringkasan konsep inti dan metode terkait]
- **Catatan Kuliah Terkait:** [Daftar file di `courses/` yang relevan]
- **Paper & Literatur Terkait:** [Daftar paper di `research/` dan `radar/papers.md`]
- **Peluang Riset / Tesis:** [Kaitan dengan ide di `radar/opportunities.md`]
- **Rekomendasi Langkah Berikutnya:** [Aksi konkrit yang disarankan untuk memperdalam topik]
