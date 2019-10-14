from Enum import enum_tipoAluno
from Modelos import Pessoa


class Aluno_normal(Pessoa):

    def __init__(self, nome: str, matricula: int, tipo_aluno: enum_tipoAluno):
        super().__init__(nome, matricula, tipo_aluno)


    def getAlunos(self):
        return self.__alunos

    def setAlunos(self, alunos):
        self.__alunos = alunos

    def add_Alunos(self, Aluno_normal):
        self.__Alunos.append(Aluno_normal)

    def removeAluno(self, index):
        self.Alunos.remove(index)
