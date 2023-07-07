"""
Scrivere una funzione che prenda una parola in imput e stampi tutte le lettere una per riga

def stampaCaratteri(parola):
pass

parola = passata da utente
"""
import time

def stampaCaratteri(parola):
    for c in parola:
        print(c)
        time.sleep(1)

# parola = input("inserisci una parola: ")
# stampaCaratteri(parola)

"""
Creare un dizionario con le seguenti chiavi e valori: "nome" : "Mario", "cognome" : "Rossi", "età" : 30.
"""

mio_diz = {
    "nome":"Mario",
    "cognome":"Rossi",
    "eta":30
}

"""
Creare un elenco di studenti per il corso JAVA
Per ogni studente si conoscono Nome, Cognome, età

Creare una funzione che chieda all'untete se vuole inserire un nuovo studente all'elenco dei corsisti di JAVA
le opzioni sono
1)Inserisci nuovo studente
2)Visualizzi elenco studenti
3)Chiudi il programma
"""
alunni = [] #Lista vuota
scelta = input("""Cosa vuoi fare?
            1)Inserisci nuovo studente
            2)Visualizzi elenco studenti
            3)Chiudi il programma """)

while scelta != "3":
    if scelta == "1":
        nome = input("Inserisci Nome alunno: ")
        cognome = input("Inserisci Cognome alunno: ")
        eta = input("Inserisci età alunno: ")
        diz_alunno = {
            "nome":nome,
            "cognome":cognome,
            "eta":eta
        }
        alunni.append(diz_alunno)
    elif scelta == "2":
        for el in alunni:
            print(el)
    else:
        print("Scelta non valida")
    
    scelta = input("""Cosa vuoi fare?
                1)Inserisci nuovo studente
                2)Visualizzi elenco studenti
                3)Chiudi il programma """)
    
print("Programma terminato")

