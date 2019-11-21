import sys
from Entidades.aluno_presidente import AlunoPresidente
from Novas_Telas.tela_presidente import TelaPresidente
from Enum.enum_tipoAluno import TipoAluno
from datetime import date
from Excecoes.excecao_controlador import *
from DAO.presidenteDAO import PresidenteDAO
from Entidades.relatorio_acesso import RelatorioAcesso


class CtrlAlunoPresidente:
    __instance = None

    def __init__(self):
        self.__tela_presidente = TelaPresidente
        presidente_admin = AlunoPresidente("Douglas", "17202184", TipoAluno.ALUNO_PRESIDENTE, "11269734911",
                                           "douglasazambuja@hotmail.com", "12345")
        self.__presidente_dao = PresidenteDAO()
        self.__presidentes = [presidente_admin]
        self.__relatorios = []

    def __new__(cls):
        if CtrlAlunoPresidente.__instance is None:
            CtrlAlunoPresidente.__instance = object.__new__(cls)
        return CtrlAlunoPresidente.__instance

    def inclui_presidente(self, novo_presidente: AlunoPresidente):
        # percorre a lista de presidentes para verificar se o novo já é existente, comparando o cpf
        try:
            if len(self.__presidentes) == 5:
                raise lista_usuario_cheia

            for presidente in self.__presidentes:
                if presidente.matricula == novo_presidente.matricula:
                    raise usuario_existente

            for presidente in self.__presidentes:
                if presidente.cpf == novo_presidente.cpf:
                    raise usuario_existente

            self.presidentes.append(novo_presidente)
            self.__presidente_dao.add(novo_presidente.matricula, novo_presidente)

        except lista_usuario_cheia:
            print("Não é possível inserir mais um presidente pois todas as vagas já estão preenchidas.")

        except usuario_existente:
            print("CPF ou matricula já existente.")

    def lista_presidentes(self):
        self.__presidente_dao.get_all()

    def atualiza_presidente(self, presidente_att: AlunoPresidente):

        try:
            self.__presidente_dao.remove(presidente_att.matricula)
            self.__presidente_dao.add(presidente_att.matricula, presidente_att)

        except IndexError:
            print("Não há nenhum presidente com essa matrícula")
        except




        with open("presidentes.txt", "r") as infile:
            lines = infile.readlines()

        cpfs = [pres.cpf for pres in self.__presidentes]

        if presidente_att.cpf not in cpfs:
            print("Presidente não consta na lista.")
            return

        pres_index = cpfs.index(presidente_att.cpf)
        self.__presidentes[pres_index] = presidente_att
        print(f"Presidente nº {pres_index + 1} atualizado.")

    def exclui_presidente(self, matricula: str):
        try:
            self.__presidente_dao.remove(matricula)
        except IndexError:
            print("Não há nenhum presidente com essa matrícula")

    def presidente_por_cpf(self, cpf):
        # abri no modo "r" de read, que vai puxar todas a linhas do arquivo
        with open("presidentes.txt", "r") as infile:
            lines = infile.readlines()
            infile.seek(0)
            for line in lines:
                if str(cpf) in line:
                    return line
        print("Nenhum presidente foi encontrado!")
        return

    def add_relatorio_acesso(self, novo_relatorio: RelatorioAcesso):
        self.__relatorios.append(novo_relatorio)
        # ao abrir o arquivo com context manager (with), o arquivo se fecha sozinho ao sair do escopo da função, ou seja, não precisa dar close
        # abrir no modo "a" de append, que vai adicionar no fim do arquivo
        with open("relatorio_acesso.txt", "a") as outfile:
            outfile.write(str(novo_relatorio))

    def lista_relatorio_acesso(self):
        # abrindo arquivo no modo "r" para read
        with open("relatorio_acesso.txt", "r") as infile:
            print(infile.read())

    def finalizar(self):
        sys.exit(0)

    @property
    def presidentes(self):
        return self.__presidentes

    @property
    def relatorios(self):
        return self.__relatorios

    def abre_menu(self):
        TelaPresidente.layout_menu()
