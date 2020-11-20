from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .forms import TaskForm

# Define the home view
def home(request):
  task = Task.objects.all()  
  task_form = TaskForm()
  form = TaskForm(request.POST)
  if form.is_valid():
    new_task = form.save(commit=False)
    new_task.save()
  return render(request, 'index.html', {'task': task, 'task_form': task_form })
  
class TaskDelete(DeleteView):
  model = Task
  success_url = '/'