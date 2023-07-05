""" 
Esercizio 2
Creare una classe Impiegato che abbia gli attributi “nome”, “cognome”, “matricola” e “stipendio”.
Aggiungere un metodo “aumenta_stipendio” che aumenti lo stipendio dell’impiegato del 10% 
e il metodo __str__ che stampi tutti i dettagli dell’impiegato, 
ad esempio “Impiegato: Marco Rossi, matricola 12345, stipendio: 3000 Euro”. 
"""

class Impiegato:
    def __init__(self, nome,cognome,matricola,stipendio):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola
        self.stipendio = stipendio

    def __str__(self):
        return f"Impiegato: {self.cognome} {self.nome}, matricola {self.matricola}, stipndio: {self.stipendio:.2f}€"
    
    def aumenta_stipendio(self, aumento_per=10):
        #con parametro fisso
        #self.stipendio *= 1.1
        self.stipendio += (self.stipendio * aumento_per) / 100


i1 = Impiegato("Mario","Rossi","IMP001", 1500)
print(i1)
i1.aumenta_stipendio()
print(i1)