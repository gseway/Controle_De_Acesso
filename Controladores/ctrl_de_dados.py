from random import randrange


class CtrlDeDados:
    __instance = None

    def __init__(self):
        pass

    def __new__(cls):
        if CtrlDeDados.__instance is None:
            CtrlDeDados.__instance = object.__new__(cls)
        return CtrlDeDados.__instance

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
