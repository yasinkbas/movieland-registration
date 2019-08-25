from rest_framework import serializers
from movie import models
from users.models import CustomUser

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(read_only=True)
    # user = serializers.HyperlinkedRelatedField(view_name="users", read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = models.Movie
        fields = ('id','title','imdb','image','isPublish','director_name','user')


# class DirectorSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = models.Director
#         fields = ('name','image','summary')



class UserSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = CustomUser
        fields = ('id','email', 'username','owner')
