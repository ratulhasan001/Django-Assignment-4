from django.shortcuts import redirect, render
from . import forms
from . import models
from .models import TaskModel
# Create your views here.

def add_task(request):
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task')
    else:
        task_form = forms.TaskForm()
    return render(request, 'add_task.html', {'form' : task_form})

def edit_task(request, id):
    post = models.TaskModel.objects.get(pk = id)
    task_form = forms.TaskForm(instance=post)
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST, instance=post)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task')
    return render(request, 'add_task.html', {'form' : task_form})

def delete_task(request, id):
    post = models.TaskModel.objects.get(pk = id)
    post.delete()
    return redirect('show_task')

def show_task(request):
    data = TaskModel.objects.all()
    return render(request, 'show_task.html', {"data": data})