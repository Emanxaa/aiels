Write-Host "=== Academic OS - Setup & Environment Bootstrap ===" -ForegroundColor Cyan

# 1. Check Git
if (Get-Command git -ErrorAction SilentlyContinue) {
    Write-Host "[✓] Git terpasang: git version 2.51.0.windows.1" -ForegroundColor Green
} else {
    Write-Host "[!] Git tidak ditemukan. Silakan pasang Git." -ForegroundColor Red
}

# 2. Check VS Code
if (Get-Command code -ErrorAction SilentlyContinue) {
    Write-Host "[✓] VS Code CLI terdeteksi" -ForegroundColor Green
} else {
    Write-Host "[-] VS Code CLI 'code' tidak ada di PATH (opsional)." -ForegroundColor Yellow
}

# 3. Check Command Code
if (Get-Command cmdc -ErrorAction SilentlyContinue) {
    Write-Host "[✓] Command Code (cmdc) terpasang" -ForegroundColor Green
} else {
    Write-Host "[-] cmdc belum terdeteksi di global PATH." -ForegroundColor Yellow
}

# 4. Verifikasi & Buat Folder Inti
$folders = @('courses', 'research\papers', 'research\summaries', 'journal\daily', 'journal\weekly', 'knowledge', 'radar', 'experiments', 'thesis', 'templates', 'memory', 'dashboard', 'scripts', 'project', '.commandcode\skills')
foreach ($f in $folders) {
    if (-not (Test-Path $f)) {
        New-Item -ItemType Directory -Path $f -Force | Out-Null
        Write-Host "[+] Membuat folder: $f" -ForegroundColor DarkGray
    }
}
Write-Host "[✓] Struktur direktori lengkap." -ForegroundColor Green
Write-Host "Setup selesai. Sistem siap digunakan!" -ForegroundColor Cyan
