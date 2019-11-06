import PySimpleGUI as sg


class TelaPrincipal:
    login_principal = [
        [sg.Text("Controle de Acesso ao CASIN")],
        [sg.InputText("Matricula",size=(15, 1), do_not_clear=True, justification='left',
                  key='input')],
        [sg.InputText("Senha", size=(15, 1), do_not_clear=True, justification='left',
                      key='input')],
        [sg.ReadButton("1"), sg.ReadButton("2"), sg.ReadButton("3")],
        [sg.ReadButton("4"), sg.ReadButton("5"), sg.ReadButton("6")],
        [sg.ReadButton("7"), sg.ReadButton("8"), sg.ReadButton("9")],
        [sg.ReadButton("Entrar"), sg.ReadButton("0"), sg.ReadButton("Limpar")]
    ]
    window = sg.Window("Controle de Acesso", default_button_element_size=(5, 2),
                       auto_size_buttons=False, grab_anywhere=False).Layout(login_principal)
    while True:
        button, values = window.Read()