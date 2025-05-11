from datetime import date
from database.contas_repository import ContasRepository
from database.clientes_repository import ClientesRepository
from views.contas_view import ContasView
from controllers.chavespix_controller import ChavesPixController
from utils import userfunctions
from utils.userfunctions import exibir_mensagem, limpar_tela, limpar_linha, exibir_conteudo, exibir_mensagem, posicionar_cursor, esperar_tecla
from models.conta import Conta, ContaDTO
from models.tiposenum import TipoConta, StatusConta
from layouts.layouts import opcoes_disponiveis, operacoes_disponiveis

letra_para_tipo_conta = {
    "C" : TipoConta.CONTA_CORRENTE,
    "P" : TipoConta.POUPANCA,
    "A" : TipoConta.APLICACAO
}

letra_para_status_conta = {
    "L" : StatusConta.ANALISE,
    "A" : StatusConta.ATIVA,
    "S" : StatusConta.SUSPENSA,
    "B" : StatusConta.BLOQUEADA,
    "I" : StatusConta.INATIVA,
    "E" : StatusConta.ENCERRADA
}

class ContasController:
    _repo_conta = None
    _repo_cliente = None,
    _app = None
    _app_chavespix = None
    _conta = None
    _cancelar = False
    _cpf_cnpj_alteracao = ""

    def __init__(self):
        self._repo_cliente = ClientesRepository()
        self._repo_conta = ContasRepository(self._repo_cliente)
        self._app = ContasView()
        self._app_chavespix = ChavesPixController()
        self.pagina_atual = 1
        self.tamanho_pagina = 21
        self.total_registros = 0
        self.total_paginas = 1
        self.filtros = {}

    def get_by_id_conta(self):
        info = self._app.campos_conta["id"]
        while True:
            try:
                limpar_linha()
                exibir_conteudo("↓", info["lin"] - 1, info["col"])
                exibir_mensagem(info["mensagem"])
                posicionar_cursor(info["lin"], info["col"])
                conta_id = int(input())
                if conta_id == 0:
                    self._cancelar = True
                    break
                conta_dto, mensagem = self._repo_conta.get_by_id(conta_id)
                if not conta_dto:
                    exibir_mensagem(mensagem, wait_key=True)
                    continue
                break
            except ValueError as error:
                exibir_mensagem(f"Número da conta inválido: {error}", wait_key=True)
            except Exception as ex:
                exibir_mensagem(ex, wait_key=True)
        exibir_conteudo(str(conta_id).rjust(10, " "), info["lin"], info["col"])
        exibir_conteudo(" ", info["lin"] - 1, info["col"])
        return conta_dto

    def get_tipo_conta(self):
        info = self._app.campos_conta["tipo"]
        campo = "conta_corrente"
        tipo_conta = None
        while True:
            limpar_linha()
            exibir_conteudo("↓", info["lin"] - 1, info[campo])
            exibir_mensagem(info["mensagem"])
            posicionar_cursor(info["lin"], info[campo])
            letra = esperar_tecla()
            if letra == "S":
                self._cancelar = True
                break
            if letra == "" and self._conta is not None:
                tipo_conta = self._conta.tipo
            else:
                tipo_conta = letra_para_tipo_conta.get(letra)
            if tipo_conta is None:
                exibir_mensagem("Tipo de conta inválido", wait_key=True)
                continue
            break
        exibir_conteudo(" ", info["lin"], info[campo])
        if not self._cancelar:
            exibir_conteudo("•", info["lin"], info[tipo_conta.descricao])
            self._app.setar_tipo_conta(tipo_conta)
        return tipo_conta
        
    def get_id_cliente(self):
        info = self._app.campos_conta["cpf_cnpj"]
        info_nome = self._app.campos_conta["nome_cliente"]
        while True:
            exibir_conteudo("↓", info["lin"] - 1, info["col"])
            exibir_mensagem(info["mensagem"])
            posicionar_cursor(info["lin"], info["col"])
            cpf_cnpj = input().strip()
            if cpf_cnpj == "SAIR":
                self._cancelar = True
                break
            if cpf_cnpj == "" and self._conta is not None:
                cpf_cnpj = self._cpf_cnpj_alteracao
            fl_ok, mensagem = userfunctions.validar_cpf_cnpj(cpf_cnpj)
            if not fl_ok:
                exibir_mensagem(mensagem, wait_key=True)
                continue
            fl_ok, doc_formatado = userfunctions.formatar_cpf_cnpj(cpf_cnpj)
            if not fl_ok:
                exibir_mensagem(doc_formatado, wait_key=True)
                continue
            cliente, mensagem = self._repo_cliente.get_by_cpf_cnpj(cpf_cnpj)
            if not cliente:
                exibir_mensagem(mensagem, wait_key=True)
                continue
            break
        exibir_conteudo(" ", info["lin"], info["col"])
        if not self._cancelar:
            exibir_conteudo(doc_formatado.rjust(18, " "), info["lin"], info["col"])
            exibir_conteudo(" " * info_nome["size"], info_nome["lin"], info_nome["col"])
            exibir_conteudo(cliente.nome, info_nome["lin"], info_nome["col"])
            return cliente.id
        return 0

    def get_limite_especial(self):
        info = self._app.campos_conta["limite_especial"]
        while True:
            try:
                exibir_conteudo("↓", info["lin"] - 1, info["col"])
                exibir_mensagem(info["mensagem"])
                posicionar_cursor(info["lin"], info["col"])
                valor_limite_str = input().replace('.', '_').replace(',', '.').replace('_', ',')
                if valor_limite_str == "SAIR":
                    self._cancelar = True
                    break
                if valor_limite_str == "":
                    if self._conta is not None:
                       limite_especial = self._conta.limite_especial
                    else:
                        limite_especial = 0.00
                else:
                    limite_especial = float(valor_limite_str)
            except ValueError as error:
                exibir_mensagem(f"Valo do limite inválido. Tente novamente: {error}", wait_key=True)
            break
        exibir_conteudo(" ", info["lin"] - 1, info["col"])
        if not self._cancelar:
            valor_formatado = userfunctions.formatar_valor(limite_especial)
            exibir_conteudo(valor_formatado.rjust(14, " "), info["lin"], info["col"])
            return limite_especial
        return 0

    def get_status(self):
        info = self._app.campos_conta["status"]
        posicao = "analise"
        status = None
        while True:
            exibir_conteudo("↓", info["lin"] - 1, info[posicao])
            exibir_mensagem(info["mensagem"])
            posicionar_cursor(info["lin"], info[posicao])
            letra = esperar_tecla()
            if letra == "X":
                self._cancelar = True
                break
            status = letra_para_status_conta.get(letra)
            if status == None:
                if self._conta is not None:
                    status= self._conta.status
                else:
                    exibir_mensagem("Status inválido. Utilize uma das opções disponível!", wait_key=True)
                    continue
            exibir_conteudo(" ", info["lin"], info[posicao])
            break
        if not self._cancelar:
            exibir_conteudo("•", info["lin"], info[status.descricao])
            self._app.setar_status_conta(status)
        return status
    
    def get_data_encerramento(self):
        info = self._app.campos_conta["data_encerramento"]
        while True:
            exibir_conteudo("↓", info["lin"] - 1, info["col"])
            exibir_mensagem(info["mensagem"])
            posicionar_cursor(info["lin"], info["col"])
            str_data_encerramento = input().strip()
            if str_data_encerramento == "SAIR":
                self._cancelar = True
                break
            if str_data_encerramento == "" and self._conta is not None:
                str_data_encerramento = self._conta.data_encerramento.strftime("%d/%m/%Y") if self._conta.data_encerramento else ""
            fl_ok, data_encerramento, mensagem = userfunctions.validar_data(str_data_encerramento)
            if not fl_ok:
                exibir_mensagem(mensagem, wait_key=True)
                continue
            break
        exibir_conteudo(" ", info["lin"] + 1, info["col"])
        exibir_conteudo(userfunctions.formatar_data(data_encerramento), info["lin"], info["col"])
        return data_encerramento
                
    def get_dados_conta(self):
        self._cancelar = False
        conta_temp = {}
        if self._conta is not None:
            conta_temp["id"] = self._conta.id
            conta_temp["data_abertura"] = self._conta.data_abertura
            conta_temp["saldo_atual"] = self._conta.saldo_atual
            conta_temp["data_encerramento"] = self._conta.data_encerramento
        else:
            conta_temp["id"] = 0
            conta_temp["data_abertura"] = date.today()
            conta_temp["saldo_atual"] = 0
            conta_temp["data_encerramento"] = None

        conta_temp["tipo"] = self.get_tipo_conta()
        if self._cancelar:
            return None
        conta_temp["id_cliente"] = self.get_id_cliente()
        if self._cancelar:
            return None
        conta_temp["limite_especial"] = self.get_limite_especial()
        if self._cancelar:
            return None
        conta_temp["status"] = self.get_status()
        if self._cancelar:
            return None
        if conta_temp["status"] == StatusConta.ENCERRADA:
            conta_temp["data_encerramento"] = self.get_data_encerramento()
        if self._cancelar:
            return None
        while True:
            exibir_mensagem("Confirma os dados (S/N)? ")
            confirmar = esperar_tecla()
            if confirmar not in ["S", "N"]:
                exibir_mensagem("Opção inválida. Tecle apenas S ou N!", wait_key=True)
                continue
            if confirmar == "N":
                conta = None
            else:
                conta = Conta(**conta_temp)
            break
        return conta

    def consultar_conta(self):
        conta_dto = self.get_by_id_conta()
        if self._cancelar or not conta_dto:
            return
        self._app.exibir_dados_conta(conta_dto)
        exibir_mensagem("Consultando conta", lin=28)
        while True:
            self._cancelar = False
            exibir_conteudo(opcoes_disponiveis["consulta_conta"], col=2)
            opcao = esperar_tecla()
            if opcao == "R":
                break
            if opcao not in operacoes_disponiveis["consulta_conta"]:
                exibir_mensagem("Opção inválida! Tente novamente!", wait_key=True)
                continue
            if opcao == "N":
                self._app.limpar_campos()
                conta_dto = self.get_by_id_conta()
                if self._cancelar or not conta_dto:
                    break
                self._app.exibir_dados_conta(conta_dto)
            elif opcao == "G":
                self._app_chavespix.iniciar(conta_dto)

    def cadastrar_conta(self):
        limpar_linha(lin=28)
        exibir_mensagem("Incluindo conta", lin=28)
        data_abertura = date.today()
        info_data = self._app.campos_conta["data_abertura"]
        exibir_conteudo(userfunctions.formatar_data(data_abertura), info_data["lin"], info_data["col"])
        conta = self.get_dados_conta()
        if self._cancelar or conta is None:
            return
        conta.data_abertura = data_abertura
        fl_ok, novo_id, mensagem = self._repo_conta.add(conta)
        if not fl_ok:
            exibir_mensagem(mensagem, wait_key=True)
        else:
            exibir_mensagem(f"Conta incluída com sucesso. Número gerado: {novo_id}", wait_key=True)

    def alterar_conta(self):
        conta_dto = self.get_by_id_conta()
        if self._cancelar or not conta_dto:
            return
        self._app.exibir_dados_conta(conta_dto)
        self._conta = conta_dto.conta
        self._cpf_cnpj_alteracao = conta_dto.cpf_cnpj
        limpar_linha()
        exibir_mensagem("Alterando conta", lin=28)
        conta = self.get_dados_conta()
        if self._cancelar or conta is None:
            return
        fl_ok, mensagem = self._repo_conta.update(conta)
        if not fl_ok:
            exibir_mensagem(mensagem, wait_key=True)
        else:
            exibir_mensagem("Conta atualizada com sucesso!", wait_key=True)

    def excluir_conta(self):
        conta_dto = self.get_by_id_conta()
        if self._cancelar or not conta_dto:
            return
        self._app.exibir_dados_conta(conta_dto)
        limpar_linha()
        exibir_mensagem("Excluindo conta", lin=28)
        while True:
            exibir_mensagem("Deseja realmente excluir essa conta (S/N)? ")
            excluir = esperar_tecla()
            if excluir not in [ 'S', 'N']:
                exibir_mensagem("Digite apenas S ou N", wait_key=True)
                continue
            break
        if excluir == 'N':
            return
        fl_ok, mensagem = self._repo_conta.delete_by_id(conta_dto.conta.id)
        if not fl_ok:
            exibir_mensagem(mensagem, wait_key=True)
        else:
            exibir_mensagem("Conta excluída com sucesso!", wait_key=True)

    def listar_contas(self):
        lista_contas, _ = self._repo_conta.listar_contas()
        while True:
            opcao = self._app.exibir_lista_contas(lista_contas)
            if opcao == "R":
                break
            match opcao:
                case "N":
                    exibir_mensagem("Opção em desenvolvimento", wait_key=True)
                case "P":
                    if self.pagina_atual == self.total_paginas:
                        exibir_mensagem("Você já está na última página", wait_key=True)
                        continue
                    exibir_mensagem("Opção em desenvolvimento", wait_key=True)
                case "V":
                    if self.pagina_atual == self.total_paginas:
                        exibir_mensagem("Você já está na primeira página", wait_key=True)
                        continue
                    exibir_mensagem("Opção em desenvolvimento", wait_key=True)

    def iniciar(self):
        while True:
            opcao = self._app.iniciar()
            if opcao == "R":
                break
            match opcao:
                case "C":
                    self.consultar_conta()
                case "I":
                    self.cadastrar_conta()
                case "A":
                    self.alterar_conta()
                case "E":
                    self.excluir_conta()
                case "L":
                    self.listar_contas()
        limpar_tela()
        limpar_linha()