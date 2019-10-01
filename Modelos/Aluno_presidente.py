from Pesssoa import Pessoa
import Enum_tipoAluno

Class Aluno_presidente(Pessoa):

    __init__(self, nome: str, matricula: int, tipo_aluno: tipo_aluno, cpf: int, email: str):
        super()__init__(nome, matricula, tipo_pessoa)
        self.__cpf = cpf
        self.__email = email
        
    @property 
    def get_cpf(self):
        return self.__cpf
    
    @property 
    def get_email(self):
        return self.__email

    @cpf.setter
    def set_cpf(self, cpf):
        self.__cpf = cpf
    
    @email.setter
    def set_matricula(self, email):
        self.__email = email
       