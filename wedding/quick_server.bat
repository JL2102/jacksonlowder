@echo off
echo Starting server on port 8000...
echo If port 8000 is busy, close other Python windows first!
echo.
echo The page will open at: http://localhost:8000
echo.
cd /d "%~dp0"
start http://localhost:8000
python -m http.server 8000
