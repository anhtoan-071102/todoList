from .models import Task, Notify
from django.contrib.auth.models import User
from rest_framework import serializers
from django.utils import timezone

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'user', 'tittle', 'describe', 'status', 'start_time', 'end_time', 'created_at', 'updated_at']
        
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    # check thời gian khi nhận từ user trước khi chuyển sang thành object (start < current < end)
    def validate(self, data):
        # Validate thời gian bắt đầu
        if data.get('start_time') and data['start_time'] < timezone.now():
            raise serializers.ValidationError({
                'start_time': 'Thời gian bắt đầu không thể nhỏ hơn thời gian hiện tại'
            })

        # Validate thời gian kết thúc
        if data.get('start_time') and data.get('end_time'):
            if data['end_time'] < data['start_time']:
                raise serializers.ValidationError({
                    'end_time': 'Thời gian kết thúc không thể nhỏ hơn thời gian bắt đầu'
                })

        return data
    
    def update(self, instance, validated_data):
        if instance.status == instance.status_choise.OVERDUE:
            raise serializers.ValidationError("Cannot update a task with status 'OVERDUE'") 
        
        validated_data.pop('status', None)
        return super().update(instance, validated_data)
    
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user
    
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notify
        fields = ['id', 'task','content', 'notify_type', 'is_readed', 'create_at']