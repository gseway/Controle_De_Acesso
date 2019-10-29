from random import randrange

class CtrlDeDados:

    def __init__(self):
        pass

    def verifica_matricula(self, matricula: str):
        if not matricula or len(matricula) < 8 or len(matricula) > 8:
            return False

        if not matricula.isdigit():
            return False

        return True

    def verifica_cpf(self, cpf: str):
        if not cpf or len(cpf) < 11 or len(cpf) > 11:
            return False

        if not cpf.isdigit():
            return False

        return True

    def gera_senha(self):
        senha = ""
        for i in range(5):
            i = str(randrange(0, 10))
            senha += i
        return senha

