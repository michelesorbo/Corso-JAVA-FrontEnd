from django.contrib import admin
from .models import ToDo, ToDoCategory
# Register your models here.
admin.site.register(ToDo)
admin.site.register(ToDoCategory)