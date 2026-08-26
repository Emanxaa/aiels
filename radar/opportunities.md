---
type: radar
category: opportunities
last_updated: 2026-08-26
---

# Research Opportunities

Dokumentasi ide penelitian, topik tesis, dan peluang proyek akademik.

---

## 1. SWAC-CatBoost (Sliding Window Adaptive Calibration)

* **Ide:** Integrasi adaptasi bobot dinamis pada algoritma CatBoost untuk menangani *concept drift* pada data tabular deret waktu.
* **Sumber Inspirasi:** Paper A & benchmark deteksi anomali.
* **Domain:** Tabular Machine Learning / Statistical Learning.
* **Status:** Eksplorasi
* **Terkait:**
  * **Metode:** [[knowledge/methods#CatBoost]]
  * **Konsep:** [[knowledge/concepts]]
* **Next Action:** Cari dataset uji publik di Kaggle/BPS dan siapkan eksperimen awal di `research/`.

---

## 2. Fraud Detection with Local Outlier Factor & Bayesian Updating

* **Ide:** Pipeline deteksi anomali transaksi menggunakan Local Outlier Factor (LOF) yang dikombinasikan dengan pembaruan probabilitas posterior Bayesian.
* **Sumber Inspirasi:** Diskusi pipeline data-to-decision.
* **Domain:** Financial Anomaly Detection.
* **Status:** Ide Awal
* **Next Action:** Eksplorasi literatur LOF dan tinjau ketersediaan dataset transaksi.

---

## 3. Adaptive Imbalance Handling for Stable SHAP Interpretation

* **Ide:** Kriteria adaptif untuk memilih metode penanganan *class imbalance* (SMOTE vs ADASYN) yang menyeimbangkan deteksi kelas minoritas dan stabilitas interpretasi SHAP diukur dengan SRA, pada data tabular tidak seimbang.
* **Sumber Inspirasi:** Najih et al. (2026) — menemukan trade-off: SMOTE unggul sensitivitas, ADASYN unggul stabilitas ranking (LightGBM ADASYN SRA=0.5350 vs tanpa handling 2.2534).
* **Domain:** Interpretable ML / Tabular Learning / Imbalanced Classification.
* **Status:** Ide Awal
* **Terkait:**
  * **Paper:** [[research/summaries/stability-shap-feature-importance-ranking]]
  * **Metode:** [[knowledge/methods#SHAP]], [[knowledge/methods#XGBoost]], [[knowledge/methods#LightGBM]]
  * **Konsep:** [[knowledge/concepts#Class-Imbalance]]
* **Next Action:** Tinjau ulang metrik SRA pada data klaim; rancang simulasi tambahan dengan struktur non-linear dan interaksi fitur sesuai saran limitasi paper.
