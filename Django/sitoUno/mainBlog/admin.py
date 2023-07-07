from django.contrib import admin
#Importo la tabella da models
from .models import Post

# Register your models here.
admin.site.register(Post)