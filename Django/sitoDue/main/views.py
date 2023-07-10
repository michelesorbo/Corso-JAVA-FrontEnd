from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDo

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def todos(request):
    todos = ToDo.objects.all()
    return render(request,'main/todos.html', {"todos":todos})

def todo(request,todo_id):
    todo = ToDo.objects.get(pk=todo_id)
    return render(request, 'main/todo.html', {'todo':todo})