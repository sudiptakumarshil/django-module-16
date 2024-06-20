from django.shortcuts import render,redirect
from task.forms import TaskForm
from django.contrib import messages
from task.models import Task

# Create your views here.
def add_task(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            messages.success(request, 'Task saved successfully!')
            return redirect('task.add')
    
    form = TaskForm
    return render(request,'add_task.html',{'form':form})


def edit_task(request,id):
    task = Task.objects.get(pk=id)
    task_form = TaskForm(instance=task)
    if request.method == 'POST':
        task_form = TaskForm(request.POST,instance=task)
        if task_form.is_valid():
            task_form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('task.show')
    
    return render(request,'add_task.html',{'form':task_form})


def delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    messages.success(request, 'Task deleted successfully!')
    return redirect('task.show')


def show_task(request):
    data = Task.objects.all()
    return render(request,'show_task.html',{'data':data})

