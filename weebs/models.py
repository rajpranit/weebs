from enum import auto
from time import time
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=225)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(null=True)
  

    def __str__(self):
        return f"{self.title} | {self.author}"