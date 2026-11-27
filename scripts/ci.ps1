# Every gate of the site, one result line: CI: ALL GATES PASSED or CI: FAILED (<gate>).
# Needs only Python 3.10+ with the markdown package (pip install markdown); not the editor repository.
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

python -c "import markdown" 2>$null
if ($LASTEXITCODE -ne 0) { Write-Host "CI: FAILED (python markdown package missing: pip install markdown)"; exit 1 }

# With the editor repository at hand (.source-path or $env:LEVELDOT_EDITOR_REPO), the pages are built
# first: a build that stops (an unknown key, say) fails the gate instead of leaving old pages behind.
if ((Test-Path ".source-path") -or $env:LEVELDOT_EDITOR_REPO) {
    python scripts/build.py
    if ($LASTEXITCODE -ne 0) { Write-Host "CI: FAILED (build)"; exit 1 }
}

python scripts/check_site.py
if ($LASTEXITCODE -ne 0) { Write-Host "CI: FAILED (site check)"; exit 1 }

Write-Host "CI: ALL GATES PASSED"
