from database.banco import Banco
from models.conta import Conta
from models.tiposenum import TipoConta, StatusConta
from utils.userfunctions import exibir_mensagem, esperar_tecla, limpar_linha, limpar_tela, exibir_conteudo, desenhar_tela
from layouts.layouts import layout_cadastro_contas, titulo_telas, opcoes_disponiveis, operacoes_disponiveis

class ContasView:
    def __init__(self, banco: Banco):
        self.banco = banco

    def iniciar(self):
        limpar_tela()
        desenhar_tela(layout_cadastro_contas)
        exibir_conteudo(titulo_telas["cadastro_contas"], lin=4, col=2)
        
        while True:
            limpar_linha()
            exibir_conteudo(opcoes_disponiveis["cadastro_contas"], lin=30, col=2)
            opcao = esperar_tecla()
            if opcao == 'R':
                break
            if opcao not in operacoes_disponiveis["cadastro_contas"]:
                exibir_mensagem("Opção inválida! Pressione qualquer tecla para continuar.", col=2, wait_key=True)
                continue
            if opcao == 'C':
                continue
            elif opcao == 'I':
                continue
            elif opcao == 'A':
                continue
            elif opcao == 'E':
                continue
            elif opcao == 'L':
                continue
        
        limpar_tela()
        limpar_linha()