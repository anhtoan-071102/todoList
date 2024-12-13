from django.urls import path, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions
from .views import TaskListCreateAPIView, TaskDetailAPIView, RegisterView, RegisterPageView, LoginPageView, TaskPageView, NotifyAPIView, NotifyReadedAPIView

schema_view = get_schema_view(
   openapi.Info(
      title="Todo List API",
      default_version='v1',
      description="API documentation for Todo List application",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="anhtoan07112002@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

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
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task_list_edit'),
    path('notifications/', NotifyAPIView.as_view(), name='notification'),
    path('notifications/<int:notification_id>/readed/', NotifyReadedAPIView.as_view(), name='notification-is-readed'),
    
    # swagger
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]