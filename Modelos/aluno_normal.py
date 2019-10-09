from Modelos import pessoa
from Enum import enum_tipoAluno

class Aluno_normal(pessoa):

  def  __init__(self, nome: str, matricula: int, tipo_aluno: enum_tipoAluno):
        super().__init__(nome, matricula, tipo_aluno)
