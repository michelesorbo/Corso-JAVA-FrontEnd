# for n in range(11):
#     print(n)


#Replico il for con WHILE
#for(conta = 0; conta <= 10; conta += 1)
# conta = 0

# while conta <= 10:
#     conta += 1
#     print(conta)


#Sommo i numeri finchè non inserisci 0

# num = int(input("Inserisici un numero 0 per terminare: "))
# somma = 0

# while num != 0:
#     somma += num
#     num = int(input("Inserisci un nuovo numero 0 per terminare: "))

# print(f"La somma dei numeri inseriti è: {somma}")


#istruzione break

# run = True
# stop = 10
# cont = 0

# while run == True:
#     print(cont)
#     cont += 1
#     if cont > stop:
#         print("Sto uscendo")
#         break

# print("Ciclo finito")

# cont = 0

# while cont <= 10:
#     if cont == 6 or cont == 5:
#         cont += 1
#         continue
#     print(cont)
#     cont += 1


#Indovina il numero
#Creare un numero Random compreso tra 1 e 10 e chiedere all'utente di indovinare il numero

#Importare la libreria random
import random
rand_num = random.randint(1, 10)
print(rand_num)

ind = int(input("Inserisci il numero e prova la fortuna: "))
tentativi = 1

while rand_num != ind:
    ind = int(input("SBAGLIATO!!!! prova ancora: "))
    tentativi += 1

print(f"BRAVOOOOO!!!! hai indovinati in {tentativi} tentativi")