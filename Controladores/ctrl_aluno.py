import sys
from Modelos import Aluno_normal
from Telas import Tela_aluno


class Ctrl_aluno:
    def __init__(self, Aluno: Aluno_normal):
        self.__alunos = []

    def inclui_aluno(self, novo_aluno: Aluno_normal):
        for aluno in self.__alunos:
            if aluno.get_matricula() == novo_aluno.get_matricula():
                # se existir um aluno com a mesma matricula, retorna None e para o loop
                print("Já existe um aluno com essa matricula")
                return
        self.__alunos.append(novo_aluno)

    def lista_alunos(self):
        index = 0
        if not self.__alunos:
            print("Não há nenhum aluno cadastrado.")
        for __alunos in self.__alunos:
            index += 1
            print(
                f"{index}-Nome: {__alunos.get_nome()}    Matricula: {__alunos.get_matricula()}")

    def atualiza_aluno(self, aluno: Aluno_normal):
        for index in self.__alunos:
            if index.matricula == aluno.matricula:
                index.nome = aluno.nome
                index.matricula = aluno.matricula

    def exclui_aluno(self, matricula: str):
        self.__alunos.pop(self.__alunos.index(self.aluno_por_matricula(matricula)))

    def aluno_por_matricula(self, matricula):
        for aln in self.__alunos:
            if matricula == aln.get_matricula():
                return aln
        print("Nenhum aluno encontrado!")
        return

    def finalizar(self):
        sys.exit(0)

    def getalunos(self):
        return self.__alunos

    def tela_aluno(self):
        Tela_aluno.tela_aluno.menu_aluno()
