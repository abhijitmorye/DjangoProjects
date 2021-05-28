from typing import List
from django.contrib import admin
from django.urls import path
from myblogapi.views import ListView, UpdateDeleteView

urlpatterns = [
    path('', ListView.as_view(), name='lisview'),
    path('<int:pk>', UpdateDeleteView.as_view(), name='updatedeleteview'),
]
