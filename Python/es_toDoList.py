""" 
Quando parte il programma vedo la lista di default e due opzioni
1) Inserisci nuovo elemento nella lista
2) Cancella elemento dalla lista
3) Opzionale cambia ordine tra gli elementi
4) 0 per chiudere il programma
Fare tutto con i metodi

Visualizzazione della lista
1) Pane\n
2) Biscotti\n
3) Latte\n
"""
toDo = ["Pane","Biscotti", "Latte"]

def pulisciStringa(testo):
    testo = testo.strip()
    testo = testo.replace(",", "")
    testo = testo.replace(".", "")
    testo = testo.replace("  ", " ")
    testo = testo.lower()
    testo = testo.capitalize()
    return testo

def visualizzaToDO(ar):
    count = 1
    for el in ar:
       print(f"{count}) {el}")
       count += 1 

def insToDo(ar):
    item = input("Inserisci una nuova voce: ")
    item = pulisciStringa(item)
    ar.append(item)


#Faccio partire il sortware

#Stampo la lista base
visualizzaToDO(toDo)

#creo il menu in loop
scelta = int(input("\n\nBenvenuno nella lista della spesa\nScegli cosa vuoi fare\n1) Inserisci nuovo item\n0) Termina\n->"))

while scelta != 0:
    
    if scelta == 1:
        insToDo(toDo)
        visualizzaToDO(toDo)
    else:
        print("\n\nScelta non valida riprova")
    
    #Fuori dall'if
    scelta = int(input('\n\nScegli cosa vuoi fare\n1) Inserisci nuovo item\n0) Termina\n->'))

print("Programma chiuso")
