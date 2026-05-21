cd C:\Users\Zarchy\fossil-contracting\frontend\static\images

$projects = @("trabablas-interchange", "harare-beitbridge", "harare-chirundu", "lorraine-drive")

foreach ($proj in $projects) {
    Write-Host "`n=== Processing $proj ===" -ForegroundColor Cyan
    $projPath = ".\$proj"
    
    # Get ALL files recursively (any subdirectory depth)
    $allFiles = @(Get-ChildItem -Path $projPath -File -Recurse -ErrorAction SilentlyContinue)
    
    Write-Host "Total files: $($allFiles.Count)"
    
    if ($allFiles.Count -gt 10) {
        # Sort by size (smallest first)
        $files = $allFiles | Sort-Object Length
        $keep = $files[0..9]
        $delete = $files[10..($allFiles.Count - 1)]
        
        Write-Host "Keeping: 10 smallest images" -ForegroundColor Green
        Write-Host "Deleting: $($delete.Count) larger images" -ForegroundColor Yellow
        
        # Delete the larger files
        $deleteCount = 0
        foreach ($file in $delete) {
            Remove-Item -Path $file.FullPath -Force
            $deleteCount++
            if ($deleteCount % 50 -eq 0) { Write-Host "  Deleted $deleteCount files..." }
        }
        Write-Host "✓ Deleted $($delete.Count) files" -ForegroundColor Green
    } else {
        Write-Host "✓ Already has $($allFiles.Count) files (keep as is)" -ForegroundColor Gray
    }
}

Write-Host "`n=== Final count ===" -ForegroundColor Cyan
foreach ($proj in $projects) {
    $count = @(Get-ChildItem ".\$proj" -File -Recurse -ErrorAction SilentlyContinue).Count
    Write-Host "$proj : $count files"
}
