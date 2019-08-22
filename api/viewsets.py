from movie import models
from . import serializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,AllowAny,IsAdminUser


from django_filters import rest_framework as filt #1
class MovieFilter(filt.FilterSet): #2

    class Meta:
        model = models.Movie
        fields = {
            'title': ['icontains'], #3
            'imdb': ['gte'], #4
        }


class MovieViewSet(viewsets.ModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    filterset_class = MovieFilter #5

    @action(methods=['get'], detail=False)  
    def published(self,request):
        published = self.get_queryset().filter(isPublish=True)
        serializer = self.get_serializer(published, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def newest(self,request):
        newest = self.get_queryset().order_by('pk').last()
        serializer = self.get_serializer(newest)
        return Response(serializer.data)

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = models.Director.objects.all()
    serializer_class = serializers.DirectorSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
