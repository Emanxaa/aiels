# Research Hypotheses (H)

- **H1:** Penanganan *class imbalance* (SMOTE/ADASYN) menurunkan SRA (ranking SHAP lebih stabil) dibanding tanpa handling, pada semua tingkat imbalance dan model gradient boosting. *(Empiris: Najih et al., 2026 — LightGBM ADASYN SRA=0.5350 vs None 2.2534; XGBoost ADASYN 0.6525 vs None 1.5085.)*
- **H2:** Terdapat trade-off sistematis: SMOTE memberikan sensitivitas tertinggi sedangkan ADASYN memberikan SRA terendah — tidak ada metode yang dominan untuk semua kondisi, sehingga keputusan pemilihan bergantung tujuan analisis (deteksi vs stabilitas interpretasi).
- **H3:** Kriteria adaptif berbasis karakteristik data yang dapat diukur sebelum modeling (proporsi kelas minoritas, korelasi rata-rata antar fitur, jumlah fitur, indikator non-linearitas/interaksi) mampu memilih kombinasi model × metode dengan kinerja (sensitivitas, PR-AUC) dan stabilitas (SRA) yang memenuhi ambang yang ditetapkan, dan tetap konsisten pada validasi lintas dataset (Susenas, benchmark).
