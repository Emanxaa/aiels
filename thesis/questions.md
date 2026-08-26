# Research Questions (RQ)

- **RQ1:** Bagaimana tingkat *class imbalance*, korelasi antar fitur, dimensionalitas, dan non-linearitas struktur data memengaruhi stabilitas ranking SHAP (diukur dengan SRA) pada model gradient boosting (XGBoost, LightGBM, CatBoost) dengan dan tanpa penanganan imbalance (SMOTE/ADASYN)?
- **RQ2:** Kriteria adaptif apa yang dapat merekomendasikan metode penanganan *class imbalance* (tanpa handling, SMOTE, ADASYN) agar menyeimbangkan deteksi kelas minoritas (sensitivitas, PR-AUC) dan stabilitas interpretasi SHAP (SRA)?
- **RQ3:** Seberapa konsisten kriteria adaptif tersebut ketika divalidasi lintas dataset — simulasi terkontrol, data empiris tidak seimbang (Susenas), dan benchmark tabular — serta lintas model (XGBoost, LightGBM, CatBoost)?
