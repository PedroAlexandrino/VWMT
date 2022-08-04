
@echo off
@ CD /D "D:"
@ CD /D "D:\wwwvtrak\vproject\"
@python manage.py renew_production_linesSchedule
exit /b