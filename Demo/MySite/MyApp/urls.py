from django.contrib import admin
from django.urls import path
from MyApp import views

app_name = 'MyApp'
urlpatterns = [
    path('', views.index, name='index'),
    path("products/", views.products, name='products'),

    # to pass variable to url, write static paart then <type of varibale(int, string) : name of variable> 
    path("products/book/<int:book_id>", views.details, name='details'),
    path('add/', views.add_book, name="addBook"),
    path("update/<int:book_id>/", views.update, name="update"),
    path("delete/<int:book_id>/", views.delete, name="delete"),
]
