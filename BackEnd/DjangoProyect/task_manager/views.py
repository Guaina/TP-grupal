from django.shortcuts import render, redirect, get_object_or_404
from .models import TaskList
from .forms import TaskListForm

def create_task(request):
    if request.method == 'POST':
        form = TaskListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-list')  
    else:
        form = TaskListForm()
    return render(request, 'task_manager/task_form.html', {'form': form})

def update_task(request, pk):
    task = get_object_or_404(TaskList, pk=pk)
    if request.method == 'POST':
        form = TaskListForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-list')  
    else:
        form = TaskListForm(instance=task)
    return render(request, 'task_manager/task_form.html', {'form': form})
