@echo off

rem Set the default Python executable
set PYTHON=python3

rem Check if python3 is not found, then use python
where %PYTHON% >nul 2>nul || set PYTHON=python

rem Check if Python executable is still not found
where %PYTHON% >nul 2>nul || (
  echo "PYTHON=%PYTHON% not found in PATH"
  exit /b 1
)

rem Get Python version
for /f "tokens=1-3" %%a in ('%PYTHON% -c "import sys; print(sys.version_info[0], sys.version_info[1], sys.version_info[2])"') do set PYTHON_VERSION=%%a.%%b.%%c
rem Check if Python version is greater than or equal to 3.0
set PYTHON_VERSION_MIN=3.01.0
if %PYTHON_VERSION% lss %PYTHON_VERSION_MIN% (
  echo "detected Python %PYTHON_VERSION% need Python >= %PYTHON_VERSION_MIN%"
  exit /b 1
)

echo "Python version is %PYTHON_VERSION%"

rem Your make targets go here

rem Example: 
:build
  echo "Building..."

:clean
  echo "Cleaning..."

rem End of make targets

exit /b 0
