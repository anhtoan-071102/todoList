# Todo List Application

A Django-based Todo List application with REST API, real-time notifications, and task management features.

## Features

- User authentication using JWT
- CRUD operations for tasks
- Automatic task status updates
- Real-time notifications for task deadlines
- API rate limiting
- Celery background tasks
- Docker deployment support

## Technologies Used

- Django 5.1.3
- Django REST Framework
- Celery
- Redis
- JWT Authentication
- Docker
- Swagger/OpenAPI

## Getting Started

### Prerequisites

- Python 3.11+
- Redis
- Docker & Docker Compose (optional)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/todoList.git
cd todoList
```
2. Install dependencies using pipenv:
```bash
pipenv install
```
3. Setup environment variables:
```bash
cp .env.example .env
```
4. Run migrations:
```bash
python manage.py migrate
```
## Running the Application
### Using Docker:
```bash
docker-compose up --build
```

### Without Docker:
1. Start Redis server:
[redis](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/)
2. Run Django server:
```bash
python manage.py runserver
```
3. Run Celery worker:
```bash
celery -A todoList worker --pool=solo -l INFO
```
4. Run Celery beat
```bash
celery -A todoList beat -l INFO
```
## API Documentation
### API documentation is available at:
- Swagger UI: /api/swagger/
- ReDoc: /api/redoc/

