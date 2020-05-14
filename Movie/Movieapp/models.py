from django.db import models

class Actor(models.Model):
    Actor = models.CharField(max_length=255)


    def __str__(self):
        return self.Actor

class Film(models.Model):
    Movie = models.CharField(max_length=255)
    Actor = models.ForeignKey(Actor,on_delete=models.CASCADE)

    def __str__(self):
        return self.Movie
