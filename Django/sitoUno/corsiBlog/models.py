from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Corsi(models.Model):
    #vado a delianare i campi della tabella
    titolo = models.CharField(max_length=150)
    descrizione = models.CharField(max_length=250)
    contenuto = models.TextField()
    data_inizio = models.DateField()
    durata_ore = models.DecimalField(decimal_places=3, max_digits=3)
    docente = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    prezzo = models.DecimalField(decimal_places=10, max_digits=10)

    def __str__(self):
        return self.titolo
    
    class Meta:
        verbose_name_plural = "Corsi"