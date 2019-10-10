from Modelos import Aluno_presidente


class Ctrl_alunoPresidente:

    def __init__(self, presidente: Aluno_presidente):
        self.__presidente = presidente
        self.__presidentes = []

    def get_presidente(self):
        return self.__presidente

    def set_presidente(self, presidente):
        self.__presidente = presidente

    def inclui_presidente(self, novo_presidente: Aluno_presidente):
        # percorre a lista de presidentes para verificar se o novo já é existente, comparando matricula e cpf
        for presidente in self.__presidentes:
            if presidente.cpf == novo_presidente.cpf:
                # se existir um presidente com a mesmo cpf, retorna None e para o loop
                return
        self.__presidentes.append(novo_presidente)
        return novo_presidente

    def atualiza_presidente(self, presidente: Aluno_presidente):
     for i in self.__presidentes:
        if i.cpf == presidente.cpf:
         index = self.__presidentes.index(i)

        self.__presidentes.insert(index, presidente)


    def exclui_presidente(self, matricula: int):
#criar função para verificar matricula
     for aluno in self.__presidentes:
        if aluno.matricula == matricula:
     self.__presidentes.remove(aluno)

  def finalizar(self):
    exit(0)

    def atualiza_presidente(self):
        pass

    def exclui_presidente(self):
        pass

    def finalizar(self):
        exit(0)
