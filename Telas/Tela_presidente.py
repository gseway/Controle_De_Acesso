from Controladores.ctrl_alunoPresidente import Ctrl_alunoPresidente
from Controladores.ctrl_de_dados import CtrlDeDados
from Modelos.Aluno_presidente import AlunoPresidente
from Enum.enum_tipoAluno import tipo_Aluno
from Telas import Tela_aluno


class Tela_presidente:
    def __init__(self):
        self.__crtl_presidente = Ctrl_alunoPresidente()
        self.__crtl_dados = CtrlDeDados()

    def menu_principal(self):
        print("0 - Finalizar Programa")
        print("1 - Incluir um Presidente   |")
        print("2 - Listar Presidentes      |")
        print("3 - Atualizar um Presidente |")
        print("4 - Excluir um Presidente   |")
        print("5 - Gerenciar alunos        |")
        switcher = {
            0: self.tela_finaliza,
            1: self.tela_inclui_presidente,
            2: self.tela_lista_presidente,
            3: self.tela_atualiza_presidente,
            4: self.tela_exclui_presidente,
            5: self.tela_aluno}
        while True:
            opcao = int(input("Digite a opção desejada: "))
            opcao_escolhida = switcher[opcao]
            opcao_escolhida()

    def tela_inclui_presidente(self):
        print("Digite os dados do novo presidente:")
        nome = str(input("Nome: "))

        matricula = str(input("Matricula: "))
        verifica_matricula = self.__crtl_dados.verifica_matricula(matricula)
        while not verifica_matricula:
            print("Digite uma matricula válida")
            matricula = matricula_dnv = str(input("Matricula: "))
            verifica_matricula = self.__crtl_dados.verifica_matricula(matricula_dnv)

        cpf = str(input("CPF: "))
        verifica_cpf = self.__crtl_dados.verifica_cpf(cpf)
        while not verifica_cpf:
            print("Digite um cpf válido")
            cpf = cpf_dnv = str(input("CPF: "))
            verifica_cpf = self.__crtl_dados.verifica_cpf(cpf_dnv)

        email = str(input("email: "))
        presidente = AlunoPresidente(nome, matricula, tipo_Aluno.ALUNO_PRESIDENTE, cpf, email)
        self.__crtl_presidente.inclui_presidente(presidente)

    def tela_lista_presidente(self):
        print("Lista de presidentes:")
        self.__crtl_presidente.lista_presidentes()

    def tela_atualiza_presidente(self):
        pass

    def tela_exclui_presidente(self):
        print("Digite o CPF do presidente que deseja excluir")
        cpf = input("CPF: ")
        verifica = self.__crtl_dados.verifica_cpf(cpf)
        while not verifica:
            print("Digite um cpf válido")
            cpf_dnv = str(input("CPF: "))
            verifica = self.__crtl_dados.verifica_cpf(cpf_dnv)
        self.__crtl_presidente.exclui_presidente(cpf)

    def tela_finaliza(self):
        self.__crtl_presidente.finalizar()

    def tela_aluno(self):
        Tela_aluno.tela_aluno.menu_aluno()
