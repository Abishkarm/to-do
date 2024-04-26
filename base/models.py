from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    status=models.TextField()
    description=models.CharField(max_length=200)