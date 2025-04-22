from utils.user_functions import exibirMensagem, limpar_linha, esperar_tecla
from views.transacao_view import iniciar, nova_transacao, visualizar_relatorio

opcoes_disponiveis = [ "N", "A", "E", "C", "L", "R" ]

class TransacaoController:
    def __init__(self):
        pass

    def iniciar(self):
        while True:
            opcao = iniciar()
            if opcao == "R":
                break
            if opcao not in opcoes_disponiveis:
                exibirMensagem(30, 3, f"Opção inválida! Entre entre {opcoes_disponiveis}!!")
                esperar_tecla()
                limpar_linha()
                continue
            if opcao == "N":
                nova_transacao()
            elif opcao == "L":
                visualizar_relatorio()
