# Installs all SEO skills for Claude Code (Windows PowerShell).
# Usage: right-click this file > "Run with PowerShell"
#   or in PowerShell:  powershell -ExecutionPolicy Bypass -File install-claude-code.ps1
# Project-only install:  ... -File install-claude-code.ps1 C:\path\to\project
param([string]$Project = "")
$Here = Split-Path -Parent $MyInvocation.MyCommand.Path
$Src = Join-Path $Here "..\3-coding-agents\skills"
if (-not (Test-Path $Src)) { $Src = Join-Path $Here "..\skills" }
if ($Project -ne "") { $Dest = Join-Path $Project ".claude\skills" } else { $Dest = Join-Path $HOME ".claude\skills" }
New-Item -ItemType Directory -Force -Path $Dest | Out-Null
$count = 0
Get-ChildItem -Directory $Src | ForEach-Object {
  $target = Join-Path $Dest $_.Name
  if (Test-Path $target) { Remove-Item -Recurse -Force $target }
  Copy-Item -Recurse $_.FullName $target
  Write-Host "  OK $($_.Name)"
  $count++
}
Write-Host ""
Write-Host "Done: $count skills installed in $Dest"
Write-Host "Restart Claude Code, then try: I just started a website. How do I get it on Google?"
Read-Host "Press Enter to close"
