from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt


from . import views

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('register/',include('rest_auth.registration.urls')),
    path('current/',views.CurrentUser.as_view(),name='current'),
]

