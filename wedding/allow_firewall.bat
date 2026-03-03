@echo off
echo Adding Windows Firewall rule for Python HTTP Server...
echo.
echo This will allow other devices on your network to access the server.
echo You may need to run this as Administrator.
echo.

netsh advfirewall firewall add rule name="Python HTTP Server" dir=in action=allow protocol=TCP localport=8000

echo.
echo Firewall rule added!
echo.
echo Now try accessing the server from your fiance's phone again.
echo.
pause
