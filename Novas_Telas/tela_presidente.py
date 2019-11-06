import PySimpleGUI as sg


class TelaPresidente:
    layout_aluno = [
        [sg.Text("Menu Presidente")],
        [sg.ReadButton("Criar"), sg.ReadButton("Listar")],
        [sg.ReadButton("Editar"), sg.ReadButton("Excluir")],
        [sg.Text("    "), sg.ReadButton("Voltar")]
    ]

    window = sg.Window("Gerenciar Aluno", default_button_element_size=(6, 1),
                       auto_size_buttons=False, grab_anywhere=False).Layout(layout_aluno)
    button, values = window.Read()
