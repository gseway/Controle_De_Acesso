import PySimpleGUI as sg
from Controladores import ctrl_alunoPresidente


class TelaPresidente:
    layout_menu = [
        [sg.Text("Menu Presidente")],
        [sg.ReadButton('Alunos'), sg.ReadButton('Presidente'), sg.ReadButton('Entrar')],
        sg.ReadButton('Sair')
    ]
    layout_presidente = [
        [sg.Text("Menu Presidente")],
        [sg.ReadButton("Cadastrar Presidente"), sg.ReadButton("Listar Presidentes")],
        [sg.ReadButton("Excluir Presidente"), sg.ReadButton("Editar Presidente")],
    ]
    window = sg.Window("Gerenciar presidente", default_button_element_size=(15, 1),
                       auto_size_buttons=False, grab_anywhere=False).Layout(layout_presidente)
    button, values = window.Read()
