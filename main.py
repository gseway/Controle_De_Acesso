from Modelos import Aluno_presidente
from Controladores import ctrl_alunoPresidente
from Enum.enum_tipoAluno import tipo_Aluno
from Modelos import Pessoa


def main():
    presida = Pessoa.Aluno_presidente("noemee", 17202184, tipo_Aluno.ALUNO_PRESIDENTE, 11269734911, "email@com.")
    ctrl_alunoPresidente().inclui_presidente(presida())


if __name__ == '__main__':
    main()
