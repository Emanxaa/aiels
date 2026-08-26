# Daily Git Sync Automation Script
$currentDate = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$commitMsg = "Academic OS Auto-sync: $currentDate"

Write-Host "Syncing Academic OS with GitHub..." -ForegroundColor Cyan
git add .
git commit -m $commitMsg
git push
Write-Host "Sync completed successfully at $currentDate" -ForegroundColor Green
