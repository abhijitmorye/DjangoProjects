from django.contrib import admin
from django.urls import path, include
from ToDoApp import views

app_name = 'ToDoApp'
urlpatterns = [
    # path('', views.index, name='index'),
    # path('done/<int:task_id>', views.done, name='done'),
    # path('update/<int:task_id>', views.update, name='update'),
    path('cbvindex/', views.TaskListView.as_view(), name='cbvindex'),
    path('cbvdetail/<int:pk>/', views.TaskDetailView.as_view(), name='cbvdetails'),
    path('cbvupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>', views.TaskDeleteView.as_view(), name='cbvdelete'),
]