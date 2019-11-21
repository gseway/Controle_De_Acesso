from DAO.dao import DAO
from Entidades.aluno_presidente import AlunoPresidente


class PresidenteDAO(DAO):

    def __init__(self):
        super().__init__('presidentes.pkl')

    def add(self, key, presidente: AlunoPresidente):
        if isinstance(presidente, AlunoPresidente) and (presidente is not None) and isinstance(presidente.matricula,
                                                                                               str):
            key = presidente.matricula
            super().add(key, presidente)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
