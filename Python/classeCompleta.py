class Persona:
    totale_persone = 0#Variabile di classe
    #Prima di tutto creo il metodo inizializzatore con i prametri base per creare la classe
    def __init__(self,nome = "", cognome = "", eta = "", residenza = ""):
        self.nome = nome #Vado a passare il paramentro alla variabile di classe
        self.cognome = cognome
        self.eta = eta
        self.residenza = residenza
        Persona.totale_persone += 1 #Incremento la variabile di classe

    #@classmethod è il decoratore che si utilizza per creare i metodi di classe, 
    # e che permette quindi di passare come parametro la classe invece dell'istanza
    @classmethod
    def from_string(cls,stringa_persona, *args):
        nome, cognome,eta,residenza = stringa_persona.split("-")
        return cls(nome,cognome,eta,residenza, *args)

    #__str__ ritorna una rappresentazione sotto forma di stringa dell'oggetto assegnato alla classe
    def __str__(self):
        return f"\n***\n\nNome: {self.nome}\nCognome: {self.cognome}\nEtà: {self.eta}\nResidenza: {self.residenza}"

    #Metodi
    def modifica_dati(self):
        print("""Modifica Scheda:
        1 - Nome
        2 - Cognome
        3 - Età
        4 - residenza""")

        scelta = input("Cosa desideri modificare?: ")
        if scelta == "1":
            self.nome = input("Nuovo Nome -> ")
        elif scelta == "2":
            self.cognome = input("Nuovo Cognome -> ")
        elif scelta == "3":
            self.eta = input("Nuova Età -> ")
        elif scelta == "4":
            self.residenza = input("Nuova Residenza -> ")
        else:
            print("Scelta non valida")
        
        return "Modifiche Effettuate"

        
#FINE CLASSE PERSONA

#Inizio Classe Studente figlio di Persona
class Studente(Persona):

    totale_studenti = 0
    def __init__(self, nome="", cognome="", eta="", residenza="", corso_di_studio = ""):
        super().__init__(nome, cognome, eta, residenza)
        self.corso_di_studio = corso_di_studio
        Studente.totale_studenti += 1
    
    #Inplemento il metodo __str__ e aggiungo il nuovo parametro
    def __str__(self):
        return super().__str__() + f"\nCorso di Studio: {self.corso_di_studio}"

#FINE CLASSE STUDENTE

#INIZIO CLASSE INSEGNANTE
class Insegnate(Persona):
    def __init__(self, nome="", cognome="", eta="", residenza="", materia = None, ore_lavoro = None):
        super().__init__(nome, cognome, eta, residenza)
        self.materia = materia
        self.ore_lavoro = ore_lavoro
    
    def __str__(self):
        return super().__str__() + f"\nMateria insegnata: {self.materia}\nOre Lavoro: {self.ore_lavoro}"


#CREO LA CALASSE AULA per contenere gli studenti
class Aula:
    def __init__(self, nome):
        self.alunni = {}
        self.nome = nome
    
    def aggiungiAlunno(self, studente):
        self.alunni[studente.nome] = studente
        self.alunni[studente.cognome] = studente

    def visualizzaStudenti(self):
        for alunno in self.alunni:
            print(f"Nome: {self.alunni[alunno].nome} Cognome: {self.alunni[alunno].cognome}")



#FUORI DALLA CLASSE
p1 = Persona("Michele","Sorbo",43,"Caserta")
p2 = Persona(eta=35,cognome="Leodori",nome="Alessio",residenza="Roma")
p3 = Persona("Enza", "Macrì", 19,"Reggio")

p4 = Persona("Michele")

iron_man = "Tony-Stark-40-Torre Stark"
p5 = Persona.from_string(iron_man) #p5 = PErsona(Tony-Stark-40-Torre Stark)



# print(p1)
# print(p2.residenza)
# print(Persona.totale_persone)
# print(p5)
#print(p1.modifica_dati())
# print(p1)

s1 = Studente("Marco", "Piottante", 25, "Roma","Python")
# print(s1)
# print(Persona.totale_persone)
# print(Studente.totale_studenti)

nuovo_studente = "Mario-Rossi-33-Roma"
s2 = Studente.from_string(nuovo_studente, "JAVA")
# print(s2)

aula1 = Aula("3A")
aula1.aggiungiAlunno(s1)
aula1.aggiungiAlunno(s2)
aula1.visualizzaStudenti()

# nuovo_insegnante = "Bruono-Barbieri-55-Bologna"
# ins1 = Insegnate.from_string(nuovo_insegnante, "Cucina", 36)
# print(ins1)