from rest_framework import serializers
from movie import models
from users.models import CustomUser


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(read_only=True)
    # user = serializers.HyperlinkedRelatedField(view_name="users", read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = models.Movie
        fields = ('id','title','imdb','isPublish','director','user')

class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Director
        fields = ('name',)



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','email', 'username', )