@echo off
echo ===============================================
echo   Starting Diia FastAPI Server
echo ===============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.11 or higher
    pause
    exit /b 1
)

REM Check if .env exists
if not exist .env (
    echo WARNING: .env file not found!
    echo Please create .env file based on env_example.txt
    pause
    exit /b 1
)

REM Run the FastAPI server
echo Starting FastAPI server on http://localhost:8000
echo API docs available at http://localhost:8000/docs
echo.
python -m uvicorn api.main:app --reload --host 0.0.0.0 --port 8000

pause

