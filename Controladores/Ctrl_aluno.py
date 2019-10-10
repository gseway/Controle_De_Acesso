from Modelos import Aluno_normal
from Controladores import Ctrl_principal
from Telas import Tela_presidente
from Enum import enum_tipoAluno


class Ctrl_aluno:
    def __init__(self, Aluno: Aluno_normal):
        self.Aluno_normal = Aluno

    def CriaAluno(self, nome, matricula, enum_tipoAluno):
        self.Aluno_normal.add_Alunos(nome, matricula, enum_tipoAluno)

    def removeAluno(self, index):
        self.Aluno_normal.removeAluno(index)

    def lista(self):
        pass
