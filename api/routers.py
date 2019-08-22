from . import viewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('movies',viewsets.MovieViewSet)
router.register('directors',viewsets.DirectorViewSet)
