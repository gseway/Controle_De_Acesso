from Entidades.aluno_presidente import AlunoPresidente
from Enum.enum_tipoAluno import TipoAluno
from Telas.tela_aluno import TelaAluno


class TelaPresidente:
    def __init__(self):
        from Controladores.ctrl_alunoPresidente import CtrlAlunoPresidente
        from Controladores.ctrl_de_dados import CtrlDeDados
        self.__crtl_presidente = CtrlAlunoPresidente()
        self.__crtl_dados = CtrlDeDados()

    def menu_principal(self):
        print(" ________________________________________________________________")
        print("|----------------------Menu do Presidente------------------------|")
        print("|0 - Finalizar Programa                                          |")
        print("|1 - Incluir um Presidente                                       |")
        print("|2 - Listar Presidentes                                          |")
        print("|3 - Atualizar um Presidente                                     |")
        print("|4 - Excluir um Presidente                                       |")
        print("|5 - Relatório de Acesso                                         |")
        print("|6 - Gerenciar alunos                                            |")
        print("|________________________________________________________________|")
        switcher = {
            0: self.tela_finaliza,
            1: self.tela_inclui_presidente,
            2: self.tela_lista_presidente,
            3: self.tela_atualiza_presidente,
            4: self.tela_exclui_presidente,
            5: self.tela_relatorio,
            6: self.tela_aluno}
        while True:
            try:
                opcao = int(input("Digite a opção desejada: "))
                opcao_escolhida = switcher[opcao]
                opcao_escolhida()
            except ValueError:
                print("Digite um valor válido!")

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
        senha = self.__crtl_dados.gera_senha()
        presidente = AlunoPresidente(nome, matricula, TipoAluno.ALUNO_PRESIDENTE, cpf, email, senha)
        self.__crtl_presidente.inclui_presidente(presidente)
        print("Sua senha foi gerada automaticamente \nAnote para não esquecer: " + senha)

    def tela_lista_presidente(self):
        self.__crtl_presidente.lista_presidentes()

    def tela_atualiza_presidente(self):
        print("Digite o CPF do presidente que deseja alterar:")
        cpf = input("CPF: ")
        print("Digite os dados a serem atualizados:")
        nome = input("Nome: ")
        matricula = input("Matricula: ")
        email = input("email: ")
        self.__crtl_presidente.atualiza_presidente(AlunoPresidente(nome, matricula, TipoAluno.ALUNO_PRESIDENTE, cpf, email))

    def tela_exclui_presidente(self):
        print("Digite o CPF do presidente que deseja excluir")
        cpf = input("CPF: ")
        verifica = self.__crtl_dados.verifica_cpf(cpf)
        while not verifica:
            print("Digite um cpf válido")
            cpf_dnv = str(input("CPF: "))
            verifica = self.__crtl_dados.verifica_cpf(cpf_dnv)
        self.__crtl_presidente.exclui_presidente(cpf)
        print("Presidente excluído com sucesso!")

    def tela_relatorio(self):
        print("Relatório de Acesso")
        self.__crtl_presidente.lista_relatorio_acesso()

    def tela_finaliza(self):
        self.__crtl_presidente.finalizar()

    def tela_aluno(self):
        menu_aluno = TelaAluno().menu_aluno()
        return menu_aluno