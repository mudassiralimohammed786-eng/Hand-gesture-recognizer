@echo off
cd /d "%~dp0"
set "PATH=C:\Users\mudas\.local\mingit\cmd;%PATH%"
echo ========================================================
echo Pushing Hand Gesture Recognition AI to GitHub...
echo Repository: https://github.com/mudassiralimohammed786-eng/Hand-gesture-recognizer.git
echo ========================================================
echo.
git push -u origin main
echo.
pause
