class Persona:
    #Prima cosa da fare è creare un costruttore
    #contatore = 0
    def __init__(self, nome, cognome):
        self._nome = nome #Rendo privata la variabile (Le variabili private sono visibili sono all'interno della classe)
        self.cognome = cognome
        #self.aumentaCont()

    def getNome(self):
        return self._nome
    
    def setNome(self,nome):
        self._nome = self._formattaTesto(nome)

    def _formattaTesto(self, testo):
        testo = testo.strip()
        testo = testo.lower()
        return testo
    
    #Metodi (Funzioni in procedurale)
    def saluta(self):
        return f"Ciao da {self._nome}"
    
    # def aumentaCont(cls):
    #     cls.contatore += 1


#Creao la classe Studente che eredita la classe Persona
class Studente(Persona):
    def __init__(self, nome, cognome, classe):
        super().__init__(nome, cognome)
        self.classe = classe

    def getClasse(self):
        return self.classe
    
    def setClasse(self, classe):
        self.classe = classe
    
    #Overload
    def saluta(self):
        return f"Buongiorno sono lo studente {self._nome} e frequento la classe di {self.classe}"



#FUORI DALLA CLASSE
persona1 = Persona("Michele", "Sorbo")
persona2 = Persona("Stefania", "Malfatti")

st1 = Studente("Alessio","Leodori","Python")

print(st1.saluta())
print(persona1.saluta())
print(st1.getClasse())
persona1.setNome("Alessio")
print(persona1.getNome())


print(persona1.saluta())
print(persona2.saluta())


