from Telas import Tela_principal
from Controladores import ctrl_alunoPresidente
from Controladores import Ctrl_aluno

class Ctrl_Principal:

    def login_presidente(self):
        ctrl_alunoPresidente.Tela_presidente.Tela_presidente.menu_principal()
    
    def login_aluno(self):
        Ctrl_aluno