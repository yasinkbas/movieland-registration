from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    email = models.EmailField(_('email address'), unique=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username