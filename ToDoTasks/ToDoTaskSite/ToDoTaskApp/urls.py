from django.urls import path
from ToDoTaskApp import views


app_name = 'ToDoTaskApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('addtask/', views.addTask, name='addTask'),
    path('viewTasks/', views.viewTasks, name='viewTasks'),
    path('viewTasks/<int:task_id>/', views.viewSingleTask, name='viewSingleTask'),
    path('deletetasks/<int:task_id>/', views.deleteSingleTasks, name='deleteSingleTasks'),
    path('updatetask/<int:task_id>/', views.updateTask, name='updateTask'),
]
