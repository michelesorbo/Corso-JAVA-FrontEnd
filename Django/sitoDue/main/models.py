from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDo(models.Model):
    autore = models.ForeignKey(User, on_delete = models.CASCADE)
    titolo = models.CharField(max_length = 200),
    task = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titolo
