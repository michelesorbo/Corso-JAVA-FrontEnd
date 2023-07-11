from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('todos/', views.todos, name='todos'),
    path('todo/<int:todo_id>', views.todo, name='todo'),
    path('creaTodo/', views.createToDo, name='crea_todo'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

