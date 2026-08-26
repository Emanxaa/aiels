param([Parameter(Mandatory=$true)][string]$PaperSlug)

$paperDir = "research\papers\$PaperSlug"
New-Item -ItemType Directory -Path $paperDir -Force | Out-Null

$summaryFile = "$paperDir\summary.md"
$notesFile = "$paperDir\notes.md"
$expFile = "$paperDir\experiment.md"

if (Test-Path "templates\paper.md") {
    $template = Get-Content "templates\paper.md" -Raw
    $template = $template -replace '\{\{title\}\}', $PaperSlug
    Set-Content -Path $summaryFile -Value $template -Encoding UTF8
} else {
    Set-Content -Path $summaryFile -Value "# Paper Summary: $PaperSlug" -Encoding UTF8
}

Set-Content -Path $notesFile -Value "# Reading Notes: $PaperSlug

## Kutipan & Observasi Mentah
- " -Encoding UTF8
Set-Content -Path $expFile -Value "# Experiment Ideas: $PaperSlug

## Potensi Replikasi Kode
- " -Encoding UTF8

Write-Host "[✓] Workspace paper berhasil dibuat di: $paperDir" -ForegroundColor Green
Write-Host "    - $summaryFile" -ForegroundColor DarkGray
Write-Host "    - $notesFile" -ForegroundColor DarkGray
Write-Host "    - $expFile" -ForegroundColor DarkGray
if (Get-Command code -ErrorAction SilentlyContinue) { code $summaryFile }
