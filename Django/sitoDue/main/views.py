from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDo
from .forms import ToDoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def todos(request):
    todos = ToDo.objects.all()
    return render(request,'main/todos.html', {"todos":todos})

def todo(request,todo_id):
    todo = ToDo.objects.get(pk=todo_id)
    return render(request, 'main/todo.html', {'todo':todo})

@login_required(login_url="/")
def createToDo(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.autore = request.user #Vado ad assegnare l'utente loggato come autore del ToDo
            todo.save()
            return redirect('todos') #Dopo aver inserito un todo vado su todos
    else:
        form = ToDoForm()
    
    return render(request, 'main/todoForms.html', {"form":form})