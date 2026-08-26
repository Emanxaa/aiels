---
type: experiment
name: xgboost-poverty
created: 2026-08-26
status: Scaffold
method: XGBoost
dataset: Susenas (Poverty & Socioeconomic)
---

# Experiment: XGBoost for Poverty Prediction

Memprediksi status kemiskinan rumah tangga menggunakan **XGBoost** pada data sosial-ekonomi **Susenas**. Eksperimen ini juga menyertakan evaluasi interpretabilitas (SHAP) mengingat kemiskinan biasanya merupakan kelas minoritas — sehingga wawasan dari paper SHAP-stability relevan untuk pemilihan penanganan *class imbalance*.

## 1. Hipotesis & Tujuan

- **H1:** XGBoost dapat mencapai *balanced accuracy* dan sensitivitas yang bermakna untuk deteksi rumah tangga miskin (minoritas) pada data Susenas, bukan sekadar akurasi tinggi yang didominasi kelas mayoritas.
- **Tujuan:** Membangun baseline prediksi kemiskinan yang reprodusibel, terukur, dan diinterpretasi via SHAP.

## 2. Baseline

- Model comparator: Logistic Regression / GLM (dari semester statistika) sebagai baseline linear.
- Metode utama: XGBoost (`n_estimators`, `max_depth`, `learning_rate` dari `config.yaml`).

## 3. Metrik Evaluasi

- **Primary:** ROC-AUC, PR-AUC, Balanced Accuracy, F1-score (kls minoritas).
- **Sekunder:** Precision/Recall per kelas; joint akurasi.
- **Interpretasi:** SHAP *mean absolute value* untuk peringkat kepentingan fitur (rujuk evaluasi stabilitas pada paper Najih et al., 2026).

## 4. Rujukan & Keterkaitan

- **Paper:** [[research/summaries/stability-shap-feature-importance-ranking]] — panduan penanganan imbalance (SMOTE vs ADASYN) dan evaluasi stabilitas SHAP untuk XGBoost.
- **Dataset:** [[knowledge/datasets#Susenas]], tercatat pada [[radar/datasets#Susenas]] (BPS, belum diunduh).
- **Metode:** [[knowledge/methods#XGBoost]].

## 5. TODO List

- [ ] Unduh/akses mikrodata Susenas (BPS) dan dokumentasikan skema variabel.
- [ ] Exploratory Data Analysis (EDA) di `notebook.ipynb` (distribusi target, missing, korelasi).
- [ ] Preprocessing & Feature Engineering (klaim tipe variabel, one-hot/ordinal, skala).
- [ ] Baseline model run (GLM + XGBoost) dan logging metrik.
- [ ] Penanganan class imbalance (tanpa handling / SMOTE / ADASYN) + perbandingan.
- [ ] SHAP interpretation & stability check.
- [ ] Hyperparameter tuning & error analysis.