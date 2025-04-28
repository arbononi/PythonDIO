from database.banco import Banco
from views import contas_view, clientes_view, transacoes_view
from layouts.layouts import layout_menu_consultas, titulo_telas, opcoes_disponiveis
from utils.userfunctions import limpar_tela, limpar_linha, exibir_conteudo, exibir_mensagem, esperar_tecla, desenhar_tela, posicionar_cursor

class ConsultasController:
    def __init__(self, banco: Banco):
        self.banco = banco

    
    def iniciar(self):
        limpar_tela()
        desenhar_tela(layout_menu_consultas)
        exibir_conteudo(titulo_telas["menu_consultas"], 4, 2)

        clientesview = clientes_view.ClientesView(self.banco)
        contasview = contas_view.ContasView(self.banco)
        transacaoview = transacoes_view.TransacoesView(self.banco)
        
        while True:
            try:
                limpar_linha()
                exibir_conteudo(opcoes_disponiveis["menu_consultas"], 30, 3)
                opcao = int(esperar_tecla())
                if opcao == 9:
                    break
                if (opcao < 1 or opcao > 4) or opcao != 9:
                    exibir_mensagem("Opçãoe inválida! Tente novamente!", wait_key=True)
                    continue
                if opcao == 1:
                    exibir_mensagem("Opção em desenvolvimento", wait_key=True)
                    continue
                elif opcao == 2:
                    exibir_mensagem("Opção em desenvolvimento", wait_key=True)
                    continue
                elif opcao == 3:
                    exibir_mensagem("Opção em desenvolvimento", wait_key=True)
                    continue
                elif opcao == 4:
                    exibir_mensagem("Opção em desenvolvimento", wait_key=True)
                    continue
            except ValueError:
                exibir_mensagem("Opção inválida! Tente novamente!", wait_key=True)
        



