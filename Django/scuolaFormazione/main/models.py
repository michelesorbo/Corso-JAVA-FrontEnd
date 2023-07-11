from django.db import models
from django.utils.html import mark_safe

# Create your models here.
class CategoriaCorsi(models.Model):
    titolo = models.CharField(max_length=150)
    descrizione = models.TextField()

    def __str__(self):
        return self.titolo
    
    class Meta:
        verbose_name_plural = "Categorie"
    
class Corsi(models.Model):
    titolo = models.CharField(max_length=200)
    img = models.ImageField(upload_to='img/corsi', default=None)
    descrizione = models.TextField()
    durata_ore = models.CharField(max_length=4)
    data_inizio = models.DateTimeField()
    prezzo = models.FloatField(max_length=6)
    categoria = models.ForeignKey(CategoriaCorsi, on_delete=models.CASCADE)

    def __str__(self):
        return self.titolo
    
    #Creo il metodo per visualizzare l'img in Admin
    def img_preview(self):
        return mark_safe(f'<img src="{self.img.url}" width="300">')
    
    class Meta:
        verbose_name_plural = "Corsi"


class Alunni(models.Model):
    nome = models.CharField(max_length=150)
    cognome = models.CharField(max_length=150)
    email = models.EmailField()
    tel = models.CharField(max_length=15)
    corso = models.ForeignKey(Corsi, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} {self.cognome}"
    
    class Meta:
        verbose_name_plural = "Alunni"