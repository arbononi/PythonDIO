from utils import user_functions
from utils.user_functions import limpar_linha, exibir_mensagem
from views.transacoes_view import iniciar

opcao_limite = 8

class TransacaoController:
    def __init__(self):
        pass

    def iniciar(self):
        while True:
            opcao = iniciar()
            if opcao == 9:
                break
            elif (opcao < 1 or opcao > 8) and opcao != 9:
                exibir_mensagem(f" Opção inválida! Escolha entre 1 o {opcao_limite}!")
                continue