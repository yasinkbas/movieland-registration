from rest_framework import serializers
from movie import models


class MovieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Movie
        fields = ('title','imdb','isPublish','director')

class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Director
        fields = ('name',)
