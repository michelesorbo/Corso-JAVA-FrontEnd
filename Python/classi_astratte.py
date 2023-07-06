from abc import ABC, abstractmethod
import math
class Persona(ABC):
    def __init__(self, nome,cognome):
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        pass

class Studente(Persona):
    def __init__(self, nome, cognome, classe):
        super().__init__(nome, cognome)
        self.classe = classe

    #Definire tutti i metodi astratti del padre
    def saluta(self):
        return "Ciao dallo studente"


print(math.pi)

p1 = Persona("Mario","Rossi")
print(p1.nome)