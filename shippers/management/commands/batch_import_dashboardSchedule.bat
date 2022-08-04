
@echo off
@ CD /D "D:"
@ CD /D "D:\wwwvtrak\vproject\"
@python manage.py import_dashboardSchedule
exit /b