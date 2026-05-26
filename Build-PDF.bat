@echo off
REM ===================================================================
REM  Build the BAPS SAP Style Guide PDF and open it.
REM
REM  Double-click this file from File Explorer, or pin it to your
REM  taskbar / Start menu, or right-click -> Send to -> Desktop to
REM  create a shortcut icon.
REM
REM  What it does:
REM    1. Switches to the project root (this file's location)
REM    2. Runs build-pdf.py (mkdocs build + Chromium print-to-PDF)
REM    3. Opens the resulting PDF in your default viewer
REM
REM  Output: site\pdf\baps-style-guide.pdf
REM ===================================================================

setlocal
cd /d "%~dp0"

echo.
echo === Building BAPS SAP Style Guide PDF ===
echo.

REM Stop the local dev server if it's running, so it doesn't lock site\
for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":8000.*LISTENING"') do (
    taskkill /F /PID %%a >nul 2>&1
)

REM Close any PDF viewer holding the previous output open
taskkill /F /IM AcroRd32.exe >nul 2>&1
taskkill /F /IM Acrobat.exe  >nul 2>&1
taskkill /F /IM FoxitPDFReader.exe >nul 2>&1
taskkill /F /IM SumatraPDF.exe >nul 2>&1

python build-pdf.py
if errorlevel 1 (
    echo.
    echo *** BUILD FAILED ***
    echo.
    echo Possible causes:
    echo   - Python packages missing  ^=^>  pip install -r requirements.txt
    echo   - Chromium not installed   ^=^>  python -m playwright install chromium
    echo   - PDF still locked by a viewer  ^=^>  close it and re-run
    echo.
    pause
    exit /b 1
)

echo.
echo Opening site\pdf\baps-style-guide.pdf ...
start "" "site\pdf\baps-style-guide.pdf"

REM Give the viewer a moment to start before closing the window
timeout /t 2 /nobreak >nul
endlocal
