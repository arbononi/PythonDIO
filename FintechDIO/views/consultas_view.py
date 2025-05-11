from layouts.layouts import layout_consultas, layout_consulta_saldo, titulo_telas, opcoes_disponiveis
from layouts.layouts import layout_consulta_extratos, operacoes_disponiveis
from utils.userfunctions import limpar_tela, desenhar_tela, exibir_conteudo, exibir_mensagem, esperar_tecla, posicionar_cursor
from utils.userfunctions import formatar_cpf_cnpj, formatar_valor, formatar_data_hora
from models.transacao import Transacao
from models.conta import ContaDTO
from models.versao import Versao
from models.tiposenum import TipoOperacao, TipoTransacao

class ConsultasView:
    _tipo_consulta = 0

    campos_consulta_saldo = {
        "id_conta" : { "lin" : 7, "col": 14, "size": 10, "mensagem": "Informe o número da conta ou 0 para sair" },
        "cpf_cnpj" : { "lin" : 7, "col": 26, "size": 18 },
        "nome_cliente" : { "lin": 7, "col": 46, "size": 52 },
        "saldo_atual": { "lin": 9, "col": 14, "size": 15 },
        "limite_especial" : { "lin": 9, "col": 52, "size": 14 },
        "saldo_disponivel": { "lin": 9, "col": 83, "size": 15 }
    }

    campos_consulta_extrato = {
        "id_conta": { "lin": 4, "col": 14, "size": 10, "mensagem": "Informe o número do conta ou 0 para sair" },
        "nome_cliente": { "lin": 4, "col": 26, "size": 32 },
        "data_inicial": { "lin": 4, "col": 73, "size": 10, "mensagem": "Informe a data inicial ou 0 para sair" },
        "data_final": { "lin": 4, "col": 88, "size": 10, "mensagem": "Informe a data final ou 0 para sair "}
    }

    colunas_relatorio_extrato = {
        "data_movto": { "col": 3, "size": 19 },
        "saldo_anterior": { "col": 25, "size": 15 },
        "valor_movto" : { "col": 43, "size": 14 },
        "saldo_final" : { "col": 60, "size": 15 },
        "tipo_transacao": { "col": 79, "size": 14 },
        "tipo_operacao": { "col": 96, "size": 3 }
    }

    def __init__(self):
        pass
    
    def limpar_campos_saldo(self):
        for key, value in self.campos_consulta_saldo.items():
            exibir_conteudo(" " * value["size"], value["lin"], value["col"], desativada = True if key != "id_conta" else False)

    def limpar_campos_extratos(self):
        for key, value in self.campos_consulta_extrato.items():
            exibir_conteudo(" " * value["size"], value["lin"], value["col"], desativada=True if key == "nome_cliente" else False)

    def desenhar_consulta_saldo(self):
        limpar_tela()
        desenhar_tela(layout_consulta_saldo)
        exibir_conteudo(titulo_telas["consulta_saldo"], lin=4, col=2)
        self.limpar_campos_saldo()

    def exibir_dados_conta(self, conta_dto: ContaDTO):
        info_id_conta = self.campos_consulta_saldo["id_conta"]
        size_conta = info_id_conta["size"]
        info_cpf_cliente = self.campos_consulta_saldo["cpf_cnpj"]
        size_cpf_cliente = info_cpf_cliente["size"]
        info_nome_cliente = self.campos_consulta_saldo["nome_cliente"]
        size_nome_cliente = info_nome_cliente["size"]
        lin_saldo_atual = self.campos_consulta_saldo["saldo_atual"]["lin"]
        col_saldo_atual = self.campos_consulta_saldo["saldo_atual"]["col"]
        size_saldo_atual = self.campos_consulta_saldo["saldo_atual"]["size"]
        lin_limite = self.campos_consulta_saldo["limite_especial"]["lin"]
        col_limite = self.campos_consulta_saldo["limite_especial"]["col"]
        size_limite = self.campos_consulta_saldo["limite_especial"]["size"]
        lin_disponivel = self.campos_consulta_saldo["saldo_disponivel"]["lin"]
        col_disponivel = self.campos_consulta_saldo["saldo_disponivel"]["col"]
        size_disponivel = self.campos_consulta_saldo["saldo_disponivel"]["size"]

        saldo_atual = formatar_valor(float(conta_dto.conta.saldo_atual))
        limite_especial = formatar_valor(float(conta_dto.conta.limite_especial))
        saldo_disponivel = formatar_valor(float(conta_dto.conta.saldo_disponivel))

        doc_formatado = ""
        if conta_dto.cpf_cnpj != "":
            _, doc_formatado = formatar_cpf_cnpj(conta_dto.cpf_cnpj)

        exibir_conteudo(str(conta_dto.conta.id).rjust(size_conta, " "), info_id_conta["lin"], info_id_conta["col"])
        exibir_conteudo(doc_formatado.rjust(size_cpf_cliente, " "), info_cpf_cliente["lin"], info_cpf_cliente["col"])
        exibir_conteudo(conta_dto.nome_cliente.ljust(size_nome_cliente, " "), info_nome_cliente["lin"], info_nome_cliente["col"])
        exibir_conteudo(saldo_atual.rjust(size_saldo_atual, " "), lin_saldo_atual, col_saldo_atual)
        exibir_conteudo(limite_especial.rjust(size_limite, " "), lin_limite, col_limite)
        exibir_conteudo(saldo_disponivel.rjust(size_disponivel, " "), lin_disponivel, col_disponivel)
        exibir_mensagem("Pressione Qualquer tecla para outra consulta!", wait_key=True)

    def desenhar_consulta_extratos(self):
        limpar_tela()
        desenhar_tela(layout_consulta_extratos, line_loop=8, stop_loop=28)
        exibir_conteudo(titulo_telas["consulta_extratos"], lin=2, col=2)
        exibir_mensagem(opcoes_disponiveis["opcoes_consultas"], col=2)
        self.limpar_campos_extratos()

    def exibir_dados_extratos(self, transacoes: list[Transacao], id_conta:int):
        lin = 7
        col_data_movto = self.colunas_relatorio_extrato["data_movto"]["col"]
        col_saldo_anterior = self.colunas_relatorio_extrato["saldo_anterior"]["col"]
        size_saldo_anterior = self.colunas_relatorio_extrato["saldo_anterior"]["size"]
        col_valor_movto = self.colunas_relatorio_extrato["valor_movto"]["col"]
        size_valor_movto = self.colunas_relatorio_extrato["valor_movto"]["size"]
        col_saldo_final = self.colunas_relatorio_extrato["saldo_final"]["col"]
        size_saldo_final = self.colunas_relatorio_extrato["saldo_final"]["size"]
        col_tipo_transacao = self.colunas_relatorio_extrato["tipo_transacao"]["col"]
        col_tipo_operacao = self.colunas_relatorio_extrato["tipo_operacao"]["col"]

        for transacao in transacoes:
            lin += 1
            data_formatada = formatar_data_hora(transacao.data_movto)
            saldo_anterior_formatado = formatar_valor(float(transacao.saldo_anterior))
            valor_operacao_formatado = formatar_valor(float(transacao.valor_movto))
            saldo_final_formatado = formatar_valor(float(transacao.saldo_final))
            tipo_operacao = "CRE" if transacao.tipo_operacao == TipoOperacao.CREDITO else "DEB"
            if transacao.tipo_operacao == TipoOperacao.DEBITO and transacao.id_conta_destino == id_conta:
                tipo_operacao = "CRE"
            exibir_conteudo(data_formatada, lin, col_data_movto)
            exibir_conteudo(saldo_anterior_formatado.rjust(size_saldo_anterior, " "), lin, col_saldo_anterior)
            exibir_conteudo(valor_operacao_formatado.rjust(size_valor_movto, " "), lin, col_valor_movto)
            exibir_conteudo(saldo_final_formatado.rjust(size_saldo_final, " "), lin, col_saldo_final)
            exibir_conteudo(transacao.tipo_transacao._name_, lin, col_tipo_transacao)
            exibir_conteudo(tipo_operacao, lin, col_tipo_operacao)

        while True:
            exibir_conteudo(opcoes_disponiveis["opcoes_consultas"], col=2)
            opcao = esperar_tecla()
            if opcao == "R":
                break
            if opcao not in operacoes_disponiveis["opcoes_consultas"]:
                exibir_mensagem("Opção inválida!", wait_key=True)
                continue
            break
        return opcao
        
    def iniciar(self):
        limpar_tela()
        titulo_tela = titulo_telas["menu_principal"].replace(" - MENU PRINCIPAL", "").strip() + " - " + Versao.get_init_version().to_str()
        exibir_conteudo(titulo_tela.center(75, " "), lin=2, col=2)
        exibir_mensagem(titulo_telas["titulo_consultas"], lin=4, col=2)
        exibir_mensagem(opcoes_disponiveis["menu_consultas"], col=2);
        desenhar_tela(layout_consultas)
        return esperar_tecla()
        