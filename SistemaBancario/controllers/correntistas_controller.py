import msvcrt
from utils import user_functions
from models.correntista import Correntista
from views.telas_sistema import layout_correntistas
from views.correntistas_view import iniciar, novo_cadastro, alterar_cadastro
from models.tiposenum import TipoOperacao as status_cad
from utils.user_functions import MOSTRAR_CURSOR, OCULTAR_CURSOR

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
                print(OCULTAR_CURSOR)
                msvcrt.getch()
                print(MOSTRAR_CURSOR)
                user_functions.limpar_linha(30, 2, 98)
                continue
            if opcao == "R":
                break
            if opcao == "N":
                novo_cadastro()
            elif opcao == "A":
                alterar_cadastro()