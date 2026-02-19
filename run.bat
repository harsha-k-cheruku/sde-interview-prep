@echo off
setlocal enabledelayedexpansion

echo 🎯 SDE Interview Prep Tracker
echo ==============================

if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

call venv\Scripts\activate.bat

echo Installing dependencies...
pip install -q -r requirements.txt

echo.
echo ✅ Server starting...
echo 📍 http://localhost:8000/tools/sde-prep
echo.

python -m uvicorn sde_prep.main:app --reload --host 0.0.0.0 --port 8000
