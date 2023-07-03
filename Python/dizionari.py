#rif: https://www.w3schools.com/python/python_dictionaries.asp
mio_diz = {
    "nome" : "Michele",
    "eta": 43,
    "citta" : "Caserta",
    "linguaggio": "Python",
    "strumento": "Chitarra"
}

print(mio_diz)

#per stampare le chiavi di un dizionario
print(mio_diz.keys())

#per stampare solo i valori di un dizionario
print(mio_diz.values())

#Per visualizzare le coppie chiavi valori 
print(mio_diz.items())

#per stamapre il valore di una chiave
print(mio_diz["eta"])

#Come rimuovere elementi da un dizionario
# del nome_dizionario["chiave_da_eliminare"]
del mio_diz["eta"]
print(mio_diz)

#Per verificare la presenza di elementi in un dizionario
# if "eta" in mio_diz:
#     print("Presente")
# else:
#     print("non presente")

# for k in mio_diz.keys():
#     if k == "strumento":
#         print("Chiave trovata")
#     else:
#         print("Chiave non trovata")

#Cambiare valore ad una chiave
#mio_diz["strumento"] = "Pianoforte"
mio_diz.update({"strumento2" : "Batteria"}) #Se non trova la chiave aggiunge l'elemento al dizionario
#Update serve anche per aggiungere un nuovo elemento al dizionario
print(mio_diz)
print(mio_diz.get("strumento", "Chiave non trovata"))

#per eliminare un elemento da dizionario
mio_diz.pop("strumento2") #Alternativa del mio_diz["strumento2"]
print(mio_diz)
mio_diz.popitem()#Elimino sempre l'ultimo elemento
print(mio_diz)

#Per svuotare un dizionario
mio_diz.clear()
print(mio_diz)

mio_diz.update({
    "nuovo_nome":"Silvia",
    "nuovo_corso":"Python"
})

print(mio_diz)

#Per stamapre sia chiave che valore
for k,v in mio_diz.items():
    print(f"Chiave: {k}\nValore: {v}\n\n")

#per copiare un dizionario 
#copia_diz = mio_diz.copy()
copia_diz = dict(mio_diz)
print(f"Copia: {copia_diz}")

#Nested Dictionaries
alunni = {
    "alunno 1" : {
        "nome" : "Alessio",
        "cognome" : "Leodori"
    },
    "alunno 2":{
        "nome" : "Greg",
        "cognome": "Grecu"
    },
    "alunno 3":{
        "nome" : "Mohamed",
        "cognome" : "Abdali"
    }
}

print(alunni["alunno 3"]["nome"])

alunno1 = {
    "nome" : "Silvia",
    "cognome" : "Drea"
}

alunno2 = {
    "nome" : "Enza",
    "cognome" : "Macrì"
}

mia_classe = {
    "alunno1" : alunno1,
    "alunno2" : alunno2
}