from django.contrib import admin
from django.urls import path, include
from movieapi import urls
from .views import MovieAPIView, MovieDetailView

urlpatterns = [
    path('', MovieAPIView.as_view(), name='movieapiview'),
    path('<int:pk>', MovieDetailView.as_view(), name='moviedetail'),
]
