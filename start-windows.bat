@echo off
rem Startet Altstadt Rausch ueber einen lokalen Server (noetig fuers Mikrofon).
cd /d "%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -File "tools\server.ps1"
