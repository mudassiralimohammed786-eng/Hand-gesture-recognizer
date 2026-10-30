@echo off
cd /d "%~dp0"
echo Starting Hand Gesture AI Web Application...
start http://localhost:5000
if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" app.py
) else (
    python app.py
)
pause

