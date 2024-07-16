# https://www.mbnq.pl/
# kills all non-essential processes in windows11

# Define exit codes
$exitSuccess = 0
$exitUserCancelled = 1
$exitError = 2

# Prompt the user for confirmation
$confirmation = Read-Host "Do you want to kill all non-essential processes? (y/n)"

if ($confirmation -ne 'y') {
    Write-Host "Cancelled by user"
    exit $exitUserCancelled
}

Write-Host "WIP..."

try {
    # exclute these
    $essentialProcesses = @(
        'Idle', 'System', 'Registry', 'smss', 'csrss', 'wininit', 'services', 
        'lsass', 'svchost', 'winlogon', 'dwm', 'explorer', 'ShellExperienceHost', 
        'SearchUI', 'StartMenuExperienceHost', 'RuntimeBroker', 'ekrn', 'egui'
    )

    Get-Process | Where-Object { 
        $_.Name -notin $essentialProcesses -and $_.SessionId -ne 0 
    } | ForEach-Object { 
        $_.CloseMainWindow() | Out-Null
        Start-Sleep -Milliseconds 100
        if (!$_.HasExited) { 
            $_.Kill() 
        } 
    }

    Write-Host "Done!"
    $exitCode = $exitSuccess
} catch {
    Write-Host "Error: $_"
    $exitCode = $exitError
}

Write-Host "Press any key to exit..."
[void][System.Console]::ReadKey($true)

exit $exitCode
