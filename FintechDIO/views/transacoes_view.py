from dataclasses import fields
from enum import Enum
from models.transacao import TransacaoDTO, ContaDTO
from models.tiposenum import TipoTransacao, TipoOperacao, TipoChavePix
from models.versao import Versao
from utils.userfunctions import exibir_mensagem, exibir_conteudo, esperar_tecla, limpar_linha, limpar_tela, desenhar_tela, posicionar_cursor
from utils.userfunctions import formatar_data, formatar_data_hora, formatar_valor
from layouts.layouts import layout_transacoes, titulo_telas, opcoes_disponiveis, operacoes_disponiveis, restaurar_linha_29

class TransacoesView:

    campos_transacao = {
        "tipo_transacao" : { "lin": 7, "size": 1, "deposito": 4, "saque": 22, "pix": 37, "pagamento": 50, "transferencia" : 69, "doc": 92 },
        "id_conta_origem" : { "lin": 9, "col": 21, "size": 10, "mensagem": "Informe a conta de onde sairá o dinheiro ou 9 para cancelar" },
        "cpf_cnpj_origem" : { "lin": 9, "col": 33, "size": 18},
        "nome_cliente_origem" : { "lin": 9, "col": 53, "size": 45 },
        "id_conta_destino" : { "lin": 11, "col": 21, "size": 10, "mensagem": "Informe a conta para onde irá o dinheiro ou 9 para cancelar" },
        "cpf_cnpj_destino" : { "lin": 11, "col": 33, "size": 18},
        "nome_cliente_destino" : { "lin": 11, "col": 53, "size": 45 },
        "tipo_chave_pix" : { "lin": 13, "size" : 1, "cpf": 21, "cnpj": 34, "telefone": 48, "email": 66, "chave_aleatoria": 81, "mensagem": "Escolha o tipo de chave para o PIX digitando: F, J, T, E, A ou S para sair" },
        "chave_pix" : { "lin": 15, "col": 21, "size": 77, "mensagem": "Informe a chave pix para esta operação ou FIM para cancelar" },
        "linha_digitavel" : { "lin": 17, "col": 21, "size": 77, "mensagem": "Informe a linha digitável (Pagamento) ou No. Documento (DOC) ou FIM para cancelar" },
        "valor_operacao" : { "lin": 19, "col": 21, "size": 14, "mensagem": "Informe o valor da operação ou 0 para cancelar" },
        "nome_autor" : { "lin": 19, "col": 53, "size": 45, "mensagem": "Informe o nome do autor da operação ou FIM para cancelar" },
        "mensagem_opcional" : { "lin": 21, "col": 21, "size": 77, "mensagem": "Digite alguma mensagem para o destinatário ou FIM para cancelar" }
    }

    def __init__(self):
        pass

    def limpar_campos(self, desativada=False):
        for key, info in self.campos_transacao.items():
            if key == "tipo_transacao":
                    exibir_conteudo("_", info["lin"], info["deposito"], desativada)
                    exibir_conteudo("_", info["lin"], info["saque"], desativada)
                    exibir_conteudo("_", info["lin"], info["pix"], desativada)
                    exibir_conteudo("_", info["lin"], info["pagamento"], desativada)
                    exibir_conteudo("_", info["lin"], info["transferencia"], desativada)
                    exibir_conteudo("_", info["lin"], info["doc"], desativada)
            elif key == "tipo_chave_pix":
                    exibir_conteudo("_", info["lin"], info["cpf"], desativada)
                    exibir_conteudo("_", info["lin"], info["cnpj"], desativada)
                    exibir_conteudo("_", info["lin"], info["telefone"], desativada)
                    exibir_conteudo("_", info["lin"], info["email"], desativada)
                    exibir_conteudo("_", info["lin"], info["chave_aleatoria"], desativada)
            else:
                exibir_conteudo("_" * info['size'], info["lin"], info["col"], desativada)
    
    def habilitar_campos(self, tipo_transacao: TipoTransacao):
        info_valor_operacao = self.campos_transacao["valor_operacao"]
        info_nome_autor = self.campos_transacao["nome_autor"]
        info_mensagem_opcional = self.campos_transacao["mensagem_opcional"]
        exibir_conteudo("_" * info_valor_operacao["size"], info_valor_operacao["lin"], info_valor_operacao["col"])
        exibir_conteudo("_" * info_nome_autor["size"], info_nome_autor["lin"], info_nome_autor["col"])
        exibir_conteudo("_" * info_mensagem_opcional["size"], info_mensagem_opcional["lin"], info_mensagem_opcional["col"])
        match tipo_transacao:
            case TipoTransacao.DEPOSITO:
                info_conta_destino = self.campos_transacao["id_conta_destino"]
                exibir_conteudo("_" * info_conta_destino["size"], info_conta_destino["lin"], info_conta_destino["col"])
            case TipoTransacao.SAQUE:
                info_conta_origem = self.campos_transacao["id_conta_origem"]
                exibir_conteudo("_" * info_conta_origem["size"], info_conta_origem["lin"], info_conta_origem["col"])
            case TipoTransacao.PIX:
                info_conta_origem = self.campos_transacao["id_conta_origem"]
                info_tipo_chave_pix = self.campos_transacao["tipo_chave_pix"]
                info_chave_pix = self.campos_transacao["chave_pix"]
                exibir_conteudo("_" * info_conta_origem["size"], info_conta_origem["lin"], info_conta_origem["col"])
                exibir_conteudo("_" * info_tipo_chave_pix["size"], info_tipo_chave_pix["lin"], info_tipo_chave_pix["cpf"])
                exibir_conteudo("_" * info_tipo_chave_pix["size"], info_tipo_chave_pix["lin"], info_tipo_chave_pix["cnpj"])
                exibir_conteudo("_" * info_tipo_chave_pix["size"], info_tipo_chave_pix["lin"], info_tipo_chave_pix["telefone"])
                exibir_conteudo("_" * info_tipo_chave_pix["size"], info_tipo_chave_pix["lin"], info_tipo_chave_pix["email"])
                exibir_conteudo("_" * info_tipo_chave_pix["size"], info_tipo_chave_pix["lin"], info_tipo_chave_pix["chave_aleatoria"])
                exibir_conteudo("_" * info_chave_pix["size"], info_chave_pix["lin"], info_chave_pix["col"])
            case TipoTransacao.PAGAMENTO:
                info_conta_origem = self.campos_transacao["id_conta_origem"]
                info_linha_digitavel = self.campos_transacao["linha_digitavel"]
                exibir_conteudo("_" * info_conta_origem["size"], info_conta_origem["lin"], info_conta_origem["col"])
                exibir_conteudo("_" * info_linha_digitavel["size"], info_linha_digitavel["lin"], info_linha_digitavel["col"])
            case TipoTransacao.TRANSFERENCIA:
                info_conta_origem = self.campos_transacao["id_conta_origem"]
                info_conta_destino = self.campos_transacao["id_conta_destino"]
                exibir_conteudo("_" * info_conta_origem["size"], info_conta_origem["lin"], info_conta_origem["col"])
                exibir_conteudo("_" * info_conta_destino["size"], info_conta_destino["lin"], info_conta_destino["col"])
            case TipoTransacao.DOC:
                info_conta_destino = self.campos_transacao["id_conta_destino"]
                info_linha_digitavel = self.campos_transacao["linha_digitavel"]
                exibir_conteudo("_" * info_conta_destino["size"], info_conta_destino["lin"], info_conta_destino["col"])
                exibir_conteudo("_" * info_linha_digitavel["size"], info_linha_digitavel["lin"], info_linha_digitavel["col"])

    def setar_tipo_transacao(self, tipo_transacao: TipoTransacao):
        self.habilitar_campos(tipo_transacao)
        lin = self.campos_transacao["tipo_transacao"]["lin"]
        col = self.campos_transacao["tipo_transacao"][tipo_transacao.descricao]
        info = self.campos_transacao["tipo_transacao"]
        exibir_conteudo("•", lin, col)
        match tipo_transacao:
            case TipoTransacao.DEPOSITO:
                exibir_conteudo(" ", lin, info["saque"])
                exibir_conteudo(" ", lin, info["pix"])
                exibir_conteudo(" ", lin, info["pagamento"])
                exibir_conteudo(" ", lin, info["transferencia"])
                exibir_conteudo(" ", lin, info["doc"])
            case TipoTransacao.SAQUE:
                exibir_conteudo(" ", lin, info["deposito"])
                exibir_conteudo(" ", lin, info["pix"])
                exibir_conteudo(" ", lin, info["pagamento"])
                exibir_conteudo(" ", lin, info["transferencia"])
                exibir_conteudo(" ", lin, info["doc"])
            case TipoTransacao.PIX:
                exibir_conteudo(" ", lin, info["deposito"])
                exibir_conteudo(" ", lin, info["saque"])
                exibir_conteudo(" ", lin, info["pagamento"])
                exibir_conteudo(" ", lin, info["transferencia"])
                exibir_conteudo(" ", lin, info["doc"])
            case TipoTransacao.PAGAMENTO:
                exibir_conteudo(" ", lin, info["deposito"])
                exibir_conteudo(" ", lin, info["saque"])
                exibir_conteudo(" ", lin, info["pix"])
                exibir_conteudo(" ", lin, info["transferencia"])
                exibir_conteudo(" ", lin, info["doc"])
            case TipoTransacao.TRANSFERENCIA:
                exibir_conteudo(" ", lin, info["deposito"])
                exibir_conteudo(" ", lin, info["saque"])
                exibir_conteudo(" ", lin, info["pix"])
                exibir_conteudo(" ", lin, info["pagamento"])
                exibir_conteudo(" ", lin, info["doc"])
            case TipoTransacao.DOC:
                exibir_conteudo("Nº do Documento", lin=17)
                exibir_conteudo(" ", lin, info["deposito"])
                exibir_conteudo(" ", lin, info["saque"])
                exibir_conteudo(" ", lin, info["pix"])
                exibir_conteudo(" ", lin, info["pagamento"])
                exibir_conteudo(" ", lin, info["transferencia"])

    def setar_tipo_chave_pix(self, tipo_chave: TipoChavePix):
        info = self.campos_transacao["tipo_chave_pix"]
        lin = info["lin"]
        col = info[tipo_chave.descricao]
        exibir_conteudo("•", lin, col)

        match tipo_chave:
            case TipoChavePix.CPF:
                exibir_conteudo(" ", lin, info["cnpj"])
                exibir_conteudo(" ", lin, info["telefone"])
                exibir_conteudo(" ", lin, info["email"])
                exibir_conteudo(" ", lin, info["chave_aleatoria"])
            case TipoChavePix.CNPJ:
                exibir_conteudo(" ", lin, info["cpf"])
                exibir_conteudo(" ", lin, info["telefone"])
                exibir_conteudo(" ", lin, info["email"])
                exibir_conteudo(" ", lin, info["chave_aleatoria"])
            case TipoChavePix.TELEFONE:
                exibir_conteudo(" ", lin, info["cpf"])
                exibir_conteudo(" ", lin, info["cnpj"])
                exibir_conteudo(" ", lin, info["email"])
                exibir_conteudo(" ", lin, info["chave_aleatoria"])
            case TipoChavePix.EMAIL:
                exibir_conteudo(" ", lin, info["cpf"])
                exibir_conteudo(" ", lin, info["cnpj"])
                exibir_conteudo(" ", lin, info["telefone"])
                exibir_conteudo(" ", lin, info["chave_aleatoria"])
            case TipoChavePix.CHAVE_ALEATORIA:
                exibir_conteudo(" ", lin, info["cpf"])
                exibir_conteudo(" ", lin, info["cnpj"])
                exibir_conteudo(" ", lin, info["telefone"])
                exibir_conteudo(" ", lin, info["email"])

    def iniciar(self):
        limpar_tela()
        desenhar_tela(layout_transacoes)
        titulo_tela = titulo_telas["menu_principal"].replace(" - MENU PRINCIPAL", "").strip() + " - " + Versao.get_init_version().to_str()
        exibir_conteudo(titulo_tela.center(75, " "), lin=2, col=2)
        exibir_conteudo(titulo_telas["transacoes"], lin=4, col=2)
        posicionar_cursor(27, 2)
        while True:
            try:
                self.limpar_campos(True)
                limpar_linha()
                exibir_mensagem(opcoes_disponiveis["opcoes_transacao"], col=2)
                opcao = int(esperar_tecla())
                if opcao not in operacoes_disponiveis["operacoes_transacao"]:
                    exibir_mensagem("Opção Inválida! Tente Novamente", wait_key=True)
                    continue
                break
            except ValueError as error:
                exibir_mensagem("Opção inválida! Escolha apenas um número dentre os disponíveis", wait_key=True)

        return opcao