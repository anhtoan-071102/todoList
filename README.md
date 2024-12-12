# ToDoList Backend

## Overview
The **ToDoList Backend** is a task management application developed using Python and Django. It provides APIs for managing tasks, with features like user authentication using JWT, task CRUD operations, and notifications for tasks nearing their start or end time.

---

## Features

### 1. **Authentication**
- User registration and login using **JSON Web Tokens (JWT)**.
- Secure access to APIs with token-based authentication.

### 2. **Task Management**
- Create, Read, Update, and Delete tasks.
- Permissions to ensure only the task owner can modify or delete their tasks.

### 3. **Notifications**
- Automatic notifications for tasks that are about to start or end using **Celery** for asynchronous task handling.

---

## Technologies Used

### **Backend Framework**
- Django
- Django REST Framework (DRF)

### **Authentication**
- Simple JWT (JSON Web Tokens)

### **Asynchronous Task Queue**
- Celery (with Redis as the message broker)

### **Cross-Origin Resource Sharing (CORS)**
- django-cors-headers

---

## Installed Applications

The project uses the following Django applications and third-party libraries:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todoListApp',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
]

Prerequisites
Python (>= 3.9)
Redis (for Celery)
git clone https://github.com/anhtoan-071102/todoList.git
cd todoList

python -m venv env
source env/bin/activate
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=*
DATABASE_URL=your_database_connection_string
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

celery -A todoList worker --loglevel=info
API Endpoints
Authentication
Endpoint	Method	Description
/api/auth/register	POST	User registration
/api/auth/login	POST	User login (JWT)
Task Management
Endpoint	Method	Description
/api/tasks/	GET	List all tasks (current user)
/api/tasks/	POST	Create a new task
/api/tasks/<id>/	GET	Retrieve a specific task
/api/tasks/<id>/	PUT	Update an existing task
/api/tasks/<id>/	DELETE	Delete a task

Key Functionalities
Authentication with JWT
The project uses rest_framework_simplejwt to secure endpoints.
Include the token in the Authorization header as:
makefile
Sao chép mã
Authorization: Bearer <your_token>

Notifications with Celery
Celery tasks are triggered to notify users when:
A task is about to start.
A task is nearing its end time.
