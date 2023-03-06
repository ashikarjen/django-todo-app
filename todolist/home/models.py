from django.db import models

# Create your models here.

class Task(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDesc = models.TextField()
    taskUrl = models.TextField(default="#")

    def __str__(self):
        return self.taskTitle