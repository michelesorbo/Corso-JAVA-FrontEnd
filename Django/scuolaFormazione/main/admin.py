from django.contrib import admin
from .models import CategoriaCorsi, Corsi, Alunni
# Register your models here.
admin.site.register(CategoriaCorsi)

#Serve per vedere il campo img nell'area admin
class CorsiAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']

admin.site.register(Corsi, CorsiAdmin)

class AlunniAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']

admin.site.register(Alunni, AlunniAdmin)
