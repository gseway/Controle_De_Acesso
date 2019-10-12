import sys
# from Modelos import Aluno_presidente
from Modelos.Aluno_presidente import AlunoPresidente

class Ctrl_alunoPresidente:

    def __init__(self):
        self.__presidentes = []

    def inclui_presidente(self, novo_presidente: AlunoPresidente):
        # percorre a lista de presidentes para verificar se o novo já é existente, comparando matricula e cpf
        if len(self.__presidentes) == 5:
            print("Não é possível inserir mais um presidente pois todas as vagas já estão preenchidas. Exclua algum existente")
            return
        for presidente in self.__presidentes:
            if presidente.get_cpf() == novo_presidente.get_cpf():
                # se existir um presidente com a mesmo cpf, retorna None e para o loop
                print("Já existe um presidente com este cpf")
                return
        self.__presidentes.append(novo_presidente)

    def lista_presidentes(self):
        index = 0
        if not self.__presidentes:
            print("Não há nenhum presidente cadastrado.")
        for presidente in self.__presidentes:
            index += 1
            print(f"{index}-Nome: {presidente.get_nome()}    Matricula: {presidente.get_matricula()}    CPF: {presidente.get_cpf()}    email: {presidente.get_email()}")

    def atualiza_presidente(self, presidente: AlunoPresidente):
        for index in self.__presidentes:
            if index.cpf == presidente.cpf:
                index.nome = presidente.nome
                index.matricula = presidente.matricula
                index.cpf = presidente.cpf
                index.email = presidente.email

    def exclui_presidente(self, cpf: str):
        self.__presidentes.pop(self.__presidentes.index(self.presidente_por_cpf(cpf)))

    def presidente_por_cpf(self, cpf):
        for pres in self.__presidentes:
            if cpf == pres.get_cpf():
                return pres
        print("Nenhum presidente foi encontrado!")
        return

    def finalizar(self):
        sys.exit(0)