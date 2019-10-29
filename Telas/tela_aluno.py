from Controladores.ctrl_de_dados import CtrlDeDados
from Enum.enum_tipoAluno import TipoAluno
from Controladores.ctrl_aluno import Ctrl_aluno
from Entidades.aluno_normal import Aluno_normal



class TelaAluno:
    def __init__(self):
        self.__crtl_aluno = Ctrl_aluno()
        self.__crtl_dados = CtrlDeDados()

    def menu_aluno(self):
        print(" ________________________________________________________________")
        print("|-------------------------Menu do Aluno--------------------------|")
        print("|0 - Finalizar Programa                                          |")
        print("|1 - Incluir um aluno                                            |")
        print("|2 - Listar alunos                                               |")
        print("|3 - Atualizar um aluno                                          |")
        print("|4 - Excluir um aluno                                            |")
        print("|5 - Voltar para tela presidente                                 |")
        print("|________________________________________________________________|")
        switcher = {
            0: self.tela_finaliza,
            1: self.tela_inclui_aluno,
            2: self.tela_lista_aluno,
            3: self.tela_atualiza_aluno,
            4: self.tela_exclui_aluno,
            5: self.retorna_tela_presidente}
        while True:
            try:
                    opcao = int(input("Digite a opção desejada: "))
                    opcao_escolhida = switcher[opcao]
                    opcao_escolhida()
            except ValueError:
                print("Insira um valor válido!")

    def tela_inclui_aluno(self):
        print("Digite os dados do novo aluno:")
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

        senha = self.__crtl_dados.gera_senha()
        aluno = Aluno_normal(nome, matricula, TipoAluno.ALUNO_PRESIDENTE, cpf, senha)
        self.__crtl_aluno.inclui_aluno(aluno)
        print("Sua senha foi gerada automaticamente \nAnote para não esquecer: " + senha)

    def tela_lista_aluno(self):
        print("Lista de alunos:")
        self.__crtl_aluno.lista_alunos()

    def tela_atualiza_aluno(self):
        TelaAluno.tela_lista_aluno(self)

        pass

    def tela_exclui_aluno(self):
        TelaAluno.tela_lista_aluno(self)

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
        from Telas.tela_presidente import TelaPresidente
        menu_presidente = TelaPresidente().menu_principal()
        return menu_presidente
