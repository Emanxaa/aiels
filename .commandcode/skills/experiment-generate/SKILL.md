---
name: experiment-generate
description: Generate boilerplate proyek eksperimen riset modular dari ringkasan paper atau dataset.
---

# Experiment Generator Skill

Tujuan: Mengonversi ide atau ringkasan paper menjadi scaffold proyek eksperimen kode yang siap dieksekusi.

## Langkah Kerja:
1. Terima input topik/slug eksperimen (contoh: catboost-employment).
2. Buat folder baru di experiments/<nama-eksperimen>/.
3. Inisialisasi 4 file utama:
   - **README.md**: Deskripsi hipotesis, baseline, metrik evaluasi, dan TODO list eksperimen.
   - **config.yaml**: Parameter model, data paths, random seeds, dan hyperparameter.
   - **	rain.py**: Skrip Python modular standar (data loading, preprocessing, model fitting, metric logging).
   - **
otebook.ipynb** (atau template eksplorasi): Notebook untuk EDA dan visualisasi hasil.
4. Hubungkan catatan eksperimen dengan rujukan paper di esearch/summaries/ dan ide di adar/opportunities.md.
5. Tampilkan konfirmasi struktur folder yang telah dibuat di terminal.
