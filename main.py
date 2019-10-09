from Modelos.aluno_presidente import AlunoPresidente
from Controladores.Ctrl_alunoPresidente import CtrlAlunoPessoa
from Enum.enum_tipoAluno import TipoAluno

def main():
    presida = AlunoPresidente("noemee", 17202184, TipoAluno.ALUNO_PRESIDENTE, 11269734911, "email@com.")
    controlador = CtrlAlunoPessoa().inclui_presidente(presida())


if __name__ == '__main__':
    main()
