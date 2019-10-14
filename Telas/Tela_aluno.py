from Controladores.ctrl_de_dados import CtrlDeDados
from Enum.enum_tipoAluno import tipo_Aluno
from Telas import Tela_presidente
from Controladores import ctrl_aluno
from Modelos import Aluno_normal


class tela_aluno:
    def __init__(self):
        self.__crtl_aluno = ctrl_aluno()
        self.__crtl_dados = CtrlDeDados()

    def menu_aluno(self):
        print("0 - Finalizar Programa")
        print("1 - Incluir um aluno            |")
        print("2 - Listar alunos               |")
        print("3 - Atualizar um aluno          |")
        print("4 - Excluir um aluno            |")
        print("5 - Voltar para tela presidente |")
        switcher = {
            0: self.tela_finaliza,
            1: self.tela_inclui_aluno,
            2: self.tela_lista_aluno,
            3: self.tela_atualiza_aluno,
            4: self.tela_exclui_aluno,
            5: self.retorna_tela_presidente}
        while True:
            opcao = int(input("Digite uma opção valida: "))
            opcao_escolhida = switcher[opcao]
            opcao_escolhida()

    def tela_inclui_aluno(self):
        print("Digite os dados do novo aluno:")
        nome = str(input("Nome: "))

        matricula = str(input("Matricula: "))
        verifica_matricula = self.__crtl_dados.verifica_matricula(matricula)
        while not verifica_matricula:
            print("Digite uma matricula válida")
            matricula = matricula_dnv = str(input("Matricula: "))
            verifica_matricula = self.__crtl_dados.verifica_matricula(matricula_dnv)

        aluno = Aluno_normal(nome, matricula, tipo_Aluno.ALUNO_NORMAL)
        self.__crtl_aluno.inclui_aluno(aluno)

    def tela_lista_aluno(self):
        print("Lista de alunos:")
        self.__crtl_aluno.lista_alunos()

    def tela_atualiza_aluno(self):
        tela_aluno.tela_lista_aluno(self)

        pass

    def tela_exclui_aluno(self):
        tela_aluno.tela_lista_aluno(self)

        print("Digite a matricula do aluno que deseja excluir")
        matricula = input("Matricula: ")
        verifica = self.__crtl_dados.verifica_matricula(matricula)
        while not verifica:
            print("Digite uma matricula válida")
            matricula_dnv = str(input("Matricula: "))
            verifica = self.__crtl_dados.verifica_matricula(matricula_dnv)
        self.__crtl_aluno.exclui_aluno(matricula)

    def tela_finaliza(self):
        self.__crtl_aluno.finalizar()

    def retorna_tela_presidente(self):
        Tela_presidente.Tela_presidente.menu_principal()
