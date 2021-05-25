from django.contrib import admin
from django.urls import path, include
from TicketReservationApp import views

app_name  = 'TicketReservationApp'
urlpatterns = [
    path('', views.index, name='index'),

]