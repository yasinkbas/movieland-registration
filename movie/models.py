from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Movie(models.Model):
    title = models.CharField(max_length=128)
    imdb = models.FloatField(validators=[MaxValueValidator(10.0),MinValueValidator(0.0)])
    isPublish = models.BooleanField(default=True)
    director = models.ForeignKey('movie.Director',on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return self.title

class Director(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
