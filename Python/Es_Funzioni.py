"""
Scrivi una funzione che prende una parole e restituisce se la parola è palindroma.
Es: osso = osso SI
Es: casa = asac NO

Sfruttando la funzione isPalindrom(), creare un programma che chieda all'utente di inserire parole
e valuti se la parola o frase è palindorma o no. Tutte le parole o frasi verranno salvate in 2 liste.
Una lista con le parole o frasi palindore e una lista con le parole o frsi non palindrome.
Il software darà subito la risposta e terminera quando l'utente inserisce "fine". al termine il software
mostrerà l'elenco delle parole divise per palindome e non palindorem e il numero totale di parole inserite

es: osso
Parola Palindroma
Inserisci nuova parola->

al termine
elenco parole palindorme
elenco parole non palindrome

Parole inserite 30 di cui 10 palindrome e 20 non palindrome
"""

def isPalindrom(parola):
    parola_revers = parola[::-1]
    if parola == parola_revers:
        return True
    else:
        return False

def leggiLista(lista):
    parole = ""
    for el in lista:
        parole += el + ", "
    return parole

parola = input("Inserisci una parola e ti dico se è palindroma, fine per terminare: ")
parole_palindorme = []
parole_non_palindrome = []

while parola != "fine":
    if isPalindrom(parola):
        parole_palindorme.append(parola)
        print("PALINDROMA")
    else:
        parole_non_palindrome.append(parola)
        print("NON PALINDROMA")
    parola = input("Inserisci una nuova parola o fine per terminare: ")

#Dopo il wile il programma finisce
print(f"Hai inserito {len(parole_palindorme) + len(parole_non_palindrome)}")
print(f"Le parole palindrome sono {len(parole_palindorme)} e sono: {leggiLista(parole_palindorme)}")
print(f"Le parole non palindrome sono {len(parole_non_palindrome)} e sono: {leggiLista(parole_non_palindrome)}")



# def isPalindrom(parola):
#     ar_rev = list(parola)
#     #Faccio il revers dell'array
#     ar_copy = ar_rev.copy()
#     ar_rev.reverse()
#     if(ar_copy == ar_rev):
#         return True
#     else:
#         return False


# if isPalindrom("osso"):
#     print("Palindroma")
# else:
#     print("Non Palindroma")