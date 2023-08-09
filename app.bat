@echo off

rem Ruta donde se encuentra el archivo requirements.txt
set REQUIREMENTS_PATH=.\requirements.txt

rem Ruta donde se encuentra el archivo app.py
set APP_PATH=.\app.py

rem Nombre del entorno virtual
set VENV_NAME=venv

rem Verificar si el entorno virtual ya existe
if not exist %VENV_NAME% (
    echo Creando entorno virtual...
    python -m venv %VENV_NAME%
)

rem Activar el entorno virtual
call %VENV_NAME%\Scripts\activate

rem Instalar los paquetes desde requirements.txt
echo Instalando paquetes desde requirements.txt...
pip install -r %REQUIREMENTS_PATH%

rem Ejecutar app.py
echo Ejecutando app.py...
python %APP_PATH%

rem Desactivar el entorno virtual
deactivate
