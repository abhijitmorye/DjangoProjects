from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tasks
from django.contrib import messages

# Create your views here.

def index(request):

    return render(request, 'ToDoTaskApp/index.html')



def addTask(request):

    if request.method == 'POST':
        taskTitle = request.POST.get('taskTitle',)
        taskDesc = request.POST.get('taskDesc',)
        taskAuthor = request.POST.get('taskAuthor',)

        task = Tasks(taskTitle=taskTitle, taskDesc=taskDesc, taskAuthor=taskAuthor)
        task.save()
        # messages.success(request, 'task addedd successfully!')

        return redirect('/viewTasks/')

    return render(request, 'ToDoTaskApp/addTask.html')




def viewTasks(request):
    tasks = Tasks.objects.all()

    context = {

        "tasks" : tasks
    }

    return render(request, 'ToDoTaskApp/viewTasks.html', context)


def viewSingleTask(request, task_id):

    task = Tasks.objects.get(id=task_id)

    context = {
        'task': task
    }

    return render(request, 'ToDoTaskApp/viewSingleTask.html', context)

def deleteSingleTasks(request, task_id):

    if request.method == 'POST':

        task = Tasks.objects.get(id=task_id)
        result = task.delete()
        if result[0] == 1:
            return redirect('/viewTasks/')

    context = {
        'id' : task_id
    }
        
    return render(request, 'ToDoTaskApp/deleteSingleTasks.html', context)


def updateTask(request, task_id):

    task = Tasks.objects.get(id=task_id)

    title = task.taskTitle
    desc = task.taskDesc
    author = task.taskAuthor

    if request.method == 'POST':

        if request.POST.get('taskTitle',) == '':
            task.taskTitle = title
        else:
            task.taskTitle = request.POST.get('taskTitle',)

        if request.POST.get('taskDesc',) == '':
            task.taskDesc = desc
        else:
            task.taskDesc = request.POST.get('taskDesc',)

        if request.POST.get('taskAuthor',) == '':
            task.taskAuthor = author
        else:
            task.taskAuthor = request.POST.get('taskAuthor',)
        
        task.save()

        # messages.success(request, 'task updated successfully!')

        return redirect('/viewTasks/{}/'.format(task.id))

    context = {
        'task' : task
    }

    return render(request, 'ToDoTaskApp/updateTask.html', context)




