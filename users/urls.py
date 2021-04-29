from django.urls import path, include
from django.contrib.auth import views as auth_view


urlpatterns = [
    # user management (allauth)
    path('', include('allauth.urls')),
]
