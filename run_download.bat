@echo off
cd /d "%~dp0"
set PY=
where python >nul 2>&1 && set PY=python
if "%PY%"=="" if exist "%USERPROFILE%\miniconda3\python.exe" set PY="%USERPROFILE%\miniconda3\python.exe"
if "%PY%"=="" where py >nul 2>&1 && set PY=py
if "%PY%"=="" (echo NO_PYTHON> download.log & echo NO_PYTHON & pause & exit /b)
echo Lancement du telechargement Wayback... (voir download.log)
%PY% download_wayback.py 1^> download.log 2^>^&1
echo EXIT=%errorlevel%>> download.log
echo TERMINE. Vous pouvez fermer cette fenetre.
