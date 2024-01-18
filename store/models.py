from django.db import models

# Create your models here.
from django.db import models
from django.utils.timezone import now
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    subject=models.TextField(max_length=500)
    message=models.TextField()
    date=models.DateField
    
    def __str__(self):
            return [self.name,self.email]
