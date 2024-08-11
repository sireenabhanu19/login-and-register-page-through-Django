from typing import Any
from django.db import models
 
class tweet(models.Model):
    uname=models.CharField(max_length=30)
    date=models.DateTimeField(auto_now_add=True)
    post=models.CharField(max_length=30)
    def __init__(self):
        return self.uname
 
