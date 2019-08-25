from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import CustomUser
from PIL import Image
from base.helper import get_file_path

class Movie(models.Model):
    title = models.CharField(max_length=128)
    imdb = models.FloatField(validators=[MaxValueValidator(10.0),MinValueValidator(0.0)])
    isPublish = models.BooleanField(default=True)
    image = models.ImageField(default='default.jpg', upload_to=get_file_path, blank=False)
    director_name = models.CharField(max_length=64)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        return super().save(force_insert=force_insert, force_update=force_update, using=using,
                            update_fields=update_fields)

# class Director(models.Model):
#     name = models.CharField(max_length=64)
#
#     def __str__(self):
#         return self.name

class CurrentUser(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)