import PySimpleGUI as sg
from Controladores import ctrl_principal


class TelaPrincipal:

    login_principal = [
        [sg.Text("Controle de Acesso ao CASIN")],
        [sg.InputText("Matricula", size=(15, 1), do_not_clear=True, justification='left', key='matricula')],
        [sg.InputText("Senha", size=(15, 1), do_not_clear=True, justification='left',key='senha')],
        [sg.ReadButton('1'), sg.ReadButton('2'), sg.ReadButton('3')],
        [sg.ReadButton('4'), sg.ReadButton('5'), sg.ReadButton('6')],
        [sg.ReadButton('7'), sg.ReadButton('8'), sg.ReadButton('9')],
        [sg.ReadButton('Entrar'), sg.ReadButton('0'), sg.ReadButton('Limpar')]
    ]
    login_presidente = [
        [sg.Text("Controle de Acesso ao CASIN")],
        [sg.InputText("CPF", size=(15, 1), do_not_clear=True, justification='left',
                      key='cpf')],
        [sg.InputText("Senha", size=(15, 1), do_not_clear=True, justification='left',
                      key='senha')],
    ]
    window = sg.Window("Controle de Acesso", default_button_element_size=(5, 2),
                       auto_size_buttons=False, grab_anywhere=False).Layout(login_principal)

    botoes_matricula = ''
    botoes_senha = ''
    while True:
        button, values = window.Read()
        if button is None:
            break
        if button == 'Limpar':
            botoes_matricula = ''
        elif button in '1234567890':
            botoes_matricula = values['matricula']
            botoes_matricula += button
        elif button == 'Entrar':
            botoes_matricula = values['matricula']
            # valor da matricula para o controlador
