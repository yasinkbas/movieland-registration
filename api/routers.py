from . import viewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('movies',viewsets.MovieViewSet)
# router.register('directors',viewsets.DirectorViewSet)
router.register('users',viewsets.UserViewSet,base_name='user')
# router.register('current_user',viewsets.CurrentUser,base_name='current_user')
