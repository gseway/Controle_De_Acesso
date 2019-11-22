from Entidades.relatorio_acesso import RelatorioAcesso
from Controladores.ctrl_alunoPresidente import CtrlAlunoPresidente
from Controladores.ctrl_aluno import Ctrl_aluno
from Novas_Telas.tela_principal import TelaPrincipal
import sys


class CtrlPrincipal:
    __instance = None

    def __init__(self):
        self.__tela_principal = TelaPrincipal
        self.__ctrl_presidente = CtrlAlunoPresidente()
        self.__ctrl_aluno = Ctrl_aluno()

    def __new__(cls):
        if CtrlPrincipal.__instance is None:
            CtrlPrincipal.__instance = object.__new__(cls)
        return CtrlPrincipal.__instance

    def login(self, matricula: str, senha: str):
        with open("presidentes.txt", "r") as infile:
            lines = infile.readlines()
            for line in lines:
                if matricula and senha in line:
                    # relatorio = RelatorioAcesso(pres.nome, pres.cpf, date.today())
                    # self.__ctrl_presidente.add_relatorio_acesso(relatorio)
                    self.__tela_principal.menuescolha(self.__tela_principal)

        for aluno in self.__ctrl_aluno.alunos:
            if aluno.matricula == matricula and aluno.senha == senha:
                relatorio = RelatorioAcesso(aluno.nome, aluno.cpf, aluno.today())
                self.__ctrl_presidente.add_relatorio_acesso(relatorio)
                self.__ctrl_aluno.tela_aluno()
        return

    def tela_aluno(self):
        Ctrl_aluno.tela_aluno(self.__ctrl_aluno)

    def tela_presidente(self):
        CtrlAlunoPresidente.tela_presidente(self.__ctrl_presidente)

    def finalizar(self):
        sys.exit(0)
