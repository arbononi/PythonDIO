from Utils import user_functions
from Views.Correntista_View import iniciar, novo_cadastro, alterar_cadastro, excluir_cadastro, consultar_cadastro, visualizar_relatorio
from Models.Correntista import Correntista

opcoes_disponiveis = [ "N", "A", "E", "C", "L", "R" ]

class ConrrentistasController:
    def __init__(self):
        pass

    def iniciar(self):
        while True:
            opcao = iniciar()
            if opcao not in opcoes_disponiveis:
                user_functions.limpar_linha(30, 2, 98)
                user_functions.exibirMensagem(30, 3, f"Opção inválida! Escolha uma entre {opcoes_disponiveis}")
                user_functions.esperar_tecla()
                user_functions.limpar_linha(30, 2, 98)
                continue
            if opcao == "R":
                break
            if opcao == "N":
                novo_cadastro()
            elif opcao == "A":
                alterar_cadastro()
            elif opcao == "E":
                excluir_cadastro()
            elif opcao == "C":
                consultar_cadastro()
            elif opcao == "L":
                visualizar_relatorio()