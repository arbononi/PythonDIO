from database.banco import Banco
from models.cliente import Cliente
from models.tiposenum import TipoPessoa, StatusCliente, estados
#from utils.userfunctions import date_to_iso, formatar_data, formatar_cpf_cnpj, formatar_telefone, formatar_cep
from utils.userfunctions import exibir_mensagem, esperar_tecla, limpar_linha, limpar_tela, exibir_conteudo, desenhar_tela
from layouts.layouts import layout_cadastro_clientes, titulo_telas, opcoes_disponiveis, operacoes_disponiveis

class ClientesView:
    def __init__(self, banco: Banco):
        self.banco = banco

    def iniciar(self):
        limpar_tela()
        desenhar_tela(layout_cadastro_clientes)
        exibir_conteudo(titulo_telas["cadastro_clientes"], lin=4, col=2)
        
        while True:
            limpar_linha()
            exibir_conteudo(opcoes_disponiveis["cadastro_clientes"], lin=30, col=2)
            opcao = esperar_tecla()
            if opcao == 'R':
                break
            if opcao not in operacoes_disponiveis["cadastro_clientes"]:
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