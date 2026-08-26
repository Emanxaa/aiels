# Knowledge Schema & Ontologi

Dokumen ini mendefinisikan entitas inti (entities), relasi (relationships), dan konvensi metadata YAML frontmatter di seluruh Academic OS.

---

## 1. Core Entities

| Entity | Deskripsi | Folder Terkait | Contoh Nilai |
| :--- | :--- | :--- | :--- |
| **Course** | Mata kuliah terdaftar | `courses/` | `STA501`, `STA511`, `STA561`, `STA581` |
| **Concept** | Teori atau konsep statistik/AI | `courses/`, `memory/` | `Bayes`, `Convex Optimization`, `Rank Matrix` |
| **Method** | Algoritma atau teknik analisis | `research/`, `courses/` | `CatBoost`, `LOF (Local Outlier Factor)`, `k-NN` |
| **Paper** | Publikasi atau jurnal referensi | `research/papers/` | `Paper X`, `Attention Is All You Need` |
| **Dataset** | Kumpulan data studi atau riset | `research/datasets/` | `Sakernas`, `Susenas`, `Kaggle Dataset` |
| **Professor** | Dosen pengampu / pembimbing | `courses/` | `Dosen IPB` |
| **Project** | Proyek riset atau implementasi | `research/`, `dashboard/` | `Project ATLAS`, `Academic OS` |

---

## 2. Core Relationships

```text
Paper
  └── uses ────────────► Method
                          └── related_to ──► Concept
                                               └── taught_in ──► Course
                                                                   └── taught_by ──► Professor

Project
  ├── requires_dataset ─► Dataset
  ├── implements ───────► Method
  └── cites ────────────► Paper