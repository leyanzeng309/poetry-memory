@echo off
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
    py -3 serve_local.py
    goto :end
)
where python >nul 2>nul
if %errorlevel%==0 (
    python serve_local.py
    goto :end
)
echo Python 3 is required to start 松间 locally.
echo Install Python 3, then double-click this file again.
pause
:end
