from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.HomePageView, name='home'),
    path('month:<int:month>/', views.HomePageView, name='home'),

    path('new-scheduling/', views.NewScheduling, name='new_scheduling'),
    path('update-scheduling/<int:id>/', views.UpdateScheduling, name='update_scheduling'),
    path('delete-scheduling/<int:id>/', views.DeleteScheduling, name='delete_scheduling'),
]
