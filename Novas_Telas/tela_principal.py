import PySimpleGUI as sg
from switch import Switch
from Controladores.ctrl_principal import CtrlPrincipal


class TelaPrincipal:

    def __init__(self):
        self.__ctrl_principal = CtrlPrincipal()

    def entrar(self):
        login_principal = [
            [sg.Text("Controle de Acesso ao CASIN")],
            [sg.Text('Matricula'),
             sg.InputText(size=(15, 1), do_not_clear=True, justification='left', key='matricula')],
            [sg.Text('Matricula'), sg.InputText(size=(15, 1), do_not_clear=True, justification='left', key='senha')],
            [sg.ReadButton('Entrar'), sg.ReadButton('Sair')]
        ]
        login = sg.Window("Controle de Acesso", default_button_element_size=(5, 2),
                          auto_size_buttons=False, grab_anywhere=False).Layout(login_principal)
        event, valor = login.Read()
        with Switch(valor) as case:
            if case('Entrar'):
                matricula = valor['matricula']
                senha = valor['senha']
                CtrlPrincipal.login(self.__ctrl_principal, matricula, senha)

            if case('Sair'):
                CtrlPrincipal.finalizar(self.__ctrl_principal)

    def menuescolha(self):
        layout_menu = [
            [sg.Text("Menu Presidente")],
            [sg.ReadButton('Alunos'), sg.ReadButton('Presidente'), sg.ReadButton('Entrar')],
            sg.ReadButton('Sair')

        ]
        window = sg.Window("Gerenciar presidente", default_button_element_size=(15, 1),
                           auto_size_buttons=False, grab_anywhere=False).Layout(layout_menu)
        event, valor = window.Read()
        with Switch(valor) as case:
            if case('Alunos'):
                CtrlPrincipal.tela_aluno(self.__ctrl_principal)
            if case('Presidente'):
                CtrlPrincipal.tela_presidente(self.__ctrl_principal)
            if case('Entrar'):
                sg.popup('Entrada Liberada')
