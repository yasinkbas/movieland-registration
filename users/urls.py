from django.urls import include, path
from . import views

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('registration/',include('rest_auth.registration.urls')),
    path('', views.UserListView.as_view()),
]

