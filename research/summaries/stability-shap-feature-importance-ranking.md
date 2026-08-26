---
type: summary
title: "Stability of SHAP-Based Feature Importance Ranking under Class Imbalance, Feature Correlation, and Feature Dimensionality"
authors: "Amri Luthfi Najih, Bagus Sartono, Septian Rahardiantoro"
year: 2026
venue: "Jurnal Statistika dan Komputasi (STATKOM), Vol. 5 No. 1"
doi: "https://doi.org/10.32665/statkom.v5i1.6455"
topic: Interpretable Machine Learning
tags: [SHAP, XGBoost, LightGBM, SRA, Class Imbalance, Feature Importance, Interpretability]
source: research/papers/test.pdf
status: Selesai
---

# Stability of SHAP-Based Feature Importance Ranking

## Masalah

Model *gradient boosting* (XGBoost, LightGBM) memiliki kinerja prediksi tinggi namun bersifat *black-box*, sehingga memerlukan metode interpretasi seperti SHAP untuk menjelaskan kontribusi fitur. Masalah yang diangkat:

- Stabilitas interpretasi SHAP dapat dipengaruhi oleh karakteristik data **dan** model yang digunakan, namun belum dievaluasi secara sistematis.
- Studi sebelumnya (Dharmawan et al., 2022) hanya membatasi analisis pada *class imbalance* dan tidak meninjau korelasi fitur serta dimensionalitas fitur.
- Kebutuhan untuk mengetahui apakah SHAP andal diterapkan pada data non-ideal (imbalance ekstrem, korelasi tinggi) sebelum digunakan mendukung pengambilan keputusan.

## Metode

Studi kuantitatif dengan dua pendekatan: **simulasi terkontrol** dan **data empiris klaim BPJS Kesehatan**.

**Simulasi:**
- 64 dataset dari kombinasi proporsi kelas minoritas $r \in \{0.01, 0.1, 0.3, 0.5\}$, korelasi fitur $\pi \in \{0, 0.2, 0.5, 0.95\}$, dan jumlah fitur $p \in \{7, 15, 25, 35\}$.
- Populasi 600.000, sampel acak sederhana 100.000, split training-tes 70:30 (stratified).
- Data dibangkitkan:
  - $X \sim \mathcal{N}(0, \Sigma)$ dengan matriks kovarians $\Sigma_{ij} = \sigma^2$ bila $i=j$ dan $\pi\sigma^2$ bila $i \neq j$.
  - Fungsi target: $f(X) = 0.9X_1 + 0.7X_2 - 0.5X_3 + 0.3X_6 + 0.01X_7$; fitur relevan sejati $X_1, X_2, X_3, X_6, X_7$ (dengan $X_7$ sangat lemah).
  - Noise $\epsilon \sim \mathcal{N}(0, \sigma^2)$, probabilitas via sigmoid $P = \frac{1}{1 + e^{-score}}$, target $y \sim \text{Bernoulli}(P)$.
- 100 kali pengulangan (split → modeling → SHAP) per kondisi.

**Model:** XGBoost (strategi *level-wise*) dan LightGBM (*leaf-wise*). Hiperparameter XGBoost: `n_estimators=100`, `max_depth=6`, `learning_rate=0.1`, log-loss; LightGBM memakai default, agar komparabel. Random seed tetap untuk reproduktibilitas.

**SHAP:** berbasis nilai Shapley (cooperative game theory)
$$\phi_j(val) = \sum_{S \subseteq \{1,\dots,p\}\setminus\{j\}} \frac{|S|!\,(p-|S|-1)!}{p!}\big(val(S \cup \{j\}) - val(S)\big)$$

**SRA (Sequential Rank Agreement)** untuk mengukur kesepakatan ranking antar daftar yang diurutkan:
$$sra_L(d) = \frac{1}{|S(d)|} \sum_{X_P \in S(d)} \hat{A}_L(X_P)$$
Nilai SRA lebih kecil = ranking lebih stabil, terutama pada posisi top-ranked.

**BPJS Kesehatan:** pada data empiris, diterapkan penanganan imbalance SMOTE dan ADASYN (hanya pada training data setelah split, mencegah *data leakage*), menggunakan `imblearn`.

## Dataset

