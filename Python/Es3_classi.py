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

#Soluzione con Dizionario  
# class GestoreMagazzino:
#     def __init__(self, costo_magazzino):
#         self.prodotti = {}
#         self.costo_magazzino = costo_magazzino

#     def aggiungi_prodotto(self, prodotto):
#         self.prodotti[prodotto.nome] = prodotto

#     def rimuovi_prodotto(self, nome_prodotto):
#         self.prodotti.pop(nome_prodotto)

#     def calcola_costi_magazzino(self):
#         costi = 0
#         for nome,prodotto in self.prodotti.items():
#             costi += prodotto.scorta * self.costo_magazzino
#         return costi
            
#Soluzione con le liste
class GestoreMagazzino:
    def __init__(self, costo_magazzino):
        self.prodotti = []
        self.costo_magazzino = costo_magazzino

    def aggiungi_prodotto(self, prodotto):
        self.prodotti.append(prodotto)

    def prodotti_in_magazzino(self):
        return len(self.prodotti)

    def rimuovi_prodotto(self, nome_prodotto):
        self.prodotti.remove(nome_prodotto)

    def calcola_costi_magazzino(self):
        costi = 0
        for prodotto in self.prodotti:
            costi += prodotto.scorta * self.costo_magazzino
        return costi

p1 = Prodotto("Telefono",500,10)
p2 = Prodotto("MacBook Pro M2", 4000, 5)

mz1 = GestoreMagazzino(15)

mz1.aggiungi_prodotto(p1)
mz1.aggiungi_prodotto(p2)
print(f"Il magazziono ha un costo di {mz1.calcola_costi_magazzino()} e ci sono {mz1.prodotti_in_magazzino()} prodotti")