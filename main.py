from Entidades.aluno_presidente import AlunoPresidente
from Controladores.ctrl_alunoPresidente import CtrlAlunoPresidente
from Enum.enum_tipoAluno import TipoAluno
from Telas.tela_principal import TelaPrincipal
from Telas.tela_presidente import TelaPresidente


def main():
    #presida = AlunoPresidente("noemee", 17202184, TipoAluno.ALUNO_PRESIDENTE, '12345678912', "email@com.")
    #presida2 = AlunoPresidente("noemee", 17202184, TipoAluno.ALUNO_PRESIDENTE, '12345678916', "email@com.")
    #presida1 = AlunoPresidente("noemee", 17202184, TipoAluno.ALUNO_PRESIDENTE, '12345678914', "email@com.")
    # presida2 = AlunoPresidente("noemee", 17202184, tipo_Aluno.ALUNO_PRESIDENTE, '112697349111', "email@com.")
    # presida_novo = AlunoPresidente("nome_teste", 17202000, tipo_Aluno.ALUNO_PRESIDENTE, '11269734911', "douglas@hotmail.com")
    controlador = CtrlAlunoPresidente()
    #controlador.inclui_presidente(presida)
    #controlador.inclui_presidente(presida2)
    #controlador.inclui_presidente(presida1)
    # controlador.inclui_presidente(presida2)

    tela1 = TelaPrincipal()
    tela1.tela_inicial()
    #controlador.lista_presidentes()
    #tela2 = TelaPresidente()
    #tela2.menu_principal()

if __name__ == '__main__':
    main()
