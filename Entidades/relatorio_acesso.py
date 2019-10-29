from datetime import date


class RelatorioAcesso():
    def __init__(self, nome: str, cpf: str, data: date):
        self.__nome = nome
        self.__cpf = cpf
        self.__data = data

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def data(self):
        return self.__data

    def __str__(self):
        return f"Nome: {self.__nome}, CPF: {self.__cpf}, Data: {self.__data}\n"