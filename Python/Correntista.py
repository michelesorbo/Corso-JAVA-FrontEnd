import time

tempo = time.localtime()

class Correntista:
    def __init__(self, nome, cognome, n_conto, saldo):
        self.__nome = nome
        self.__cognome = cognome
        self.__n_conto = n_conto
        self.__saldo = saldo

    @property
    def _nome(self):
        return self.__nome

    @_nome.setter
    def _nome(self, value):
        self.__nome = value

    @property
    def _cognome(self):
        return self.__cognome

    @_cognome.setter
    def _cognome(self, value):
        self.__cognome = value

    @property
    def _n_conto(self):
        return self.__n_conto

    @_n_conto.setter
    def _n_conto(self, value):
        self.__n_conto = value

    @property
    def getSaldo(self):
        return self.__saldo

    def setSaldo(self, value):
        self.__saldo = value

    def versamento(self, importo):
        self.__saldo += importo


cr1 = Correntista("Alessio", "Leodori", "001", 100000)
print(f"{cr1.getSaldo()}")