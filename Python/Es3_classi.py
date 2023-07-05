""" 
Esercizio 3
Crea una classe GestoreMagazzino che gestisca un magazzino di prodotti. La classe dovrà avere i seguenti attributi:
Un dizionario “prodotti” che mappa i nomi dei prodotti ai rispettivi oggetti “Prodotto” (che descriverai in seguito)
Una variabile “costo_magazzinaggio” che indica il costo per magazzinare ogni prodotto per un mese
La classe dovrà avere i seguenti metodi:
Un metodo “aggiungi_prodotto” che aggiunga un nuovo prodotto al magazzino
Un metodo “rimuovi_prodotto” che rimuova un prodotto dal magazzino
Un metodo “calcola_costi_magazzinaggio” che calcoli i costi di magazzinaggio per tutti i prodotti presenti nel magazzino
Crea inoltre una classe Prodotto che abbia gli attributi “nome”, “prezzo” e “scorta”. 
"""

class Prodotto:
    def __init__(self, nome, prezzo,scorta):
        self.nome = nome
        self.prezzo = prezzo
        self.scorta = scorta

    def __str__(self):
        return f"Prodotto: {self.nome}, prezzo: {self.prezzo}€, quantità in magazzino {self.scorta}"
    
class GestoreMagazzino:
    def __init__(self, costo_magazzino):
        pass

    def aggiungi_prodotto(self, prodotto):
        pass

    def rimuovi_prodotto(sel, nome_prodotto):
        pass

    def calcola_costi_magazzino(self):
        pass
        

p1 = Prodotto("Telefono",500,10)
p2 = Prodotto("MacBook Pro M2", 4000, 5)

mz1 = GestoreMagazzino(15)