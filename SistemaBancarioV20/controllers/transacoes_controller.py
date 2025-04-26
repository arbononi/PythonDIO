from utils import user_functions
from utils.user_functions import limpar_linha, exibir_mensagem
from views.transacoes_view import iniciar, depositar, sacar, transferir, efetuar_pix, enviar_doc, efetuar_pagamentos

opcao_limite = 6

class TransacaoController:
    def __init__(self):
        pass

    def iniciar(self):
        while True:
            opcao = iniciar()
            if opcao == 9:
                break
            if (opcao < 1 or opcao > opcao_limite) and opcao != 9:
               exibir_mensagem(f" Opção inválida! Escolha entre 1 o {opcao_limite}!")
               continue
            if opcao == 1:
                depositar()
            elif opcao == 2:
                sacar()
            elif opcao == 3:
                transferir()
            elif opcao == 4:
                efetuar_pix()
            elif opcao == 5:
                enviar_doc()
            elif opcao == 6:
                efetuar_pagamentos()
