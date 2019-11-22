import PySimpleGUI as sg
from switch import Switch
from Controladores import ctrl_alunoPresidente


class TelaPresidente:

    def __init__(self):
        self.__ctrlPresidente = ctrl_alunoPresidente

    def menupresidente(self):
        layout_presidente = [
            [sg.Text("Menu Presidente")],
            [sg.ReadButton("Cadastrar Presidente"), sg.ReadButton("Listar Presidentes")],
            [sg.ReadButton("Excluir Presidente"), sg.ReadButton("Editar Presidente")],
        ]
        window = sg.Window("Gerenciar presidente", default_button_element_size=(15, 1),
                           auto_size_buttons=False, grab_anywhere=False).Layout(layout_presidente)
        botao, valor = window.Read()
        with Switch(valor) as case:
            if case('Criar'):
                self.cadastrar_presidente()
            if case('Editar'):
                self.cadastrar_presidente()
            if case('Excluir'):
                self.cadastrar_presidente()
            if case('Listar'):
                self.cadastrar_presidente()

    def cadastrar_presidente(self):
        layout_criar = [
            [sg.Text("Cadastrar aluno")],
            [sg.Text('Nome', size=(15, 1)), sg.InputText('', key='nome', size=(15, 1))],
            [sg.Text('Matricula', size=(15, 1)), sg.InputText('', key='matricula', size=(15, 1))],
            [sg.Text('CPF', size=(15, 1)), sg.InputText('', key='cpf', size=(15, 1))],
            [sg.Text('Senha', size=(15, 1)), sg.InputText('', key='senha', size=(15, 1))],
            [sg.ReadButton("Cadastrar"), sg.ReadButton("Voltar")]
        ]
        window = sg.Window("Gerenciar Aluno").Layout(layout_criar)
        event, valor = window.Read()
        with Switch(valor) as case:
            if case('Cadastrar'):
                nome = valor['nome']
                matricula = valor['matricula']
                cpf = valor['cpf']
                senha = valor['senha']
                self.__ctrlPresidente.inclui_presidente(self.__ctrlPresidente, nome, matricula, cpf, senha)

            if case('Voltar'):
                TelaPresidente.menupresidente(self)

    def excluir_presidente(self):
        layout_excluir = [
            [sg.Text("Excluir aluno")],
            [sg.Text('Matricula', size=(15, 1)), sg.InputText('', key='matricula', size=(15, 1))],
            [sg.Submit("Excluir"), sg.Cancel("Voltar")]
        ]
        window = sg.Window("Gerenciar Aluno").Layout(layout_excluir)
        event, valor = window.Read()

    def seleciona_presidente(self):
        layout_seleciona = [
            [sg.Text("Selecione o aluno")],
            [sg.Text('Matricula', size=(15, 1)), sg.InputText('', key='matricula', size=(15, 1))],
            [sg.Submit("Editar"), sg.Cancel("Voltar")]
        ]
        window = sg.Window("Gerenciar Aluno").Layout(layout_seleciona)
        event, valor = window.Read()

    def editar_presidente(self):
        layout_editar = [
            [sg.Text("Editar aluno")],
            [sg.Text('Nome', size=(15, 1)), sg.InputText('', key='nome', size=(15, 1))],
            [sg.Text('Matricula', size=(15, 1)), sg.InputText('', key='matricula', size=(15, 1))],
            [sg.Text('CPF', size=(15, 1)), sg.InputText('', key='cpf', size=(15, 1))],
            [sg.Text('Senha', size=(15, 1)), sg.InputText('', key='senha', size=(15, 1))],
            [sg.Submit("Salvar"), sg.Cancel("Voltar")]
        ]
        window = sg.Window("Gerenciar Aluno").Layout(layout_editar)
        event, valor = window.Read()