# Sprint Retrospective & Engineering Review

* **Sprint:** Sprint 1 — Foundation & MVP Architecture
* **Tanggal:** 2026-08-26
* **Status:** Evaluasi Berkala

---

## 1. Completed (Yang Berhasil Diselesaikan)
- Arsitektur 4-Layer Academic OS (Foundation, Knowledge, Workflow, Agents) selesai dibangun.
- Pipeline riset, integrasi Research Radar, dan 5 skill agen spesialis aktif.
- Standar manajemen proyek ala Scrum (Backlog, Granular Issues, Sprint Plan, DoD) telah terstruktur di folder \project/\.

## 2. Blockers & Bottlenecks (Hambatan)
- Format string multi-baris PowerShell di terminal VS Code sempat tertahan (solusi: inline command / Set-Content terisolasi).
- Keterbatasan hardware lokal untuk training model berat (solusi: arsitektur modular \src/\ + \config.yaml\ untuk dieksekusi di cloud GPU).

## 3. Lessons Learned (Pembelajaran)
- Memisahkan coding dan eksperimen dari format monolithic notebook ke modular scripts membuat AI Agent bekerja jauh lebih cepat dan minim error.
- Menyimpan ide riset seketika di \adar/\ mencegah hilangnya gagasan berharga.

## 4. Next Sprint Focus (Sprint 2)
- **Topik Utama:** Refactoring proyek tesis Sentiment Analysis milik teman menjadi pipeline modular (\src/\, \config.yaml\, \main.py\).
- **Eksplorasi Riset:** Pengujian metode *Local Outlier Factor (LOF)* dan *CatBoost* pada dataset benchmark.
