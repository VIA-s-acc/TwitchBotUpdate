@echo off
rem Путь к вашему виртуальному окружению
set VENV_PATH=.venv

rem Активация виртуального окружения
call %VENV_PATH%\Scripts\activate

rem Запуск вашего Python скрипта
python run.py