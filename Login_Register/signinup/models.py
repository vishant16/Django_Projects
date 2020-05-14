from django.db import models

# Create your models here.

class signin(models.Model):
    username=models.CharField(unique=True,max_length=120)
    phonenumber=models.CharField(unique=True,max_length=16)
    password=models.CharField(unique=True,max_length=16)
    password1=models.CharField(unique=True,max_length=16)


    def __str__(self):
        return self.username
