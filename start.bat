@echo off
:loop
python main.py
IF %ERRORLEVEL% NEQ 0 GOTO end
goto loop
:end