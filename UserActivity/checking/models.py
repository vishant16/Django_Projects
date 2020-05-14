from django.db import models
from datetime import datetime
# Create your models here.

class SE(models.Model):
    start_time= models.CharField(max_length=120,default='start_time',help_text="Feb 1 2020  1:33PM")
    end_time= models.CharField(max_length=120,default='end_time',help_text="Feb 1 2020  1:33PM")
    start_time1= models.CharField("start time",max_length=120,default='start time',help_text="Feb 1 2020  1:33PM")
    end_time1= models.CharField("end time",max_length=120,default='end time',help_text="Feb 1 2020  1:33PM")
    start_time2= models.CharField("start time",max_length=120,default='start time',help_text="Feb 1 2020  1:33PM")
    end_time2= models.CharField("end time",max_length=120,default='end time',help_text="Feb 1 2020  1:33PM")

    def __str__(self):
        return f"{self.start_time} and {self.end_time}"


class UserDetails(models.Model):
    real_name= models.CharField(max_length=10,default="vishant")
    tz= models.CharField(max_length=10,default="India")
    activity_periods= models.ForeignKey(SE,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.real_name} and {self.activity_periods.start_time} and {self.activity_periods.end_time}"
