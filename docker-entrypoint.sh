#!/bin/bash
set -e  # Dừng script nếu có lỗi

# Thực hiện migrate
python manage.py migrate

# Khởi động ứng dụng chính
exec "$@"