---
name: paper-intake
description: Ekstraksi dan sintesis dokumen paper riset (PDF/teks) menjadi ringkasan terstruktur dan integrasi ke radar.
---

# Paper Intake Skill

Tujuan: Mengolah satu dokumen paper menjadi ringkasan komprehensif, memperbarui peta literatur, dan menangkap peluang riset baru.

## Langkah Kerja:
1. Ekstrak metadata: Judul, Penulis, Tahun, Topik, Metode Utama, Dataset.
2. Identifikasi dan rumuskan 6 bagian esensial:
   - **Masalah:** Problem statement & latar belakang riset.
   - **Metode:** Algoritma, arsitektur, atau formulasi matematis utama (gunakan LaTeX jika ada rumus).
   - **Dataset:** Data yang digunakan, karakteristik, dan metrik evaluasi.
   - **Hasil:** Temuan utama dan perbandingan performa.
   - **Limitation:** Asumsi, kelemahan, atau skenario di mana metode gagal.
   - **Peluang Penelitian:** Celah ide atau potensi perbaikan untuk riset masa depan.
3. Simpan file ringkasan ke esearch/summaries/<paper-slug>.md menggunakan frontmatter standar.
4. Perbarui file esearch/literature-map.md (tambahkan entri baris baru).
5. Jika ditemukan celah riset yang menjanjikan, tambahkan entri ide baru ke adar/opportunities.md.
6. Perbarui status paper di adar/papers.md menjadi **Selesai**.
