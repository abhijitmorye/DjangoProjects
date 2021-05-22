from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task 
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ToDoForm


# Create your views here.

class TaskListView(ListView):

    model = Task
    template_name = 'ToDoApp/index.html'
    context_object_name = 'task_list'

class TaskDetailView(DetailView):

    model = Task
    template_name = 'ToDoApp/detail.html'
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'ToDoApp/update.html'
    context_object_name = 'task'
    fields = [
        'name', 'priority', 'date'
    ]

    # success_url = '/cbvdetail/{}'.format(object.id)

    
    def get_success_url(self):

        return reverse_lazy('cbvdetail', kwargs={'pk': self.object.id})


class TaskDeleteView(DeleteView):

    model = Task
    template_name = 'ToDoApp/delete.html'
    success_url = '/cbvindex/'


# def index(request):

#     if request.method == "POST":

#         name =  request.POST.get('name',)
#         priority = request.POST.get('priority',)
#         date = request.POST.get('date','')

#         task = Task(name=name, priority=priority, date=date)
#         task.save()
#         return redirect('/')

#     task_list = Task.objects.all()

#     context = {
#         "task_list" : task_list
#     }

#     return render(request, 'ToDoApp/index.html', context)


# def done(request, task_id):

#     task = Task.objects.get(id=task_id)
#     task.delete()

#     return redirect('/')

# def update(request, task_id):

#     task = Task.objects.get(id=task_id)
#     name = task.name
#     priority = task.priority

#     if request.method == "POST":

        

#         if request.POST.get('name',) == '':
#             task.name = name
#         else:
#             task.name =  request.POST.get('name',)
        
#         if request.POST.get('priority',) == '':
#             task.priority = priority
#         else:
#             task.priority = request.POST.get('priority',)

#         task.save()
        
#         return redirect('/')

#     context = {
#         'task': task
#     }
    

#     return render(request, 'ToDoApp/update.html', context)

        
        


