param([string]$Date = (Get-Date -Format "yyyy-MM-dd"))

$targetDir = "journal\daily"
if (-not (Test-Path $targetDir)) { New-Item -ItemType Directory -Path $targetDir -Force | Out-Null }

$targetFile = "$targetDir\$Date.md"
if (Test-Path $targetFile) {
    Write-Host "[!] Jurnal hari ini sudah ada: $targetFile" -ForegroundColor Yellow
} else {
    if (Test-Path "templates\daily.md") {
        $content = Get-Content "templates\daily.md" -Raw
        $content = $content -replace '\{\{date\}\}', $Date
        Set-Content -Path $targetFile -Value $content -Encoding UTF8
    } else {
        Set-Content -Path $targetFile -Value "# Daily Journal - $Date

## Fokus Hari Ini
- " -Encoding UTF8
    }
    Write-Host "[✓] Berhasil membuat jurnal harian: $targetFile" -ForegroundColor Green
}

if (Get-Command code -ErrorAction SilentlyContinue) { code $targetFile }
