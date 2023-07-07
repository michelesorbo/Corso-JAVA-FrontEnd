from django.db import models
#Importo la calsse di Django che gestisce gli utenti
from django.contrib.auth.models import User

# Create your models here.
#Creao la calsse Post che estende la casse Model di Django per gestire i DB.
#Il nome della classe sarà il nome della tabella el DB
class Post(models.Model):
    titolo = models.CharField(max_length=200) #Input di testo con grandezza massima di caratteri fissa a 200
    corpo = models.TextField(blank=True) #è una textarea, la rendo non obbligatoria
    data_ins = models.DateTimeField(auto_now_add=True) #DateTime e imposto che automaticamente sia impostata la data e l'ora corrente
    #Vado ad inserire l'utente che scriverà il post
    autore = models.ForeignKey(User, on_delete=models.CASCADE) #Vado a dire quale utente del sito ha scritto il post
    #CASCADE Cancello tutti i post che sono stati scritti da qull'ultente
    #DO_NATHING non fa nulla e lascio invariato il valore nella tabella, ricordati di gestire gli eventuali errori nel sito
    #SET_NULL setta il valore a nullo

    def __str__(self):
        return f"{self.titolo} data creazione: {self.data_ins.strftime('%A %d %B %Y')}"