from database.banco import Banco
from models.transacao import Transacao
from layouts.layouts import layout_menu_transacoes, titulo_telas, opcoes_disponiveis, operacoes_disponiveis
from utils.userfunctions import limpar_linha, limpar_tela, desenhar_tela, exibir_conteudo, exibir_mensagem, posicionar_cursor, esperar_tecla

class TransacoesView():
    def __init__(self, banco: Banco):
        self.banco = banco

    def iniciar(self):
        limpar_tela()
        desenhar_tela(layout_menu_transacoes)
        exibir_conteudo(titulo_telas["menu_transacoes"], lin=4, col=2)
        while True:
            try:
                limpar_linha()
                exibir_conteudo(opcoes_disponiveis["menu_transacoes"], lin=30, col=3)
                opcao = int(esperar_tecla())
                if opcao == 9:
                    break
                if opcao not in operacoes_disponiveis["menu_transacoes"]:
                    exibir_mensagem("Opção inválida! Tente novamente!", wait_key=True)
                    continue
                if opcao == 1:
                    exibir_mensagem("Opção em desenvolvimento!!!", wait_key=True)
                    continue
                elif opcao == 2:
                    exibir_mensagem("Opção em desenvolvimento!!!", wait_key=True)
                    continue
                elif opcao == 3:
                    exibir_mensagem("Opção em desenvolvimento!!!", wait_key=True)
                    continue
                elif opcao == 4:
                    exibir_mensagem("Opção em desenvolvimento!!!", wait_key=True)
                    continue
                elif opcao == 5:
                    exibir_mensagem("Opção em desenvolvimento!!!", wait_key=True)
                    continue
                else:
                    exibir_mensagem("Opção em desenvolvimento!!!", wait_key=True)
                    continue
            except ValueError:
                exibir_mensagem("Opção inválida! Tente novamente!", wait_key=True)
                continue

        limpar_tela()
        limpar_linha()