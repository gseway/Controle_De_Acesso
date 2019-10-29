from Telas.tela_presidente import TelaPresidente
from Controladores.ctrl_alunoPresidente import CtrlAlunoPresidente
from Controladores.ctrl_aluno import Ctrl_aluno
from Telas.tela_aluno import TelaAluno
from datetime import date
from Entidades.relatorio_acesso import RelatorioAcesso


class CtrlPrincipal:

    def __init__(self):
        self.__ctrl_presidente = CtrlAlunoPresidente()
        self.__ctrl_aluno = Ctrl_aluno()
        self.__tela_presidente = TelaPresidente()
        self.__tela_aluno = TelaAluno()

    def login(self, matricula: str, senha: str):
        with open("presidentes.txt", "r") as infile:
            lines = infile.readlines()
            for line in lines:
                if matricula and senha in line:
                    #relatorio = RelatorioAcesso(pres.nome, pres.cpf, date.today())
                    #self.__ctrl_presidente.add_relatorio_acesso(relatorio)
                    self.__tela_presidente.menu_principal()

        #for pres in self.__ctrl_presidente.presidentes:
        #    if pres.matricula == matricula and pres.senha == senha:
        #        relatorio = RelatorioAcesso(pres.nome, pres.cpf, date.today())
        #        self.__ctrl_presidente.add_relatorio_acesso(relatorio)
        #        self.__tela_presidente.menu_principal()

        for aluno in self.__ctrl_aluno.alunos:
            if aluno.matricula == matricula and aluno.senha == senha:
                relatorio = RelatorioAcesso(aluno.nome, aluno.cpf, aluno.today())
                self.__ctrl_presidente.add_relatorio_acesso(relatorio)
                self.__tela_aluno.menu_aluno()
        return