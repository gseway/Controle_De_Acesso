import sys
from Entidades.aluno_presidente import AlunoPresidente
from Telas.tela_presidente import TelaPresidente
from Enum.enum_tipoAluno import TipoAluno
from datetime import date
from Entidades.relatorio_acesso import RelatorioAcesso


class CtrlAlunoPresidente:

    def __init__(self):
        presidente_admin = AlunoPresidente("Douglas", "17202184", TipoAluno.ALUNO_PRESIDENTE, "11269734911",
                                           "douglasazambuja@hotmail.com", "12345")
        self.__presidentes = [presidente_admin]
        self.__relatorios = []

    def inclui_presidente(self, novo_presidente: AlunoPresidente):
        # percorre a lista de presidentes para verificar se o novo já é existente, comparando o cpf
        if len(self.__presidentes) == 5:
            print(
                "Não é possível inserir mais um presidente pois todas as vagas já estão preenchidas. Exclua algum existente")
            return

        for presidente in self.__presidentes:
            if presidente.matricula == novo_presidente.matricula:
                # se existir um presidente com a mesmo cpf, retorna None e para o loop
                print("Já existe um presidente com esta matricula")
                return

        for presidente in self.__presidentes:
            if presidente.cpf == novo_presidente.cpf:
                # se existir um presidente com a mesmo cpf, retorna None e para o loop
                print("Já existe um presidente com este cpf")
                return
        self.__presidentes.append(novo_presidente)
        with open("presidentes.txt", "a") as outfile:
            outfile.write(str(novo_presidente))

    def lista_presidentes(self):
        with open("presidentes.txt", "r") as infile:
            if not infile:
                print("Não há nenhum presidente cadastrado!")
            print(infile.read())

    def atualiza_presidente(self, presidente_att: AlunoPresidente):
        with open("presidentes.txt", "r") as infile:
            lines = infile.readlines()


        cpfs = [pres.cpf for pres in self.__presidentes]
        if presidente_att.cpf not in cpfs:
            print("Presidente não consta na lista.")
            return

        pres_index = cpfs.index(presidente_att.cpf)
        self.__presidentes[pres_index] = presidente_att
        print(f"Presidente nº {pres_index + 1} atualizado.")

    def exclui_presidente(self, cpf: str):
        with open("presidentes.txt", "r") as infile:
            lines = infile.readlines()
        with open("presidentes.txt", "w") as infile:
            for line in lines:
                if str(cpf) not in line:
                    infile.write(line)

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
        # abri no modo "a" de append, que vai adicionar no fim do arquivo
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

    def tela_presidente(self):
        TelaPresidente.menu_principal()
