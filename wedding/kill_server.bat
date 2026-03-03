@echo off
echo Stopping all Python HTTP servers...
echo.

taskkill /F /IM python.exe /FI "WINDOWTITLE eq *http.server*" 2>nul

if %ERRORLEVEL% EQU 0 (
    echo Python servers stopped successfully!
) else (
    echo No Python servers were running.
)

echo.
echo You can now start the server again.
echo.
pause
