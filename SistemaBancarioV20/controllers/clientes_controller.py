from utils import user_functions
from views.clientes_view import iniciar, incluir
from layouts.layouts_telas import operacoes_disponiveis
from utils.user_functions import exibir_mensagem

class ClienteController:
    def __init__(self):
        pass

    def iniciar(self):
        while True:
            opcao = iniciar()
            if opcao == "R":
                break
            if opcao not in operacoes_disponiveis:
                exibir_mensagem(f"Opção inválida! Escolha uma das disponíveis: {operacoes_disponiveis}!")
                continue
            if opcao == "I":
                incluir()
                
                
