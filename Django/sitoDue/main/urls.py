from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todos/', views.todos, name='todos'),
    path('todo/<int:todo_id>', views.todo, name='todo'),
]