| Dataset | Deskripsi | Fitur | Target |
| :--- | :--- | :--- | :--- |
| Simulasi | 64 dataset, 600.000 populasi, split 70:30 | $p \in \{7,15,25,35\}$ numerik | Biner (Bernoulli) |
| BPJS Kesehatan 2018–2023 | 586.733 partisipan, kelas minoritas mental health 7.826 (1.33%) | 22 (14 numerik + 8 kategorikal), dikelompokkan: demografi, status keanggotaan/sosioekonomi, akses kesehatan, riwayat utilisasi | Biner: status gangguan mental (INACBGs) |

**Metrik evaluasi:** akurasi, balanced accuracy, sensitivitas, spesifisitas; plus SRA untuk stabilitas ranking.

## Hasil

**Simulasi:**
- SHAP andal mengembalikan fitur dominan sejati $X_1, X_2, X_3, X_6$ dengan akurasi ranking > 90% pada kondisi korelasi rendah–moderat (0, 0.2, 0.5).
- Fitur berkoefisien sangat kecil ($X_7 = 0.01$) tidak stabil, sulit dibedakan dari fitur non-relevan — kelemahan SHAP pada fitur marginal.
- Stabilitas menurun pada korelasi sangat tinggi (0.95) dan imbalance ekstrem (proporsi 0.1 dan 0.01).
- SRA terkecil pada kedalaman ranking dangkal; meningkat seiring kedalaman bertambah (fitur lemah ikut dibandingkan).

**BPJS Kesehatan (Tabel performa):**

| Model | Handling | Accuracy (test) | Balanced Acc (test) | Sensitivity (test) | Specificity (test) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| LightGBM | None | 0.9888 | 0.6978 | 0.3989 | 0.9967 |
| LightGBM | ADASYN | 0.9857 | 0.8058 | 0.6209 | 0.9906 |
| LightGBM | SMOTE | 0.9854 | 0.8139 | 0.6377 | 0.9901 |
| XGBoost | None | 0.9888 | 0.6991 | 0.4015 | 0.9968 |
| XGBoost | ADASYN | 0.9854 | 0.8042 | 0.6181 | 0.9904 |
| XGBoost | SMOTE | 0.9851 | 0.8137 | 0.6375 | 0.9898 |

**Stabilitas SRA (Tabel 3):**

| Model | Handling | Mean SRA |
| :--- | :--- | :--- |
| LightGBM | None | 2.2534 |
| LightGBM | ADASYN | **0.5350** |
| LightGBM | SMOTE | 0.5950 |
| XGBoost | None | 1.5085 |
| XGBoost | ADASYN | 0.6525 |
| XGBoost | SMOTE | 0.7661 |

- Penanganan imbalance meningkatkan baik kinerja (terutama sensitivitas) maupun stabilitas interpretasi.
- **Trade-off:** SMOTE unggul deteksi kelas minoritas (sensitivity), ADASYN unggul stabilitas ranking (SRA lebih rendah). Pilihan metode bergantung tujuan analisis.
- Fitur paling berpengaruh pada LightGBM+SMOTE: *family mental-health clinic visit history* (SHAP 1.26), gender (0.49), tipe fasilitas primer (0.47), kelas perawatan (0.46).

## Limitation

- Komponen simulasi terbatas pada struktur **linear** pada proses pembangkitan data; temuan hanya valid dalam konteks kondisi simulasi yang ditetapkan.
- Hiperparameter tidak dioptimasi (ditetapkan agar komparabel), bukan untuk mengoptimalkan performa.
- Nilai SHAP diinterpretasikan sebagai kontribusi prediktif, **bukan** bukti hubungan kausal.
- Akurasi tinggi pada data imbalance menyesatkan; perlu interpretasi hati-hati karena didominasi kelas mayoritas.

## Peluang Penelitian

- Membandingkan stabilitas SHAP dengan metode interpretabilitas lain (LIME, *permutation feature importance*).
- Metrik evaluasi tambahan untuk klasifikasi imbalance: PR-AUC, F1-score, precision per kelas.
- Perluasan ke dataset kesehatan lain, luaran penyakit berbeda, model ML lain, dan teknik penanganan imbalance alternatif untuk generalisasi.
- Menguji stabilitas SHAP pada mekanisme pembangkitan data non-linear, efek interaksi antarfitur, dan struktur korelasi berbeda.
- Menyelidiki perlakuan terhadap fitur marginal yang tidak stabil (koefisien kecil) sebelum dijadikan dasar pengambilan keputusan.