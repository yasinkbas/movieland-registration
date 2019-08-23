from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/',include('rest_auth.registration.urls')),
]

