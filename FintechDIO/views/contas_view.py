from dataclasses import fields
from enum import Enum
from models.conta import Conta, ContaConsulta, ContaDTO
from models.tiposenum import TipoConta, StatusConta
from models.versao import Versao
from utils.userfunctions import exibir_mensagem, esperar_tecla, limpar_linha, limpar_tela, exibir_conteudo, desenhar_tela
from utils.userfunctions import formatar_data, formatar_cpf_cnpj, formatar_valor
from layouts.layouts import layout_cadastro_contas, layout_consulta_conta, titulo_telas, opcoes_disponiveis, operacoes_disponiveis, restaurar_linha_29

class ContasView:
    _cancelar = False
    _conta = None

    campos_conta = {
        "id": { "lin": 7, "col": 15, "size": 10, "mensagem": "Informe o número da conta ou 0 para sair" },
        "tipo" : { "lin": 7, "size": 1, "conta_corrente": 38, "poupanca": 58, "aplicacao": 72, "mensagem" : "Selecione o tipo da conta pressionando C, P, A ou S pra sair" },
        "cpf_cnpj" : { "lin": 9, "col": 15, "size": 18, "mensagem": "Informe o CPF/CNPJ do cliente ou SAIR pra encerrar" },
        "nome_cliente": { "lin": 9, "col": 35, "size": 63 },
        "limite_especial" : { "lin": 11, "col": 15, "size": 14, "mensagem": "Digite o valor do limite especial ou SAIR para encerrar" },
        "data_abertura" : { "lin": 11, "col": 88, "size": 10 },
        "status" : { "lin": 13, "size": 1, "analise": 15, "ativa": 29, "suspensa": 41, "bloqueada": 56, "inativa": 72, "encerrada": 86,
                    "mensagem": "L = Análise / A = Ativa / S = Suspensa / B = Bloqueada / E - Encerrada ou X para sair" },
        "data_encerramento": { "lin": 15, "col": 87, "size": 10, "mensagem": "Digite a data de encerramento" }
    }

    def __init__(self):
        pass

    def limpar_campos(self):
        for key, info in self.campos_conta.items():
            if key == "tipo":
                exibir_conteudo("_", info["lin"], info["conta_corrente"])
                exibir_conteudo("_", info["lin"], info["poupanca"])
                exibir_conteudo("_", info["lin"], info["aplicacao"])
            elif key == "status":
                exibir_conteudo("_", info["lin"], info["analise"])
                exibir_conteudo("_", info["lin"], info["ativa"])
                exibir_conteudo("_", info["lin"], info["suspensa"])
                exibir_conteudo("_", info["lin"], info["bloqueada"])
                exibir_conteudo("_", info["lin"], info["inativa"])
                exibir_conteudo("_", info["lin"], info["encerrada"])
            else:
                exibir_conteudo("_" * info["size"], info["lin"], info["col"])

    def setar_tipo_conta(self, tipo_conta: TipoConta):
        info_tipo = self.campos_conta["tipo"]
        match tipo_conta:
            case TipoConta.CONTA_CORRENTE:
                exibir_conteudo(" ", info_tipo["lin"], info_tipo["poupanca"])
                exibir_conteudo(" ", info_tipo["lin"], info_tipo["aplicacao"])
            case TipoConta.POUPANCA:
                exibir_conteudo(" ", info_tipo["lin"], info_tipo["conta_corrente"])
                exibir_conteudo(" ", info_tipo["lin"], info_tipo["aplicacao"])
            case TipoConta.APLICACAO:
                exibir_conteudo(" ", info_tipo["lin"], info_tipo["conta_corrente"])
                exibir_conteudo(" ", info_tipo["lin"], info_tipo["poupanca"])

    def setar_status_conta(self, status: StatusConta):
        info_status = self.campos_conta["status"]
        match status:
            case StatusConta.ANALISE:
                exibir_conteudo(" ", info_status["lin"], info_status["ativa"])
                exibir_conteudo(" ", info_status["lin"], info_status["suspensa"])
                exibir_conteudo(" ", info_status["lin"], info_status["bloqueada"])
                exibir_conteudo(" ", info_status["lin"], info_status["inativa"])
                exibir_conteudo(" ", info_status["lin"], info_status["encerrada"])
            case StatusConta.ATIVA:
                exibir_conteudo(" ", info_status["lin"], info_status["analise"])
                exibir_conteudo(" ", info_status["lin"], info_status["suspensa"])
                exibir_conteudo(" ", info_status["lin"], info_status["bloqueada"])
                exibir_conteudo(" ", info_status["lin"], info_status["inativa"])
                exibir_conteudo(" ", info_status["lin"], info_status["encerrada"])
            case StatusConta.SUSPENSA:
                exibir_conteudo(" ", info_status["lin"], info_status["analise"])
                exibir_conteudo(" ", info_status["lin"], info_status["ativa"])
                exibir_conteudo(" ", info_status["lin"], info_status["bloqueada"])
                exibir_conteudo(" ", info_status["lin"], info_status["inativa"])
                exibir_conteudo(" ", info_status["lin"], info_status["encerrada"])
            case StatusConta.BLOQUEADA:
                exibir_conteudo(" ", info_status["lin"], info_status["analise"])
                exibir_conteudo(" ", info_status["lin"], info_status["ativa"])
                exibir_conteudo(" ", info_status["lin"], info_status["suspensa"])
                exibir_conteudo(" ", info_status["lin"], info_status["inativa"])
                exibir_conteudo(" ", info_status["lin"], info_status["encerrada"])
            case StatusConta.INATIVA:
                exibir_conteudo(" ", info_status["lin"], info_status["analise"])
                exibir_conteudo(" ", info_status["lin"], info_status["ativa"])
                exibir_conteudo(" ", info_status["lin"], info_status["suspensa"])
                exibir_conteudo(" ", info_status["lin"], info_status["bloqueada"])
                exibir_conteudo(" ", info_status["lin"], info_status["encerrada"])
            case StatusConta.ENCERRADA:
                exibir_conteudo(" ", info_status["lin"], info_status["analise"])
                exibir_conteudo(" ", info_status["lin"], info_status["ativa"])
                exibir_conteudo(" ", info_status["lin"], info_status["suspensa"])
                exibir_conteudo(" ", info_status["lin"], info_status["bloqueada"])
                exibir_conteudo(" ", info_status["lin"], info_status["inativa"])

    def iniciar(self):
        limpar_tela()
        desenhar_tela(layout_cadastro_contas)
        titulo_tela = titulo_telas["menu_principal"].replace(" - MENU PRINCIPAL", "").strip() + " - " + Versao.get_init_version().to_str()
        exibir_conteudo(titulo_tela.center(75, " "), lin=2, col=2)
        exibir_conteudo(titulo_telas["cadastro_contas"], lin=4, col=2)

        while True:
            limpar_linha()
            self.limpar_campos()
            exibir_mensagem(opcoes_disponiveis["opcoes_cadastro"], col=2)
            opcao = esperar_tecla()
            
            if opcao not in operacoes_disponiveis["operacoes_cadastro"]:
                exibir_mensagem("Opção inválida! Pressione qualquer tecla para continuar.", col=2, wait_key=True)
                continue
            break
        return opcao

    def exibir_lista_contas(self, contas: list[ContaConsulta]):
        limpar_tela()
        desenhar_tela(layout_consulta_conta, line_loop=8, stop_loop=28)
        exibir_conteudo(titulo_telas["consulta_conta"], lin=4, col=2)
        lin = 7
        if contas is None:
            exibir_mensagem("Nenhuma conta encontrada! Pressione qualquer tecla pra continuar", wait_key=True)
        else:
            for conta in contas:
                lin += 1
                data_abertura = formatar_data(conta.data_abertura)
                exibir_conteudo(str(conta.id).rjust(10, " "), lin, 3)
                exibir_conteudo(conta.nome_cliente[:42].ljust(42, " "), lin, 16)
                exibir_conteudo(conta.telefone[:13].ljust(13, " "), lin, 61)
                exibir_conteudo(data_abertura, lin, 77)
                exibir_conteudo(conta.status.name, lin, 90)

        while True:
            exibir_mensagem(opcoes_disponiveis["opcoes_consultas"], col=2)
            opcao = esperar_tecla()
            if opcao == "R":
                exibir_conteudo(restaurar_linha_29, lin=29, col=1)
                break
            if opcao not in [ "N", "P", "V", "R"]:
                exibir_mensagem("Opção inválida! Tente novamente!", wait_key=True)
                continue
            break
        return opcao
    
    def exibir_dados_conta(self, conta_dto: ContaDTO):
        info_nome = self.campos_conta["nome_cliente"]
        exibir_conteudo(" " * info_nome["size"], info_nome["lin"], info_nome["col"])
        exibir_conteudo(conta_dto.nome_cliente, info_nome["lin"], info_nome["col"])
        for campo in fields(conta_dto.conta):
            if campo.name == "saldo_atual":
                continue
            if campo.name == "id_cliente":
                info = self.campos_conta["cpf_cnpj"]
            else:
                info = self.campos_conta[campo.name]
            valor = getattr(conta_dto.conta, campo.name)
            if campo.type.__name__ == "date":
                if valor is not None:
                    valor_formatado = formatar_data(valor)
                else:
                    valor_formatado = ""
            elif campo.name == "id_cliente":
                _, valor_formatado = formatar_cpf_cnpj(conta_dto.cpf_cnpj)
                if valor_formatado is not None:
                    valor_formatado = valor_formatado.rjust(18, " ")
            elif isinstance(valor, Enum):
                exibir_conteudo("•", info["lin"], info[valor.descricao])
                continue
            elif campo.type.__name__ ==  "int":
                valor_formatado = str(valor).rjust(10, " ")
            elif campo.type.__name__ == "float":
                valor_float = float(valor)
                valor_formatado = formatar_valor(valor_float).rjust(14, " ")
            else:
                valor_formatado = valor
            exibir_conteudo(" " * info["size"], info["lin"], info["col"])
            exibir_conteudo(valor_formatado, info["lin"], info["col"])
        self.setar_tipo_conta(conta_dto.conta.tipo)
        self.setar_status_conta(conta_dto.conta.status)
            

