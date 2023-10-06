from django.urls import path

from . import views

app_name = 'nasaAPI'
urlpatterns = [
    path('', views.requestNasaAPI, name='requestNasaAPI'),
]