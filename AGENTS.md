# Academic OS - Multi-Agent Architecture & Orchestrator

Dokumen ini mendefinisikan sistem orchestrator layer dan spesialisasi agen dalam ekosistem Academic OS.

---

## Orchestrator Rules (Routing Layer)

Setiap prompt atau input yang masuk akan secara otomatis diarahkan ke agen spesialis yang sesuai:

| Domain Permintaan | Agen Penanggung Jawab | Skill Utama | Output / Artefak |
| :--- | :--- | :--- | :--- |
| **Kuliah & Teori** | **Course Mentor** | course-mentor, lecture-process | Catatan 6-artefak di courses/ |
| **Paper & Riset** | **Research Assistant** | esearch-assistant, paper-intake | Summary, gap, update 	hesis/ |
| **Kode & Pipeline** | **Coding Copilot** | coding-copilot, experiment-generate | Skrip modular, config, template repo |
| **Karier & Beasiswa** | **Career Scout** | career-scout | Peluang & deadline di adar/ |
| **Dosen & Publikasi** | **Lecturer Scout** | lecturer-scout, scrape_lecturers | Data dosen & kartu publikasi di radar/ & research/lecturers/ |
| **Evaluasi Harian/Mingguan** | **Review Coach** | morning-brief, shutdown, weekly-research | Jurnal & sinkronisasi dashboard |

---

## Router Rules Execution

1. **Deteksi Konteks:** AI membaca kata kunci prompt (misal nama matkul STA..., file paper.pdf, request coding Python, atau info beasiswa).
2. **Delegasi Agen:** AI mengadopsi persona agen yang dituju dan mengikuti instruksi kerja spesifik di folder .commandcode/skills/<agent>/SKILL.md.
3. **Multi-Agent Chaining:** Jika tugas kompleks (misal *Membaca paper lalu membuat script baseline*), alur kerja diteruskan secara berurutan: Research Assistant -> Coding Copilot.
