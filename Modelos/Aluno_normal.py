from Pessoa import Pessoa
from Enum_tipoAluno import TipoAluno

class Aluno_normal(Pessoa):

  def  __init__(self, nome: str, matricula: int, tipo_aluno: TipoAluno):
        super().__init__(nome, matricula, tipo_aluno)
