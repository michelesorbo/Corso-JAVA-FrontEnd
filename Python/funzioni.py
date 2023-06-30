#Servono a scrivere dei blocchi di codice riutilizzabili

#def nome_funzione(eventuali_parametri)
def saluta():
    print("Ciao Mondo!!!!")

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
