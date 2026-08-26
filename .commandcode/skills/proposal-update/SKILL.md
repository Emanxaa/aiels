---
name: proposal-update
description: Memperbarui draft proposal tesis secara dinamis berdasarkan temuan di literature-map, radar, dan eksperimen.
---

# Proposal Update Skill

Tujuan: Menjaga proposal tesis sebagai 'dokumen hidup' dengan menyintesis literature map, research gaps, dan hasil eksperimen terbaru.

## Langkah Kerja:
1. Pindai file esearch/literature-map.md, adar/opportunities.md, dan ringkasan paper di esearch/summaries/.
2. Identifikasi pembaruan terbaru terkait research gap, metode komputasi/statistika, atau dataset potensial.
3. Perbarui dan sinkronkan file-file inti di folder 	hesis/:
   - **	hesis/proposal.md**: Perbarui latar belakang, gap riset, metodologi, dan kontribusi.
   - **	hesis/questions.md**: Tajamkan rumusan masalah (Research Questions).
   - **	hesis/hypotheses.md**: Perbarui hipotesis kerja yang dapat diuji secara empiris/matematis.
   - **	hesis/roadmap.md**: Perbarui target timeline, tahapan pra-proposal, seminar, hingga sidang.
4. Tampilkan log ringkasan bagian proposal apa saja yang telah diperbarui di terminal.
