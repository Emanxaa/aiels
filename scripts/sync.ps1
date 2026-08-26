$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
Write-Host "=== Academic OS Auto-Sync: $timestamp ===" -ForegroundColor Cyan
git add .
$status = git status --porcelain
if ($status) {
    git commit -m "Academic OS Sync: $timestamp [automated]"
    git push origin main
    Write-Host "[✓] Berhasil sinkronisasi ke GitHub." -ForegroundColor Green
} else {
    Write-Host "[=] Tidak ada perubahan file untuk di-commit." -ForegroundColor Yellow
}
