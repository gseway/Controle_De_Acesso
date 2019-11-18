import PySimpleGUI as sg
from Controladores import ctrl_aluno


class TelaAluno:
    layout_aluno = [
        [sg.Text("Menu Aluno")],
        [sg.ReadButton("Criar"), sg.ReadButton("Listar")],
        [sg.ReadButton("Editar"), sg.ReadButton("Excluir")],
        [sg.Text("    "), sg.ReadButton("Voltar")]
    ]

    layout_criar = [
        [sg.Text("Cadastrar aluno")],
        [sg.Text('Nome', size=(15, 1)), sg.InputText('', key='nome', size=(15, 1))],
        [sg.Text('Matricula', size=(15, 1)), sg.InputText('', key='matricula', size=(15, 1))],
        [sg.Text('CPF', size=(15, 1)), sg.InputText('', key='cpf', size=(15, 1))],
        [sg.Text('Senha', size=(15, 1)), sg.InputText('', key='senha', size=(15, 1))],
        [sg.Submit("Cadastrar"), sg.Cancel("Sair")]
    ]

    layout_excluir = [
        [sg.Text("Excluir aluno")],
        [sg.Text('Matricula', size=(15, 1)), sg.InputText('', key='matricula', size=(15, 1))],
        [sg.Submit("Excluir"), sg.Cancel("Sair")]
    ]

    layout_seleciona = [
        [sg.Text("Selecione o aluno")],
        [sg.Text('Matricula', size=(15, 1)), sg.InputText('', key='matricula', size=(15, 1))],
        [sg.Submit("Editar"), sg.Cancel("Sair")]
    ]

    layout_editar= [
        [sg.Text("Editar aluno")],
        [sg.Text('Nome', size=(15, 1)), sg.InputText('', key='nome', size=(15, 1))],
        [sg.Text('Matricula', size=(15, 1)), sg.InputText('', key='matricula', size=(15, 1))],
        [sg.Text('CPF', size=(15, 1)), sg.InputText('', key='cpf', size=(15, 1))],
        [sg.Text('Senha', size=(15, 1)), sg.InputText('', key='senha', size=(15, 1))],
        [sg.Submit("Salvar"), sg.Cancel("Sair")]
    ]

    window = sg.Window("Gerenciar Aluno", default_button_element_size=(7, 1),
                       auto_size_buttons=False, grab_anywhere=False).Layout(layout_editar)
    button, values = window.Read()
