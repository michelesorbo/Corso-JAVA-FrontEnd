from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ToDoCategory(models.Model):
    titolo = models.CharField(max_length=200)

    def __str__(self):
        return self.titolo

class ToDo(models.Model):
    autore = models.ForeignKey(User, on_delete = models.CASCADE)
    categoria = models.ForeignKey(ToDoCategory, on_delete=models.CASCADE, default=None)
    img = models.ImageField(default=None, upload_to='img')
    titolo = models.CharField('Titolo del ToDo',max_length = 200,default=None)
    task = models.TextField('Descrizione del Task')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titolo
