from database.banco import Banco
from models.cliente import Cliente
from models.tiposenum import TipoPessoa, StatusCliente, estados
#from utils.userfunctions import date_to_iso, formatar_data, formatar_cpf_cnpj, formatar_telefone, formatar_cep
from utils.userfunctions import exibir_mensagem, esperar_tecla, limpar_linha, limpar_tela, exibir_conteudo, desenhar_tela, posicionar_cursor
from utils import userfunctions
from layouts.layouts import layout_cadastro_clientes, layout_consulta_cliente, titulo_telas, layout_opcoes_consultas, opcoes_disponiveis, operacoes_disponiveis

class ClientesView:
    _tipo_consulta = 1

    def __init__(self, banco: Banco):
        self.banco = banco

    def limpar_opcoes(self):
        info = layout_opcoes_consultas["consulta_cliente"]
        for key, value in info.__dict__.items():
            if key == "lin":
                lin = value
                continue
            exibir_conteudo(" ", lin, value)

    def obter_tipo_consulta(self):
        info = layout_opcoes_consultas["consulta_cliente"]
        fl_cancelar = False
        while True:
            exibir_mensagem("Selecione o tipo de pesquisa pressionanado X or R para cancelar a consulta")
            for key, value in info.items:
                if key == "lin":
                    lin = value
                    continue
                exibir_conteudo("•", lin, value)
                escolha = esperar_tecla()
                if escolha == "R":
                    fl_cancelar = True
                    break
                if escolha != "X":
                    exibir_conteudo(" ", lin, value)
                    self._tipo_consulta += 1
                    if self._tipo_consulta > 4:
                        self._tipo_consulta = 1
                    continue
                else:
                    break
            if escolha == "X" or fl_cancelar:
                break
            exibir_mensagem("Você precisa escolher uma opção. Tente novamente!", wait_key=True)
            limpar_linha()
        
        return fl_cancelar

    def digitar_argumento(self):
        if self._tipo_consulta == 1:
            help = "Digite o nome ou parte do nome do cliente"
        elif self._tipo_consulta == 2:
            help = "Digite o CPF ou CNPJ para consulta"
        elif self._tipo_consulta == 3:
            help = "Digite o nome da cidade para consulta"
        else:
            help = "Digite a data de nascimento/fundação"
        help += "  ou FIM para cancelar"

        while True:
            exibir_mensagem(help)
            posicionar_cursor(4, 71)
            argumento = input().upper()
            fl_ok = True
            if self._tipo_consulta == 2:
                fl_ok, mensagem = userfunctions.validar_cpf_cnpj(argumento)
            elif self._tipo_consulta == 4:
                fl_ok, mensagem = userfunctions.validar_data(argumento)
            if not fl_ok:
                exibir_mensagem(mensagem, wait_key=True)
                limpar_linha()
                continue
            break
        return fl_ok, argumento

    def consultar_clientes(self):
        limpar_tela()
        desenhar_tela(layout_consulta_cliente, 8, 28)
        exibir_conteudo(titulo_telas["consulta_cliente"], 2, 2)
        exibir_conteudo(opcoes_disponiveis["opcao_consultas"])

        while True:
            self.limpar_opcoes()
            fl_cancelar = self.obter_tipo_consulta(self)
            if fl_cancelar:
                break
            fl_ok, argumento = self.digitar_argumento()
            break
        if fl_cancelar:
            return
        
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
                exibir_mensagem("Opcão em desenvolvimento!", wait_key=True)
                continue
            elif opcao == 'I':
                exibir_mensagem("Opcão em desenvolvimento!", wait_key=True)
                continue
            elif opcao == 'A':
                exibir_mensagem("Opcão em desenvolvimento!", wait_key=True)
                continue
            elif opcao == 'E':
                exibir_mensagem("Opcão em desenvolvimento!", wait_key=True)
                continue
            elif opcao == 'L':
                exibir_mensagem("Opcão em desenvolvimento!", wait_key=True)
                continue
        
        limpar_tela()
        limpar_linha()