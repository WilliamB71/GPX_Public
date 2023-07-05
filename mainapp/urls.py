from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('create_gpx/', views.create_gpx, name='create_gpx'),
]