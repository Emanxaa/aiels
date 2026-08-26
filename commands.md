# Academic OS - Command Library

Dokumentasi pintasan perintah (slash commands) untuk mempercepat alur kerja akademik harian.

| Command | Fungsi | Input / Trigger | Output Utama |
| :--- | :--- | :--- | :--- |
| `/start-day` | Membaca dashboard & menyusun prioritas harian | Kondisi awal hari | Agenda kerja & fokus harian |
| `/lecture` | Memproses materi kuliah menjadi catatan terstruktur | Catatan mentah / slide materi | File di `courses/<MK>/lecture-XX.md` |
| `/coding` | Dokumentasi script, modularisasi, dan implementasi | Snippet / skrip kode | Catatan teknis & modul proyek |
| `/paper` | Membaca, menganalisis, dan meringkas paper riset | PDF / teks paper | Ringkasan di `research/summaries/` |
| `/weekly` | Evaluasi mingguan dan retrospeksi progres | Log jurnal harian | Review di `journal/weekly/` |
| `/shutdown` | Tutup hari kerja dan simpan status terkini | Aktivitas hari ini | Update `dashboard/` & jurnal |

---

## Contoh Alur Penggunaan

1. **Pagi Hari:** Jalankan `/start-day` untuk memuat konteks dan 3 target utama.
2. **Saat/Setelah Kuliah:** Jalankan `/lecture` lalu tempel catatan mentah materi kuliah.
3. **Malam Hari:** Jalankan `/shutdown` untuk menutup konteks dan menyinkronkan dashboard.
