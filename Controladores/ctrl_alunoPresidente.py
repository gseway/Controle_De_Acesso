from Modelos.aluno_presidente import AlunoPresidente


class CtrlAlunoPessoa:

  def __init__(self, presidente: AlunoPresidente):
    self.__presidente = presidente
    self.__presidentes = []

  def get_presidente(self):
    return self.__presidente

  def set_presidente(self, presidente):
    self.__presidente = presidente

  def inclui_presidente(self, novo_presidente: AlunoPresidente):
    #percorre a lista de presidentes para verificar se o novo já é existente, comparando matricula e cpf
    for presidente in self.__presidentes:
      if (presidente.cpf == novo_presidente.cpf):
        #se existir um presidente com a mesmo cpf, retorna None e para o loop
        return
    self.__presidentes.append(novo_presidente)
    return novo_presidente

  def lista_presidentes(self):
    if not self.__presidentes:
      print("Não há nenhum presidente cadastrado.")
    for presidente in self.__presidentes:
      print(f"Nome: {presidente.nome} Matricula: {presidente.matricula} CPF: {presidente.cpf} email: {presidente.email}")

  def atualiza_presidente(self, presidente: AlunoPresidente):
    for i in self.__presidentes:
      if i.cpf == presidente.cpf:
        index = self.__presidentes.index(i)
        break
    self.__presidentes.insert(index, presidente)

  def exclui_presidente(self, matricula: int):
    #criar função para verificar matricula
    for aluno in self.__presidentes:
      if aluno.matricula == matricula:
        self.__presidentes.remove(aluno)

  def finalizar(self):
    exit(0)
