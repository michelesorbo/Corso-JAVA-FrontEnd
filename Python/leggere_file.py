testo = "Ciao Mondo!!!"

""" 
#Vado ad aprire il file per salvare il contenuto di testo
file_uno = open("file_esempio.txt","w") #Nome del file da aprire, modalità di apertura w, r, a
file_uno.write(testo) #Vado a scrivere sul file
file_uno.close() #Chiudo il file DA FARE SEMPRE 
"""

def scriviFile(testo):
    file_uno = open("file_esempio.txt","a") #Nome del file da aprire, modalità di apertura w, r, a
    file_uno.write("\n") #Creo una nuova riga sul fle txt
    file_uno.write(testo) #Vado a scrivere sul file
    file_uno.close() #Chiudo il file DA FARE SEMPRE

#scriviFile("Sono un nuovo testo")

""" 
#Scrivere un programma che chida di inserire testo sul file, il programma termina
#quando l'utente scrive fine
ins_testo = input("Inserisci quello che vuoi, 'fine' per terminare: ")

while ins_testo.rstrip().lower() != "fine":
    scriviFile(ins_testo)
    ins_testo = input("Inseriesci altro o scrivi 'fine': ")

print("Fine programma") 
"""

def readFile():
    file_uno = open("file_esempio.txt", "r")
    print(file_uno.read())

""" 
ins_testo = input("Cosa vuoi fare?\n1) per inserire un nuovo argomento nel file\n2) visualizza file\n'fine' per terminare\n-> ")

while ins_testo.rstrip().lower() != "fine":
    
    if ins_testo.rstrip() == "1":
        testo = input("inserisci il testo da aggiungere: ")
        scriviFile(testo)
        ins_testo = input("Cosa vuoi fare?\n1) per inserire un nuovo argomento nel file\n2) visualizza file\n'fine' per terminare\n->")
    elif ins_testo.rstrip() == "2":
        readFile()
        ins_testo = input("Cosa vuoi fare?\n1) per inserire un nuovo argomento nel file\n2) visualizza file\n'fine' per terminare\n->")
    else:
        print("Scelta non valida")
        ins_testo = input("Cosa vuoi fare?\n1) per inserire un nuovo argomento nel file\n2) visualizza file\n'fine' per terminare\n->")

print("Fine programma") 

 """

# file_uno = open("file_esempio/proverbi.txt", "r")
# ar_frase = []
# conta_linea = 1
""" 
for line in file_uno.readlines():
    if(line.count("casa")):
        ar_frase.append(f"Linea: {conta_linea} {line}")
    conta_linea += 1 #Aggiorno la linea sempre
 """
#Alternativa for senza dichiarare variabile esterna per count
# for i,line in enumerate(file_uno.readlines()):
#     if(line.count("casa")):
#         ar_frase.append(f"Linea: {i+1} {line}")

# for el in ar_frase:
#     print(el)
    

""" count = 0
for line in file_uno.readlines():
    count +=1
    print(f"Line{count}: {line}") """

"""
Per poter scrivere all'interno di un file dobbiamo aprire il file con i giusti permessi specificati nella funzione open:

    r: apre il file in sola lettura (modalità di default)
    r+: apre i file in lettura e scrittura, il puntatore viene posizionato all'inzio del file.
    w: apre il file in sola scrittura, se il file esiste lo sovrascrive, se non esiste lo crea.
    w+: apre il file in lettura e scrittura, se il file esiste lo sovrascrive, se non esiste lo crea.
    a: apre il file in scrittura senza sovrascrivere il contenuto corrente.
    a+: apre il file in lettura e scrittura senza sovrascrivere il contenuto corrente. Se il file non esiste lo crea.
Quindi come puoi capire non definendo un permesso apriamo automaticamente il file in lettura. Proviamo ad aprire il file in scrittura per l'aggiunta di contenuti (append).

"""

file_proverbi = open("file_esempio/proverbi.txt", "a+") #Il puntatore è posizionato alla fine del file
file_proverbi.seek(0) #Posiziono il puntatore all'inizio del file


def scriviFileMod(testo, file_txt):
    file_uno = open("file_esempio/"+file_txt,"a") #Nome del file da aprire, modalità di apertura w, r, a
    file_uno.write(testo) #Vado a scrivere sul file
    file_uno.close() #Chiudo il file DA FARE SEMPRE
    

def delete_line(filename, line_number):

    #open di default apre il file in lettura (r)
    with open(filename) as file:
        lines = file.readlines()
    
    if(line_number <= len(lines)):
        del lines[line_number - 1]

        with open(filename, "w") as file:
            for line in lines:
                file.write(line)
    else:
        print(f"La linea {line_number} non è presente nel file")


def scriviFileIndice(filename):
    with open(filename) as file:
        for i, line in enumerate(file.readlines()):
            print(f"{i+1}: {line}")

scriviFileIndice("file_esempio/alessio.txt")
delete_line("file_esempio/alessio.txt", 3)
print("\n\n\DOPO-------------------------\n\n")
scriviFileIndice("file_esempio/alessio.txt")