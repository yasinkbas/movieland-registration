from django.contrib import admin
from . import models

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'imdb','isPublish','director_name','user']
    list_display_links = ('id', 'title')

admin.site.register(models.Movie,MovieAdmin)
# admin.site.register(models.Director)
