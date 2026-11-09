@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  py -3.11 -m venv .venv || exit /b 1
)
".venv\Scripts\python.exe" -m pip install -r requirements.txt || exit /b 1
".venv\Scripts\python.exe" simulate.py || exit /b 1
if "%~1"=="" goto done
if not exist report.tex (
  echo Place report.tex and university.png in this folder first.
  exit /b 1
)
pdflatex --enable-installer -halt-on-error -interaction=nonstopmode -jobname="%~1_EN3330_A03" report.tex || exit /b 1
pdflatex --enable-installer -halt-on-error -interaction=nonstopmode -jobname="%~1_EN3330_A03" report.tex || exit /b 1
:done
echo Build completed.
