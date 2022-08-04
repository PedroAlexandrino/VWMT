
@echo off
@ CD /D "C:\Users\aroque1\env\Scripts\"
@Call "activate.bat"
@ CD /D "C:\visteon\"
@python manage.py updateSchedule
exit /b