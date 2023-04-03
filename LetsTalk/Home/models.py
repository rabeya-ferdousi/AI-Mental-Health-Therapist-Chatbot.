from datetime import datetime
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=50)
    Date_Of_Birth = models.DateField(null=True)
    user_ID = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Profile(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    about_info = models.TextField(max_length=10000000)

class Therapist_Review(models.Model):
    comment = models.CharField(max_length=500)
    comment_Time = models.DateTimeField(default=datetime.now, blank=True)
    commentator = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)

class ChatBot_Message_Thread(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)

class ChatBot_Message(models.Model):
    Client_Message = models.TextField(max_length=10000000, default=None)
    Therapist_Message = models.TextField(max_length=10000000)
    Message_Time = models.DateTimeField(default=datetime.now, blank=True)
    Thread_Id = models.ForeignKey(ChatBot_Message_Thread, on_delete=models.CASCADE, null=True, related_name='thread')

class Diary(models.Model):
    title = models.CharField(max_length=500)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    note = models.TextField(max_length=10000000, default=None)
    time = models.DateTimeField(default=datetime.now, blank=True)

class Blog(models.Model):
    title = models.CharField(max_length=500)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    blog = models.TextField(max_length=10000000, default=None)
    time = models.DateTimeField(default=datetime.now, blank=True)