from abc import ABC, abstractmethod
<<<<<<< HEAD
from Enum import enum_tipoAluno
=======
from enum_tipoAluno import Tipo_aluno
>>>>>>> 2fba35e167035f6316e76e5fda6ab1e2bb7afea8

class Pessoa(ABC):
    
    @abstractmethod
<<<<<<< HEAD
    def __init__(self, nome: str, matricula: int, tipo_aluno: enum_tipoAluno):
=======
    def __init__(self, nome: str, matricula: int, tipo_aluno: Tipo_aluno):
>>>>>>> 2fba35e167035f6316e76e5fda6ab1e2bb7afea8
        self.__nome = nome
        self.__matricula = matricula
        self.__tipo_aluno = tipo_aluno

    def get_nome(self):
        return self.__nome

    def get_matricula(self):
        return self.__matricula

    def get_tipo_pessoa(self):
        return self.__tipo_aluno

    def set_nome(self, nome):
        self.__nome = nome

    def set_matricula(self, matricula):
        self.__matricula = matricula