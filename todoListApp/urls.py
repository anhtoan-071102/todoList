from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import TaskListCreateAPIView, TaskDetailAPIView, RegisterView, RegisterPageView, LoginPageView, TaskPageView

urlpatterns = [
    #Template URLs
    path('register-page/', RegisterPageView.as_view(), name='register_page'),
    path('login-page/', LoginPageView.as_view(), name='login_page'),
    path('tasks-page/', TaskPageView.as_view(), name="tasks_page"),
    
    #API urls
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tasks/', TaskListCreateAPIView.as_view(), name='task_list_create'),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task_list_edit')
]