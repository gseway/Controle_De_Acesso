from Enum import enum_tipoAluno
from Entidades.pessoa import Pessoa


class Aluno_normal(Pessoa):
    def __init__(self, nome: str, matricula: str, tipo_aluno: enum_tipoAluno, cpf: str, senha: str):
        super().__init__(nome, matricula, tipo_aluno, cpf, senha)

    def __str__(self):
        return f"Nome:{super().nome}    Matricula:{super().matricula}    CPF:{super().cpf}"