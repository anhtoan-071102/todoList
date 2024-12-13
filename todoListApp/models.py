from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    class status_choise(models.TextChoices):
        PENDING = 'PENDING', 'chưa thực hiện'
        IN_PROGRESS = 'IN_PROGRESS', 'đang tiến hành'
        COMPLETED = 'COMPLETED', 'đã hoàn thành'
        OVERDUE = 'OVERDUE', 'quá hạn'
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    tittle = models.TextField(200)
    describe = models.TextField(1000)
    status = models.CharField(max_length=25, choices=status_choise.choices, default=status_choise.PENDING)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['start_time']
    
    # kiểm tra thời gian trước khi lưu (bắt đầu < hiện tại < kết thúc)
    def clean(self):
    # Chỉ validate khi tạo mới task
        if not self.pk:  # Nếu là task mới
            if self.start_time and self.start_time < timezone.now():
                raise ValidationError('Thời gian bắt đầu không thể nhỏ hơn thời gian hiện tại')
        
        if self.end_time and self.start_time and self.end_time < self.start_time:
            raise ValidationError('Thời gian kết thúc không thể nhỏ hơn thời gian bắt đầu')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def check_and_create_notifyction(self):
        current_time = timezone.now()
        time_before_start = self.start_time - timezone.timedelta(minutes=5)
        time_before_end = self.end_time - timezone.timedelta(minutes=10)
        
        # Chỉ tạo thông báo cho task chưa hoàn thành
        if self.status == self.status_choise.COMPLETED:
            return
            
        # Kiểm tra thông báo bắt đầu
        if (time_before_start <= current_time <= self.start_time):
            existing_notify = Notify.objects.filter(
                task=self,
                notify_type='START_SOON',
                create_at__gte=time_before_start
            ).exists()
            
            if not existing_notify:
                Notify.objects.create(
                    task=self,
                    notify_type='START_SOON',
                    content=f'Task {self.tittle} sẽ bắt đầu trong 5 phút nữa'
                )
        
        # Kiểm tra thông báo kết thúc
        if (time_before_end <= current_time <= self.end_time):
            existing_notify = Notify.objects.filter(
                task=self,
                notify_type='END_SOON',
                create_at__gte=time_before_end
            ).exists()
            
            if not existing_notify:
                Notify.objects.create(
                    task=self,
                    notify_type='END_SOON',
                    content=f'Task {self.tittle} sẽ kết thúc trong 10 phút nữa'
                )
        
    def check_and_modify_Task_status(self):
        current_time = timezone.now()
        
        # Nếu task đang ở trạng thái COMPLETED, không thay đổi
        if self.status == self.status_choise.COMPLETED:
            return
            
        # Kiểm tra quá hạn
        if current_time > self.end_time:
            self.status = self.status_choise.OVERDUE
            return
            
        # Kiểm tra đang thực hiện
        if self.start_time <= current_time <= self.end_time:
            if self.status == self.status_choise.PENDING:
                self.status = self.status_choise.IN_PROGRESS
        
    def __str__(self) -> str:
        return self.tittle

class Notify(models.Model):
    NOTIFY_TYPES = (
        ('START_SOON', 'Task sắp đến giờ bắt đầu'),
        ('END_SOON', 'Task sắp kết thúc'),
    )
    
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='notifys')
    content = models.TextField()
    notify_type = models.CharField(max_length=20, choices=NOTIFY_TYPES)
    is_readed = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['create_at']
        
    @property
    def user(self):
        return self.task.user