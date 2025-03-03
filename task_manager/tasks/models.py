from django.db import models

class Task(models.Model):
    title = models.CharField()
    description = models.TextField()
    completed = models.BooleanField(default='False')
