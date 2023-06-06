from email.policy import default
from tkinter import CASCADE
import uuid
from xmlrpc.client import TRANSPORT_ERROR
from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    first_Name = models.CharField(max_length=120)
    last_Name = models.CharField(max_length=120)
    password = models.CharField(max_length=200)
    number = models.CharField(max_length=15, null=False)


class Task(models.Model):
    STATUS_CHOICES = (
        ('COMPLETED', 'completed'),
        ('IN PROGRESS', 'In progress')
    )
    title = models.CharField(max_length=150)
    notes = models.TextField(max_length=200)
    date = models.DateField(default=None)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='IN PROGRESS', null=True)
 
