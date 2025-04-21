from Utils.user_functions import exibirMensagem, limpar_linha, esperar_tecla
from Views.ContaCorrente_View import iniciar, novo_cadastro, alterear_cadastro, visualizar_cadastro, visualizar_relatorio
from Models.ContaCorrente import ContaCorrente

opcoes_disponiveis = [ "N", "A", "E", "C", "L", "R" ]

class ContaCorrentesController:
    def __init__(self):
        pass
    
    def iniciar(self):
        while True:
            opcao = iniciar()
            if opcao == "R":
                break
            if opcao not in opcoes_disponiveis:
                exibirMensagem(30, 3, f"Opção inválida! Escolha entre {opcoes_disponiveis}.")
                esperar_tecla()
                limpar_linha()
                continue
            if opcao == "N":
                novo_cadastro()
            elif opcao == "A":
                alterear_cadastro()
            elif opcao == "C":
                visualizar_cadastro()
            elif opcao == "L":
                visualizar_relatorio()