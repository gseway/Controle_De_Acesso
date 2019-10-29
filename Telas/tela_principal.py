from Controladores.ctrl_principal import CtrlPrincipal
from Controladores.ctrl_alunoPresidente import AlunoPresidente
from Controladores.ctrl_de_dados import CtrlDeDados

class TelaPrincipal:

    def __init__(self):
        self.__ctrl_principal = CtrlPrincipal()
        self.__ctrl_dados = CtrlDeDados()

    def tela_inicial(self):
        print(" ________________________________________________________________")
        print("|Controle de Acesso Ao Centro Acadêmico de Sistemas de Informação|")
        print("|________________________________________________________________|")
        self.tela_login()

    def tela_login(self):
        while True:
            matricula = str(input("Matricula: "))
            senha = str(input("Digite sua senha: "))
            self.__ctrl_principal.login(matricula, senha)

    def login_efetuado(self):
        print("Login efetuado! Bem vindo!")

    def falha_login(self):
        print("Login incorreto ou bloqueado pelo presidente!")
