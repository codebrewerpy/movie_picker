@echo off

set PYTHON=python

where %PYTHON% >nul 2>nul || set PYTHON=python

where %PYTHON% >nul 2>nul || (
  echo "PYTHON=%PYTHON% not found in PATH"
  exit /b 1
)

rem Get Python version
for /f "tokens=1-3" %%a in ('%PYTHON% -c "import sys; print(sys.version_info[0], sys.version_info[1], sys.version_info[2])"') do set PYTHON_VERSION=%%a.%%b.%%c

rem Check if Python version is greater than or equal to 3.0
set PYTHON_VERSION_MIN=3.08.0
if %PYTHON_VERSION% lss %PYTHON_VERSION_MIN% (
  echo "detected Python %PYTHON_VERSION% need Python >= %PYTHON_VERSION_MIN%"
  exit /b 1
)

if "%1"=="" goto :eof
goto %1

:build
  echo "Building..."
  %PYTHON% --version

:clean
  echo "Cleaning..."

:eof
    exit /b 0
