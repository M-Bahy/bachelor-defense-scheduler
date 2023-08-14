@echo off

REM Start Django server minimized
start /min cmd /c "cd django && py manage.py runserver"

REM Start React server minimized
start /min cmd /c "cd react && npm start"