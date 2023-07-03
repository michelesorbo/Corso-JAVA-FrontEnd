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

file_uno = open("file_esempio/proverbi.txt", "r")

print(file_uno.read())

""" count = 0
for line in file_uno.readlines():
    count +=1
    print(f"Line{count}: {line}") """