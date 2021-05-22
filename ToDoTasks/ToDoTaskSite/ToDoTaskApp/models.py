from django.db import models

# Create your models here.

class Tasks(models.Model):

    def __str__(self):

        return self.taskTitle
    
    taskTitle = models.CharField(max_length=100)

    taskDesc = models.CharField(max_length=500)

    taskAuthor = models.CharField(max_length=100)

