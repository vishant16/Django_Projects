from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=100)

class Activity(models.Model):
    user = models.ForeignKey(User, related_name='activity_periods', on_delete=models.CASCADE)
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)

    class Meta:
        unique_together = ['user', 'start_time','end_time']

    def __str__(self):
        a=f"{self.user.id}"
        return a
