from DAO.dao import DAO
from Entidades.aluno_normal import Aluno_normal


class AlunoDAO(DAO):

    def __init__(self):
        super().__init__('presidentes.pkl')

    def add(self, key, aluno_normal: Aluno_normal):
        if isinstance(aluno_normal, Aluno_normal) and (aluno_normal is not None) and isinstance(aluno_normal.matricula,
                                                                                               str):
            key = aluno_normal.matricula
            super().add(key, aluno_normal)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)