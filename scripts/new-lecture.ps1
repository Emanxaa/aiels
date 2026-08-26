param(
    [Parameter(Mandatory=$true)][string]$Course,
    [Parameter(Mandatory=$true)][string]$Topic
)
$courseDir = "courses\$Course"
New-Item -ItemType Directory -Path $courseDir -Force | Out-Null

$dateStr = Get-Date -Format "yyyy-MM-dd"
$slug = $Topic.ToLower() -replace '\s+', '-'
$targetFile = "$courseDir\$dateStr-$slug.md"

if (Test-Path "templates\lecture.md") {
    $tpl = Get-Content "templates\lecture.md" -Raw
    $tpl = $tpl -replace '\{\{course_code\}\}', $Course -replace '\{\{topic\}\}', $Topic -replace '\{\{date\}\}', $dateStr
    Set-Content -Path $targetFile -Value $tpl -Encoding UTF8
} else {
    Set-Content -Path $targetFile -Value "# $Course: $Topic" -Encoding UTF8
}
Write-Host "[✓] Catatan kuliah baru dibuat: $targetFile" -ForegroundColor Green
if (Get-Command code -ErrorAction SilentlyContinue) { code $targetFile }
