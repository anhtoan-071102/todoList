import logging
from celery import shared_task
from django.utils import timezone
from .models import Task

logger = logging.getLogger(__name__)

@shared_task
def check_task_notifications():
    try:
        logger.info(f"Starting task check at {timezone.now()}")
        
        # Check active tasks for notifications
        active_tasks = Task.objects.exclude(status=Task.status_choise.COMPLETED)
        logger.info(f"Found {active_tasks.count()} active tasks")
        
        for task in active_tasks:
            try:
                logger.info(f"Checking notifications for task {task.id}: {task.tittle}")
                task.check_and_create_notifyction()
            except Exception as e:
                logger.error(f"Error checking notifications for task {task.id}: {str(e)}")
        
        # Check pending tasks for status updates
        pending_tasks = Task.objects.filter(
            status__in=[Task.status_choise.PENDING, Task.status_choise.IN_PROGRESS]
        )
        logger.info(f"Found {pending_tasks.count()} pending/in-progress tasks")
        
        for task in pending_tasks:
            try:
                old_status = task.status
                task.check_and_modify_Task_status()
                if old_status != task.status:
                    logger.info(f"Task {task.id} status changed from {old_status} to {task.status}")
                    task.save()
            except Exception as e:
                logger.error(f"Error updating status for task {task.id}: {str(e)}")
                
        logger.info("Task check completed successfully")
        
    except Exception as e:
        logger.error(f"Error in check_task_notifications: {str(e)}")
        raise