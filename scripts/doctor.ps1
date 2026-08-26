Write-Host "=== Academic OS System Health Doctor ===" -ForegroundColor Cyan
$healthy = $true

function Check-Component($name, $condition, $hint) {
    if ($condition) {
        Write-Host "  [✓] $name : OK" -ForegroundColor Green
    } else {
        Write-Host "  [✗] $name : FAILED ($hint)" -ForegroundColor Red
        $script:healthy = $false
    }
}

Check-Component "Git Binary" (Get-Command git -ErrorAction SilentlyContinue) "Pasang Git di PATH"
Check-Component "Git Repository" (Test-Path ".git") "Jalankan git init"
Check-Component "Core AGENTS Routing" (Test-Path "AGENTS.md") "Buat AGENTS.md"
Check-Component "README Dashboard" (Test-Path "README.md") "Buat README.md"
Check-Component "Knowledge Schema" (Test-Path "knowledge-schema.md") "Buat knowledge-schema.md"
Check-Component "Memory Layer" (Test-Path "memory\goals.md") "Inisialisasi memory/"
Check-Component "Templates Core" (Test-Path "templates\daily.md") "Pastikan templates lengkap"
Check-Component "Skills Modules" (Test-Path ".commandcode\skills\course-mentor\SKILL.md") "Verifikasi skills agen"

Write-Host "----------------------------------------"
if ($healthy) {
    Write-Host "Verdict: System Healthy! (Siap Operasional Penuh)" -ForegroundColor Green
} else {
    Write-Host "Verdict: System Warning! (Perbaiki checklist merah)" -ForegroundColor Yellow
}
