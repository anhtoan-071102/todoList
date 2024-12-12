from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import UserRateThrottle
from django.utils import timezone

from .models import Task
from .serializers import TaskSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly
from .form import RegisterForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

class RegisterPageView(TemplateView):
    template_name = 'todoListApp/register.html'
    permission_classes = []

class LoginPageView(TemplateView):
    template_name = "todoListApp/login.html"
    permission_classes = []

class TaskPageView(TemplateView):
    template_name = "todoListApp/tasks.html"
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().get(request, *args, **kwargs)

# Create your views here.
class RegisterView(APIView):
    permission_classes = []  # Cho phép truy cập không cần xác thực
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskListCreateAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    
    def get(self, request):
        try:
            tasks = Task.objects.filter(user=request.user).select_related('user')
            serializer = TaskSerializer(tasks, many=True)
            
            if 'application/json' in request.headers.get('Accept', ''):
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return render(request, 'todoListApp/tasks.html')
                
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request):
        serializer = TaskSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class TaskDetailAPIView(APIView):
    """
    View cho phép:
    - Xem chi tiết một task (GET)
    - Cập nhật task (PUT hoặc PATCH)
    - Xóa task (DELETE)
    """
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    authentication_classes = [JWTAuthentication]
    throttle_classes = [UserRateThrottle]
    
    def get_object(self, pk):
        try:
            obj = Task.objects.get(pk=pk)
            self.check_object_permissions(self.request, obj)
            return obj
        except Task.DoesNotExist:
            return None

    def get(self, request, pk):
        task = self.get_object(pk)
        if not task:
            return Response(
                {"error": "Task not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
            
    def put(self, request, pk):
        task = self.get_object(pk)
        if not task:
            return Response(
                {"error": "Task not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = TaskSerializer(
            task, 
            data=request.data, 
            partial=True, 
            context={'request': request}
        )
        
        tasks = TaskSerializer()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk)
        if not task:
            return Response(
                {"error": "Task not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        task.delete()
        return Response(
            {"message": "Task deleted successfully"}, 
            status=status.HTTP_204_NO_CONTENT
        )

