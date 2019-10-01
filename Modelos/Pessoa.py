from abc import ABCMeta, abstractmethod
import Enum_tipoAluno

Class Pessoa:

    __init__(self, nome: str, matricula: int, tipo_aluno: tipo_aluno):
        self.__nome = nome
        self.__matricula = matricula
        self.__tipo_aluno = tipo_aluno

    @property
    def get_nome(self):
        return self.__nome

    @property
    def get_matricula(self):
        return self.__matricula

    @property
    def get_tipo_pessoa(self):
        return self.__tipo_aluno

    @nome.setter
    def set_nome(self, nome):
        self.__nome = nome

    @matricula.setter
    def set_matricula(self, matricula):
        self.__matricula = matricula
