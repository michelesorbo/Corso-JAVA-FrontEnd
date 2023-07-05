#Creo la classe Studente

class Studente:
    #ogni classe ha bisogno di un inizializzatore
    #creo il metodo __init__
    studenti_totali = 0
    
    def __init__(self, nome="John", cognome="Doe", corso="Nessuno"):
        self._nome = self._testoFormat(nome) #Inposto una variabile globale nome e gli assegno il valore passato a nome nella funzione
        self._cognome = self._testoFormat(cognome) #Dichiare la variabile private con __
        self._corso = self._testoFormat(corso)
        self._voto = 0
        Studente.studenti_totali += 1

    #Creo l'incapsulamento della classe studente
    def getNome(self):
        return self._testOut(self._nome)
    
    def setNome(self,nome):
        self._nome = self._testoFormat(nome)

    def getCognome(self):
        return self._testOut(self._cognome)
    
    def setCognome(self, cognome):
        self._cognome = self._testoFormat(cognome)

    def getVoto(self):
        return self._voto

    def setVoto(self, voto):
        self._voto = voto

    def getCorso(self):
        return self._testOut(self._corso)

    def setCorso(self,corso):
        self._corso = self._testoFormat(corso)
    
    #FINE Incapsulamento


    #__str__ ritorna una rappresentazione sotto forma di stringa dell'oggetto assegnato alla classe

    def __str__(self):
        return f"Nome: {self._nome}\nCognome: {self._cognome}\nCorso: {self._corso}"


    #Inizio Metodi della classe
    def scheda_studente(self):
        return f"Nome: {self._nome}\nCognome: {self._cognome}\nCorso: {self._corso}"

    def _testoFormat(self,testo):
        testo = testo.strip()
        testo = testo.lower()
        return testo
    
    def _testOut(self, testo):
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

print(Studente.studenti_totali)
print(st1)
#Creare una classe correntista
#Per ogni correntisca conoscere Nome, Cognome, N° Contto, Capitale Iniziale
#Fare incapsulamento
#Fare il metodo per conoscere il saldo 
#Fare il metodo per un versamento
#Fare il metodo per un prelievo