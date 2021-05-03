from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.HomePageView, name='home'),

    path('new-scheduling/', views.NewScheduling, name='new_scheduling')
]
