"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.routers import router
from rest_framework.authtoken import views
from django.contrib.auth.views import LoginView,LogoutView  # <-- LoginView ve LogoutView eklendi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('token/', views.obtain_auth_token, name='token'),
    path('login/', LoginView.as_view(), name="login"),  # LoginView urlimize eklendi
    path('logout/', LogoutView.as_view(), name='logout'), # LogoutView urlimize eklendi
]
