from utils import user_functions
from views.contas_view import iniciar
from layouts.layouts_telas import operacoes_disponiveis

class ContaController:
    def __init__(self):
        pass

    def iniciar(self):
        while True:
            opcao = iniciar()
            if opcao == "R":
                break