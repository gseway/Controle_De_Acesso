import PySimpleGUI as sg
from Controladores import ctrl_aluno
from Controladores import ctrl_alunoPresidente


class TelaAluno:
    def menu_aluno(self):
        layout_aluno = [
            [sg.Text("Menu Aluno")],
            [sg.ReadButton("Criar", key='Criar'), sg.ReadButton("Listar", key='Listar')],
            [sg.ReadButton("Editar", key='Editar'), sg.ReadButton("Excluir", key='Excluir')],
            [sg.Text("    "), sg.ReadButton("Voltar", key='Voltar')]
        ]
        window = sg.Window("Gerenciar Aluno").Layout(layout_aluno)
        event, valor = window.Read()

    def cadastrar_aluno(self):
        layout_criar = [
            [sg.Text("Cadastrar aluno")],
            [sg.Text('Nome', size=(15, 1)), sg.InputText('', key='nome', size=(15, 1))],
            [sg.Text('Matricula', size=(15, 1)), sg.InputText('', key='matricula', size=(15, 1))],
            [sg.Text('CPF', size=(15, 1)), sg.InputText('', key='cpf', size=(15, 1))],
            [sg.Text('Senha', size=(15, 1)), sg.InputText('', key='senha', size=(15, 1))],
            [sg.Submit("Cadastrar"), sg.Cancel("Voltar")]
        ]
        window = sg.Window("Gerenciar Aluno").Layout(layout_criar)
        event, valor = window.Read()

    def excluir_aluno(self):
        layout_excluir = [
            [sg.Text("Excluir aluno")],
            [sg.Text('Matricula', size=(15, 1)), sg.InputText('', key='matricula', size=(15, 1))],
            [sg.Submit("Excluir"), sg.Cancel("Voltar")]
        ]
        window = sg.Window("Gerenciar Aluno").Layout(layout_excluir)
        event, valor = window.Read()

    def seleciona_aluno(self):
        layout_seleciona = [
            [sg.Text("Selecione o aluno")],
            [sg.Text('Matricula', size=(15, 1)), sg.InputText('', key='matricula', size=(15, 1))],
            [sg.Submit("Editar"), sg.Cancel("Voltar")]
        ]
        window = sg.Window("Gerenciar Aluno").Layout(layout_seleciona)
        event, valor = window.Read()

    def editar_aluno(self):
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
