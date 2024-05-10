from django.db import models

# Create your models here.

class TaskModel(models.Model):
    id = models.IntegerField(primary_key=True)
    taskTittle = models.CharField(max_length=30)
    task_description = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
