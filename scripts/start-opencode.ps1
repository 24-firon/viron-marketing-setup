# scripts/start-opencode.ps1
# Startet OpenCode TUI mit geladenen ENV-Variablen aus .env.local.
# Benoetigt weil OpenCode MCP-Tokens aus der Process-Scope des
# startenden Shells liest, nicht aus .env-Dateien.

$ErrorActionPreference = 'Stop'
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
& (Join-Path $scriptDir 'load-env.ps1')

# opencode im Vordergrund starten
opencode @args
