@REM @echo off
@REM start cmd /k python manage.py runserver
@REM start cmd /k celery -A todoList worker --pool=solo -l INFO
@REM start cmd /k celery -A todoList beat -l INFO
@REM start cmd /k celery -A todoList flower

@echo off
:: Đặt DJANGO_SETTINGS_MODULE
set DJANGO_SETTINGS_MODULE=todoList.settings

:: Khởi động Django server
start cmd /k "python manage.py runserver"

:: Đợi 5 giây để Django server khởi động
timeout /t 5

:: Khởi động Celery worker
start cmd /k "celery -A todoList worker --pool=solo -l INFO"

:: Khởi động Celery beat
start cmd /k "celery -A todoList beat -l INFO"

:: Khởi động Flower (tùy chọn)
:: start cmd /k "celery -A todoList flower"

echo Các server đã được khởi động!
echo Django: http://localhost:8000
echo Flower: http://localhost:5555 (nếu được kích hoạt)
pause