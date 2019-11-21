import PySimpleGUI as sg
from Controladores import ctrl_principal
from Controladores.ctrl_principal import CtrlPrincipal


class TelaPrincipal:
    ctrl_presidente = CtrlPrincipal()

    def entrar(self):
        login_principal = [
            [sg.Text("Controle de Acesso ao CASIN")],
            [sg.Text('Matricula'),
             sg.InputText(size=(15, 1), do_not_clear=True, justification='left', key='matricula')],
            [sg.Text('Matricula'), sg.InputText(size=(15, 1), do_not_clear=True, justification='left', key='senha')],
            [sg.Submit('Entrar'), sg.ReadButton('0'), sg.ReadButton('Sair')]
        ]
        login = sg.Window("Controle de Acesso", default_button_element_size=(5, 2),
                          auto_size_buttons=False, grab_anywhere=False).Layout(login_principal)
        event, valor = login.Read()
        while True:
            if event is None or valor == 'Sair':
                 break
            elif event == 'Entrar' and valor is not None:
                matricula = valor['matricula']
                senha = valor['senha']
                ctrl_principal.CtrlPrincipal.login(CtrlPrincipal, matricula, senha)
