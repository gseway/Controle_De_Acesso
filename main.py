from Modelos.Aluno_presidente import AlunoPresidente
from Controladores.ctrl_alunoPresidente import Ctrl_alunoPresidente
from Enum.enum_tipoAluno import tipo_Aluno
from Telas.Tela_presidente import Tela_presidente

def main():
    presida = AlunoPresidente("noemee", 17202184, tipo_Aluno.ALUNO_PRESIDENTE, '11269734911', "email@com.")
    #presida2 = AlunoPresidente("noemee", 17202184, tipo_Aluno.ALUNO_PRESIDENTE, '112697349111', "email@com.")
    #presida_novo = AlunoPresidente("nome_teste", 17202000, tipo_Aluno.ALUNO_PRESIDENTE, '11269734911', "douglas@hotmail.com")
    controlador = Ctrl_alunoPresidente()
    controlador.inclui_presidente(presida)
    #controlador.inclui_presidente(presida2)
    #controlador.lista_presidentes()
    tela = Tela_presidente()
    tela.menu_principal()



if __name__ == '__main__':
    main()
