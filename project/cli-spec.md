# Academic OS - CLI Specification (DX Interface)

Dokumen ini mendefinisikan kontrak interface dan perintah CLI cepat untuk seluruh alur kerja operasional.

| Command | Script Path | Fungsi & Tujuan |
| :--- | :--- | :--- |
| **setup** | .\scripts\setup.ps1 | Inisialisasi awal environment, verifikasi dependensi, dan pembuatan template |
| **new-day** | .\scripts\new-day.ps1 | Generate file jurnal harian baru dari template & buka di editor |
| **new-lecture** | .\scripts\new-lecture.ps1 <MK> <Topik> | Setup template catatan pertemuan kuliah baru di courses/<MK>/ |
| **new-paper** | .\scripts\new-paper.ps1 <Slug> | Inisialisasi workspace riset paper lengkap di esearch/papers/<Slug>/ |
| **sync** | .\scripts\sync.ps1 | Eksekusi auto-commit & push Git ke GitHub |
| **doctor** | .\scripts\doctor.ps1 | Audit diagnostik integritas sistem, repositori, dan kelengkapan folder |
