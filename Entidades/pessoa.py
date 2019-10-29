from abc import ABC, abstractmethod
from Enum.enum_tipoAluno import TipoAluno


class Pessoa(ABC):

    def __init__(self,nome: str, matricula: str, tipo_aluno: TipoAluno, cpf: str, senha: str):

        self.__nome = nome
        self.__matricula = matricula
        self.__tipo_aluno = tipo_aluno
        self.__cpf = cpf
        self.__senha = senha

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def tipo_pessoa(self):
        return self.__tipo_aluno

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula