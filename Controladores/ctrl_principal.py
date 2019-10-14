from Telas import Tela_principal
from Controladores import ctrl_alunoPresidente
from Controladores import ctrl_aluno


class ctrl_Principal:

    def login_presidente(self, usuario, senha):

        if usuario in ctrl_alunoPresidente.Ctrl_alunoPresidente.getPresidentes(self):
            ctrl_alunoPresidente.Tela_presidente.Tela_presidente.menu_principal()

    def login_aluno(self, usuario, senha):
        if usuario in ctrl_aluno.Aluno_normal.Aluno_normal.getAlunos() and ctrl_aluno.Aluno_normal.Aluno_normal.getAlunos(
                usuario):
            Tela_principal.Tela_Principal.login_efetuado()
        else:
            Tela_principal.Tela_Principal.falha_login()
