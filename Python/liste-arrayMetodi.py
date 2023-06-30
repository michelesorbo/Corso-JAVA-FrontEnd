ar_testo = ["Uno", "pasta", "prova"] #Lista di Stringhe
ar_num = [23,43,8.14] #Lista numerica
ar_mista = [12, "testo", True, ["nuova", "Lista"], ar_testo]
print(ar_mista)

#Per stampare un singolo elemento della lista devo indicare l'indice dell'elemento
print(ar_mista[2])
print(ar_mista[3][1])
print(ar_mista[4][2])

ar = [1,3,5,67,8,6,45,6,78,6,4,34,23,6,8,23,5,43,9,87,8]
#Conoscere quanti elementi ha la lista
print(len(ar))
#Per stamapre una parte della lista
print(ar[4:12]) #Dall'indice 4 fino al 12 escluso
print(ar[4:]) #dall'indice 4 fino alla fine
print(ar[:4])#Dall'inizio dino all'indice 4 escluso

#Per leggere gli elemente di una lista
# for el in ar:
#     print(el)

#Ordinare una Lista per poterlo fare la lista deve avere gli elementi dello stesso tipo
#Rif: https://www.w3schools.com/python/ref_list_sort.asp
ar_1 = [2,4,6,1]
ar_1.sort()#Modifica la lista
print(ar_1)
ar_1a = ['Michele', 'Alessio',"Massimiliano"]
ar_1a.sort()
print(ar_1a)


#Come aggiungere elemnti ad una lista
#Metodo append, inserisce l'elemento alla fine della lista Rif: https://www.w3schools.com/python/ref_list_append.asp
ar_2 = ['mele','fragole','pere']
ar_2.append("limone")
print(ar_2)

#Metodo insert, inscerisce un elemneto in uno specifico indice
ar_2a = ['francesco','silvia','stefania']
ar_2a.insert(1,"marco")
print(ar_2a)

#Per cancellare tutti gli elementi da un array si usa clear()
#Rif: https://www.w3schools.com/python/ref_list_clear.asp
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
print(fruits)

#Contare qunte occorrenze ci sono in una lista
#Rif: https://www.w3schools.com/python/ref_list_count.asp
ar_3 = [2,4,6,2,3,2]
print(ar_3.count(2))
ar_3a = ['apple', 'banana', 'cherry', 'orange']
print(ar_3a.count('apple'))

#Creare una lista che contenga 5 presi random compresi tra 1 e 10, tutti diversi
import random
ar_rand = []

while len(ar_rand) < 5:
    n = random.randint(1,10)
    if ar_rand.count(n) == 0:
        ar_rand.append(n)

print(ar_rand)

#Per copiare una lista si usa copy()
ar_4 = [2,4,5,1,3]
ar_4a = ar_4.copy() #Creo una copia
print(ar_4a)

#Estendere Liste
ar_5 = [3,'Michele']
ar_5.extend(ar_4)
print(ar_5)

#Per trovare l'inidce di un elemento nella lista si unsa index(), ritorna l'indice della prima occorrenza
ar_6 = ['apple', 'banana', 'cherry','apple']
print(ar_6.index('apple'))


#Come rimuovere elementi dalla lista
#Metodo pop, rimuove l'elemento specifanco l'indice
ar_7 = ['apple', 'banana', 'cherry','apple']
#ar_7.pop(1) #Elemento con indice 1
ar_7.pop() #Di defolt toglie l'ultimo elemento (-1)
print(ar_7)

#Metodo Remove
ar_7_a = ['apple', 'banana', 'cherry','apple']
ar_7_a.remove('apple')
print(ar_7_a)

ar_7_b = [12,4,54,6]
ar_7_b.remove(4)
print(ar_7_b)

#Revers serve a invertire gli elementi della lista
ar_8 = ['apple', 'banana', 'cherry','apple']
ar_8.reverse()
print(ar_8)