from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import CustomUser

class Movie(models.Model):
    title = models.CharField(max_length=128)
    imdb = models.FloatField(validators=[MaxValueValidator(10.0),MinValueValidator(0.0)])
    isPublish = models.BooleanField(default=True)
    director = models.ForeignKey('movie.Director',on_delete=models.SET_NULL,blank=True,null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Director(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
