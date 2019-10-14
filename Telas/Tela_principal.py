import sys
from Controladores import ctrl_principal


class Tela_Principal:

    def __init__(self):
        pass

    def tela_inicial(self):
        print("Login CASIN")
        status = input("Voce é aluno ou presidente? aperte 0 para sair")
        if status == "aluno":
            self.tela_login_aluno()
        elif status == "presidente":
            self.tela_login_presidente()
        elif status == "0":
            sys.exit(0)

    def tela_login_presidente(self):
        usuario = input("Digite seu usuario")
        senha = input("Digite sua senha")
        ctrl_principal.ctrl_Principal.login_presidente(usuario, senha)

    def tela_login_aluno(self):
        usuario = input("Digite seu usuario")
        senha = input("Digite sua senha")
        ctrl_principal.ctrl_Principal.login_aluno(usuario, senha)

    def login_efetuado(self):
        print("Login efetuado, entre")

    def falha_login(self):
        print("Login incorreto ou bloqueado pelo presidente")
