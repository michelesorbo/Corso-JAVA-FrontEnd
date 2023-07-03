#Creo la classe Studente

class Studente:
    #ogni classe ha bisogno di un inizializzatore
    #creo il metodo __init__
    __voto = 0
    def __init__(self, nome="John", cognome="Doe", corso="Nessuno"):
        self.__nome = self.__testoFormat(nome) #Inposto una variabile globale nome e gli assegno il valore passato a nome nella funzione
        self.__cognome = self.__testoFormat(cognome) #Dichiare la variabile private con __
        self.__corso = self.__testoFormat(corso)

    #Creo l'incapsulamento della classe studente
    def getNome(self):
        return self.__testOut(self.__nome)
    
    def setNome(self,nome):
        self.__nome = self.__testoFormat(nome)

    def getCognome(self):
        return self.__testOut(self.__cognome)
    
    def setCognome(self, cognome):
        self.__cognome = self.__testoFormat(cognome)

    def getVoto(self):
        return self.__voto

    def setVoto(self, voto):
        self.__voto = voto

    def getCorso(self):
        return self.__testOut(self.__corso)

    def setCorso(self,corso):
        self.__corso = self.__testoFormat(corso)
    
    #FINE Incapsulamento

    #Inizio Metodi della classe
    def scheda_studente(self):
        return f"Nome: {self.__nome}\nCognome: {self.__cognome}\nCorso: {self.__corso}"

    def __testoFormat(self,testo):
        testo = testo.strip()
        testo = testo.lower()
        return testo
    
    def __testOut(self, testo):
        return testo.capitalize()


#Inizio programma
st1 = Studente("Silvia","Drea", "JAVA")#st1 è un oggetto della classe Studente
st2 = Studente("Alessio","Leodori", "Python")
st3 = Studente("Mohamed", "", "Python")

#st1.setNome("Antonella")
# print(st1.scheda_studente())
# print(st2.scheda_studente())
# print(st3.scheda_studente())

st1.setNome("  AnTONELLa  ")
print(f"Voto per lo studente {st1.getNome()} è: {st1.getVoto()}")

#Creare una classe correntista
#Per ogni correntisca conoscere Nome, Cognome, N° Contto, Capitale Iniziale
#Fare incapsulamento
#Fare il metodo per conoscere il saldo 
#Fare il metodo per un versamento
#Fare il metodo per un prelievo