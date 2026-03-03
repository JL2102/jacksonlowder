@echo off
title Wedding Server - Press Ctrl+C to stop
echo ============================================================
echo Wedding Mystery Server
echo ============================================================
echo.
echo Server starting on port 8000...
echo.
echo Opening browser...
start http://localhost:8000
echo.
echo ============================================================
echo Server is running!
echo.
echo TO STOP: Press Ctrl+C, then close this window
echo Or just close this window anytime
echo ============================================================
echo.

cd /d "%~dp0"
python -m http.server 8000

echo.
echo Server stopped!
pause
