# lista = [1,"Ciao",9.45]

# lista.append("Michele")

# for el in lista:
#     print(el)

#range(start, stop, incremento)
#range(start, stop) parte da start incluso e si ferma a stop escluso
#range(stop) Parte da 0 e si ferma allo stop escluso

#Stampare i primi 10 nnumeri partendo da 1
# for n in range(1, 11, 2):
#     print(n)

#Mi stampi i numeri da 10 a 0
#for(let i = 10; i >= 0; i--)

# for n in range(10,-1,-1):
#     print(n)


#Chiedere quanti numeri si voglio sommare, e poi chiedere i singoli numeri.
#Alla fine far uscire la somma di tutti i numeri inseriti
#e l'lelenco dei inumeri inseriti
#Qunti numeri vuoi inserire? 3
#Inserisci numero: 3
#Inserisci numero: 4
#Inserisci numero: 1
#La somma dei numeri è: 8 e i numeri inseriti sono 3,4,1 ar.append(n)

fine = int(input("Quanti numeri vuoi inserire?: "))
lista = [] #lista vuota
somma = 0

for n in range(fine):
    num = int(input("Inserisci un numero: "))
    somma += num
    lista.append(num)

testo = ""

for el in lista:
    testo += str(el) + ", "

#print(f"La somma è: {somma} e i numeri inseriti sono {testo}")
print("La somma è " + str(somma) + " e i numeri inseriti sono " + testo)