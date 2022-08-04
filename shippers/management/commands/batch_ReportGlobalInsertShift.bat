
@echo off
@ CD /D "C:\Users\CLOPES4\.virtualenvs\visteon-zAvzH-Ye\Scripts\"
@Call "activate.bat"
@ CD /D "C:\visteon\"
@python manage.py EmailProdReportShift
exit /b