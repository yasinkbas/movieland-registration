from django.urls import include, path
from . import views

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('', views.UserListView.as_view()),
]

