from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'TravelGoApp'

urlpatterns = [
    path('', views.index, name="index"),
]
