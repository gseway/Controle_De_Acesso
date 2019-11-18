import sys
from Entidades.aluno_normal import Aluno_normal
from Enum.enum_tipoAluno import TipoAluno
from Novas_Telas.tela_aluno import TelaAluno

class Ctrl_aluno:
    __instance = None

    def __init__(self):
        aluno = Aluno_normal("Douglas", "17202185", TipoAluno.ALUNO_PRESIDENTE, "11269734913", "12345")
        self.__alunos = [aluno]

    def __new__(cls):
        if Ctrl_aluno.__instance is None:
            Ctrl_aluno.__instance = object.__new__(cls)
            return Ctrl_aluno.__instance

    def inclui_aluno(self, novo_aluno: Aluno_normal):
        for aluno in self.__alunos:
            if aluno.matricula == novo_aluno:
                # se existir um aluno com a mesma matricula, retorna None e para o loop
                print("Já existe um aluno com essa matricula")
                return
        self.__alunos.append(novo_aluno)
        with open("alunos.txt", "a") as outfile:
            outfile.write(str(novo_aluno))

    def lista_alunos(self):
        if not self.__alunos:
            print("Não há nenhum aluno cadastrado.")
        # for index, __alunos in enumerate(self.__alunos):
        #    print(
        #        f"{index}-Nome: {__alunos.nome}    Matricula: {__alunos.matricula}    CPF {__alunos.cpf}")
        with open("alunos.txt", "r") as infile:
            print(infile.read())

    def atualiza_aluno(self, aluno_att: Aluno_normal):
        matriculas = [aluno.matricula for aluno in self.__alunos]
        if aluno_att.matricula not in matriculas:
            print("Presidente não consta na lista.")
            return

        aluno_index = matriculas.index(aluno_att.matricula)
        self.__alunos[aluno_index] = aluno_att
        print(f"Aluno nº {aluno_index + 1} atualizado.")

    def exclui_aluno(self, matricula: str):
        self.__alunos.pop(self.__alunos.index(self.aluno_por_matricula(matricula)))

    def aluno_por_matricula(self, matricula):
        for aln in self.__alunos:
            if matricula == aln.matricula:
                return aln
        print("Nenhum aluno encontrado!")
        return

    def finalizar(self):
        sys.exit(0)

    @property
    def alunos(self):
        return self.__alunos

    def tela_aluno(self):
        TelaAluno.layout_aluno()
