from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Task(models.Model):
    task_name = models.CharField(max_length=100)
    task_date = models.DateField()
    task_status = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
# Create your models here.
