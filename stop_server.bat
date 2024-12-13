@echo off
echo Đang dừng các server...

:: Dừng các process Python (Django và Celery)
taskkill /F /IM python.exe
taskkill /F /IM celery.exe

echo Đã dừng tất cả các server!
pause