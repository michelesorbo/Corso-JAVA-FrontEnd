#Servono a scrivere dei blocchi di codice riutilizzabili

#def nome_funzione(eventuali_parametri)
def saluta():
    print("Ciao Mondo!!!!")
    print("Ciao a tutti!!!")

#Per chiamre (Invocare) una funzione bisogno scrivere il nome_della_funzione()
saluta()
saluta()
saluta()
saluta()
saluta()
saluta()
saluta()

#Una funzione può ricevere parametri senza ritorno
def salutaNome(nome):
    print(f"Ciao {nome}")

salutaNome("Alessio")
n = "Silvia"
salutaNome(n)

#Funzione con ritorno 
def somma(n1, n2):
    return n1 + n2

n_1 = somma(4,8)

print(n_1)
print(somma(54,78))

def stapaAR(ar):
    testo = ""
    for el in ar:
        testo += f"{el}, "
    return testo

ar = [1,4,3,6,7]
ar_2 = ['Michele','Silvia','Stefania']
print(stapaAR(ar_2))

mio_testo = stapaAR(ar)
print(mio_testo)

def pulisciStringa(testo):
    testo = testo.strip()
    testo = testo.replace(",", "")
    testo = testo.replace(".", "")
    testo = testo.replace("  ", " ")
    testo = testo.lower()
    return testo

parola = "   Ciao, da , python"
print(pulisciStringa(parola))

#Funzioni con parametri di Default
def preparaPrimo(tipo_pasta = "rigatoni", sugo = True):
    print(f"La pasta sceta è: {tipo_pasta}")
    if sugo:
        print("E preparo il sugo")
    else:
        print("Pasta in bianco")

preparaPrimo()
preparaPrimo("Penne", False)
preparaPrimo("Penne")


#KeyArguments
preparaPrimo(sugo = False, tipo_pasta= "Penne")

#Funzioni con parametri variabili
def sommaNumeri(*numeri):
    somma = 0
    for el in numeri:
        somma += el
    return somma

print(sommaNumeri(2,5))
print(sommaNumeri(4,5,8,98,78))
print(sommaNumeri(2,5,98,34,2,34,5,76,8,9,45))

def operazioniMultiple(operando, *numeri):
    pass

operazioniMultiple("/", 3,6,7,23,5)
operazioniMultiple("+", 46,7,23,5,89)