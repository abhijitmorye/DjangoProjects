from django.contrib import admin
from django.urls import path
from MyBlogApp import views


app_name = 'MyBlogApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register' ),
    path('success/', views.success, name='success'),
    path('loginFresh/', views.login_fresh, name='login_fresh'),
    path('login/', views.login, name='login'),
    path('warning/', views.warning, name='warning'),
    path('loginsuc/', views.loginSuccess, name='login_success'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('updateprofile/', views.update, name='updateprofile'),
]