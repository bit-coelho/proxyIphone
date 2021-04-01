import PySimpleGUI as gui

class TelaPython:
    def __init__(self):
        layout = [
            [gui.Text("Nome:", size=(5, 0)), gui.Input(size=(15, 0), key="name")],
            [gui.Button("OK")]
        ]

        self.janela = gui.Window("Dados do Usuário").layout(layout)

    def iniciar(self):
        self.button, self.values = self.janela.Read()
        name = self.values["name"]
        return name

