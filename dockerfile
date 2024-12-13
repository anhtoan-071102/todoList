FROM python:3.11

# Đặt biến môi trường
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Tạo thư mục làm việc
WORKDIR /app

# Cài đặt pipenv
RUN pip install pipenv

# Copy Pipfile và Pipfile.lock
COPY Pipfile Pipfile.lock ./

# Cài đặt dependencies
RUN pipenv install --system --deploy

# Copy project
COPY . .

# Expose port
EXPOSE 8000

# Entrypoint script
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]