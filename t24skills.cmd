@echo off
rem t24skills -- Temenos-Skills command line (pipeline\t24skills.py). See: t24skills --help
setlocal
set "PY=python"
where py >nul 2>nul && set "PY=py -3"
%PY% "%~dp0pipeline\t24skills.py" %*
exit /b %ERRORLEVEL%
