# scripts/load-env.ps1
# Laedt Variablen aus .env.local in die aktuelle PowerShell-Session.
# Benoetigt von MCP-Servern (Linear, Notion), weil OpenCode {env:...} aus
# der Process-Scope des startenden Shells aufloest, nicht aus .env-Dateien.
#
# Verwendung:
#   . .\scripts\load-env.ps1
#   opencode
#
# Oder als One-Liner vor opencode-Start:
#   pwsh -NoProfile -Command ". ./scripts/load-env.ps1; opencode"

$ErrorActionPreference = 'Stop'
$envFile = Join-Path $PSScriptRoot '..' '.env.local'

if (-not (Test-Path -LiteralPath $envFile)) {
    throw "ENV-Datei nicht gefunden: $envFile"
}

$loaded = 0
foreach ($line in Get-Content -LiteralPath $envFile) {
    if ($line -match '^\s*([A-Za-z_][A-Za-z0-9_-]*)\s*=\s*"?((?:[^"\\]|\\.)*)"?\s*$') {
        $name = $Matches[1]
        $raw = $Matches[2]
        # Shell-Unescape: \_ -> _ (und aehnliche)
        $val = [System.Text.RegularExpressions.Regex]::Replace($raw, '\\(.)', { param($m) $m.Groups[1].Value })
        [Environment]::SetEnvironmentVariable($name, $val, 'Process')
        $loaded++
    }
}

Write-Host "[load-env] $loaded Variablen aus .env.local geladen." -ForegroundColor Green
