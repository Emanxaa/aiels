# Draft Proposal Tesis / Riset

## 1. Latar Belakang & Motivasi

- Model *gradient boosting* (XGBoost, LightGBM, CatBoost) unggul pada data tabular namun bersifat *black-box*, sehingga interpretasi menjadi prasyarat untuk mendukung pengambilan keputusan (Najih et al., 2026).
- SHAP adalah metode interpretasi berbasis nilai Shapley yang populer, namun keandalannya belum teruji sistematis pada data non-ideal, khususnya **class imbalance** yang umum di domain kesehatan, sosial, dan keuangan.
- Najih et al. (2026) menunjukkan penanganan imbalance (SMOTE/ADASYN) meningkatkan **sekaligus** kinerja (sensitivitas) dan stabilitas ranking SHAP (SRA), tetapi terdapat **trade-off**: SMOTE unggul deteksi kelas minoritas, ADASYN unggul stabilitas interpretasi (LightGBM ADASYN SRA=0.5350 vs tanpa handling 2.2534).
- Belum ada **kriteria adaptif** yang memandu pemilihan metode penanganan imbalance berdasarkan karakteristik data, sehingga pemilihan metode saat ini bersifat ad hoc dan dapat mengorbankan stabilitas interpretasi.
- Motivasinya: menyediakan pedoman objektif bagi analis agar interpretasi SHAP tetap andal (ranking stabil) sekaligus deteksi kelas minoritas tetap optimal.

## 2. Research Gap

- Studi sebelumnya (Dharmawan et al., 2022; Najih et al., 2026) mengevaluasi efek *class imbalance* pada interpretasi SHAP, tetapi **belum** menurunkan aturan/kriteria adaptif untuk memilih metode penanganan imbalance.
- Komponen simulasi Najih et al. (2026) terbatas pada struktur **linear**; pengaruh non-linearitas dan interaksi fitur terhadap stabilitas SHAP belum diuji.
- Evaluasi stabilitas pada data empiris baru diuji pada satu domain (klaim BPJS Kesehatan); perlu generalisasi ke data tabular tidak seimbang lain (misal kemiskinan Susenas) dan model lain (CatBoost).
- Metrik tambahan (PR-AUC, F1 per kelas) belum dipadukan dengan SRA untuk menyusun keputusan pemilihan metode secara bersamaan (performance–interpretability trade-off).

## 3. Research Questions

- **RQ1:** Bagaimana karakteristik data (tingkat imbalance, korelasi fitur, dimensionalitas, non-linearitas) memengaruhi stabilitas ranking SHAP (SRA) pada model gradient boosting dengan dan tanpa penanganan imbalance?
- **RQ2:** Kriteria adaptif apa yang dapat memilih metode penanganan imbalance (tanpa handling, SMOTE, ADASYN) agar menyeimbangkan deteksi kelas minoritas (sensitivitas, PR-AUC) dan stabilitas interpretasi SHAP (SRA)?
- **RQ3:** Seberapa konsisten kriteria tersebut berlaku lintas dataset (simulasi, Susenas, benchmark tabular) dan model (XGBoost, LightGBM, CatBoost)?

## 4. Hipotesis

- **H1:** Penanganan imbalance meningkatkan stabilitas ranking SHAP (SRA lebih rendah) dibanding tanpa handling pada semua tingkat imbalance.
- **H2:** Tidak ada satu metode yang dominan untuk semua kondisi — SMOTE unggul pada sensitivitas sedangkan ADASYN pada SRA — sehingga kriteria adaptif diperlukan.
- **H3:** Kriteria adaptif berbasis karakteristik data (proporsi kelas minoritas, korelasi, dimensionalitas) menghasilkan kombinasi metode yang memenuhi ambang kinerja dan stabilitas sekaligus.

## 5. Metode & Kerangka Analisis

- **Kerangka umum:** simulasi terkontrol → kalibrasi kriteria adaptif → validasi empiris lintas dataset.
- **Model:** XGBoost, LightGBM, CatBoost (hiperparameter tetap komparabel; tuning terbatas pada tahap validasi).
- **Penanganan imbalance:** tanpa handling, SMOTE, ADASYN (diterapkan hanya pada training data setelah split, mencegah *data leakage*; `imblearn`).
- **Interpretasi:** SHAP *mean absolute value*; stabilitas diukur dengan **SRA (Sequential Rank Agreement)** — semakin kecil semakin stabil.
- **Simulasi:** perluasan desain Najih et al. (2026) — kombinasi proporsi kelas minoritas $r$, korelasi $\pi$, jumlah fitur $p$, **ditambah struktur non-linear dan interaksi fitur** sesuai saran limitasi paper.
- **Metrik:** sensitivitas, balanced accuracy, PR-AUC, F1 per kelas (kinerja); SRA (stabilitas). Keputusan pemilihan metode dievaluasi dengan trade-off kinerja–stabilitas.

## 6. Dataset & Rencana Eksperimen

- **Simulasi:** 64+ kondisi kombinasi $r \in \{0.01, 0.1, 0.3, 0.5\}$, $\pi \in \{0, 0.2, 0.5, 0.95\}$, $p \in \{7,15,25,35\}$ + varian non-linear/interaksi; populasi 600.000, split 70:30 stratified, 100 pengulangan.
- **Susenas (BPS):** mikrodata kemiskinan & sosial-ekonomi; target biner status kemiskinan (kelas minoritas) — belum diunduh, perlu akses.
- **Benchmark tabular:** Kaggle (mis. klaim kesehatan, deteksi anomali transaksi) untuk generalisasi.
- **Tahapan:** (1) reproduksi desain simulasi baseline, (2) ekstensi non-linear, (3) penurunan kriteria adaptif (rule/tree sederhana atau skor), (4) validasi Susenas + benchmark, (5) dokumentasi di `experiments/`.

## 7. Kontribusi Teoretis & Praktis

- **Teoretis:** pemahaman sistematis interaksi karakteristik data × penanganan imbalance × stabilitas interpretasi pada struktur non-linear; kriteria adaptif berbasis SRA.
- **Praktis:** pedoman objektif pemilihan metode penanganan imbalance untuk analis ML (kesehatan, sosial-ekonomi, keuangan) yang membutuhkan interpretasi SHAP yang stabil untuk pengambilan keputusan.
- **Metodologis:** perpaduan metrik kinerja (PR-AUC, F1) dan stabilitas (SRA) dalam satu kerangka keputusan.

---

## Related Knowledge
- **Literature Map:** [[research/literature-map]]
- **Research Opportunities:** [[radar/opportunities]] (Opportunity #3: Adaptive Imbalance Handling)
- **Paper Kunci:** [[research/summaries/stability-shap-feature-importance-ranking]]
- **Eksperimen Terkait:** [[experiments/xgboost-poverty]]
- **Metode:** [[knowledge/methods]] (SHAP, XGBoost, LightGBM, CatBoost)
- **Dataset:** [[knowledge/datasets]] (Susenas, Kaggle)
