from Entidades.pessoa import Pessoa
from Enum import enum_tipoAluno


class AlunoPresidente(Pessoa):

    def __init__(self, nome: str, matricula: str, tipo_aluno: enum_tipoAluno, cpf: str, email: str, senha: str):
        super().__init__(nome, matricula, tipo_aluno, cpf, senha)
        self.__email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    def __str__(self):
        return f"Nome: {super().nome}    Matricula: {super().matricula}    CPF: {super().cpf}    email: {self.__email}\n"