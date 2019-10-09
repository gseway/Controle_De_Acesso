from Modelos.pessoa import Pessoa
from Enum import enum_tipoAluno


class AlunoPresidente(Pessoa):

    def __init__(self, nome: str, matricula: int, tipo_aluno: enum_tipoAluno, cpf: int, email: str):
        super().__init__(nome, matricula, tipo_aluno)
        self.__cpf = cpf
        self.__email = email

    def get_cpf(self):
        return self.__cpf

    def get_email(self):
        return self.__email

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def set_email(self, email):
        self.__email = email
