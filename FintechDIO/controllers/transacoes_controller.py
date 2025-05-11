from datetime import datetime
from utils.userfunctions import formatar_data, limpar_linha, limpar_tela, exibir_mensagem, exibir_conteudo, posicionar_cursor
from utils.userfunctions import formatar_cpf_cnpj, formatar_valor, esperar_tecla
from utils.helper import TransacaoInputValidator
from models.tiposenum import TipoOperacao, TipoTransacao, TipoChavePix
from models.conta import ContaDTO
from models.transacao import Transacao, TransacaoDTO
from models.versao import Versao
from database.transacoes_repository import TransacoesRepository
from database.clientes_repository import ClientesRepository
from database.contas_repository import ContasRepository
from views.transacoes_view import TransacoesView

letra_to_tipo_chave_pix = {
    "F" : TipoChavePix.CPF,
    "J" : TipoChavePix.CNPJ,
    "T" : TipoChavePix.TELEFONE,
    "E" : TipoChavePix.EMAIL,
    "A" : TipoChavePix.CHAVE_ALEATORIA
}

class TransacaoController:
    _repo_transacao = None
    _repo_cliente = None
    _repo_conta = None
    _app = None
    _conta = None
    _cancelar = False

    def __init__(self):
        self._repo_cliente = ClientesRepository()
        self._repo_conta = ContasRepository(self._repo_cliente)
        self._repo_transacao = TransacoesRepository(self._repo_conta)
        self._app = TransacoesView()
    
    def registrar_transacao(self, **kwargs):
        tipo_transacao = kwargs["tipo_transacao"]

        transacao_temp = {}
        transacao_temp["id"] = 0
        transacao_temp["data_movto"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transacao_temp["tipo_operacao"] = kwargs["tipo_operacao"].value
        transacao_temp["tipo_transacao"] = kwargs["tipo_transacao"].value
        transacao_temp["saldo_anterior"] = kwargs["saldo_atual"]
        transacao_temp["valor_movto"] = kwargs["valor_operacao"]
        transacao_temp["saldo_final"] = kwargs["saldo_final"]
        transacao_temp["nome_autor"] = kwargs["nome_autor"]
        transacao_temp["mensagem"] = kwargs["mensagem"]

        match tipo_transacao:
            case TipoTransacao.DEPOSITO:
                transacao_temp["id_conta_origem"] = 0
                transacao_temp["id_conta_destino"] = kwargs["id_conta_destino"]
                transacao_temp["tipo_chave_pix"] = 0
                transacao_temp["chave_pix"] = ""
                transacao_temp["linha_digitavel"] = ""
            case TipoTransacao.SAQUE:
                transacao_temp["id_conta_origem"] = kwargs["id_conta_origem"]
                transacao_temp["id_conta_destino"] = 0
                transacao_temp["tipo_chave_pix"] = 0
                transacao_temp["chave_pix"] = ""
                transacao_temp["linha_digitavel"] = ""
            case TipoTransacao.PIX:
                transacao_temp["id_conta_origem"] = kwargs["id_conta_origem"]
                transacao_temp["id_conta_destino"] = 0
                transacao_temp["tipo_chave_pix"] = kwargs["tipo_chave_pix"].value
                transacao_temp["chave_pix"] = kwargs["chave_pix"]
                transacao_temp["linha_digitavel"] = ""
            case TipoTransacao.PAGAMENTO:
                transacao_temp["id_conta_origem"] = kwargs["id_conta_origem"]
                transacao_temp["id_conta_destino"] = 0
                transacao_temp["tipo_chave_pix"] = 0
                transacao_temp["chave_pix"] = ""
                transacao_temp["linha_digitavel"] = kwargs["linha_digitavel"]
            case TipoTransacao.TRANSFERENCIA:
                transacao_temp["id_conta_origem"] = kwargs["id_conta_origem"]
                transacao_temp["id_conta_destino"] = kwargs["id_conta_destino"]
                transacao_temp["tipo_chave_pix"] = 0
                transacao_temp["chave_pix"] = ""
                transacao_temp["linha_digitavel"] = ""
            case TipoTransacao.DOC:
                transacao_temp["id_conta_origem"] = 0
                transacao_temp["id_conta_destino"] = kwargs["id_conta_destino"]
                transacao_temp["tipo_chave_pix"] = 0
                transacao_temp["chave_pix"] = ""
                transacao_temp["linha_digitavel"] = kwargs["linha_digitavel"]

        transacao = Transacao(**transacao_temp)

        fl_ok, novo_id, mensagem = self._repo_transacao.add(transacao)

        if not fl_ok:
            exibir_mensagem(mensagem, wait_key=True)
            return fl_ok
    
        exibir_mensagem(f"Transação registrada com sucesso! Número da Transação: {novo_id}", wait_key=True)
        return fl_ok

    def atualizar_saldo(self, id_conta:int, valor_operacao:float, tipo_operacao: TipoOperacao):
        exibir_mensagem("Atualizando saldo da conta....")
        fl_ok, mensagem = self._repo_conta.atualizar_saldo(id_conta, valor_operacao, tipo_operacao)

        if not fl_ok:
            exibir_mensagem(mensagem, wait_key=True)
        else:
            exibir_mensagem("Saldo atualizado com sucesso!", wait_key=True)

    def get_conta_origem(self):
        lin_conta = self._app.campos_transacao["id_conta_origem"]["lin"]
        col_conta = self._app.campos_transacao["id_conta_origem"]["col"]
        msg_conta = self._app.campos_transacao["id_conta_origem"]["mensagem"]
        size_conta = self._app.campos_transacao["id_conta_origem"]["size"]
        lin_cpf_origem = self._app.campos_transacao["cpf_cnpj_origem"]["lin"]
        col_cpf_origem = self._app.campos_transacao["cpf_cnpj_origem"]["col"]
        size_cpf_origem = self._app.campos_transacao["cpf_cnpj_origem"]["size"]
        lin_nome_cliente = self._app.campos_transacao["nome_cliente_origem"]["lin"]
        col_nome_cliente = self._app.campos_transacao["nome_cliente_origem"]["col"]
        size_nome_cliente = self._app.campos_transacao["nome_cliente_origem"]["size"]
        while True:
            try:
                limpar_linha()
                exibir_conteudo("↓", lin_conta - 1, col_conta)
                exibir_mensagem(msg_conta)
                posicionar_cursor(lin_conta, col_conta)
                id_conta_origem = int(input())
                if id_conta_origem == 9:
                    self._cancelar = True
                    break
                conta_dto_origem, mensagem = self._repo_conta.get_by_id(id_conta_origem)
                if not conta_dto_origem:
                    exibir_mensagem(mensagem, wait_key=True)
                    continue
                if conta_dto_origem.cpf_cnpj != "":
                    _, doc_formatado = formatar_cpf_cnpj(conta_dto_origem.cpf_cnpj)
                else:
                    doc_formatado = ""
                exibir_conteudo(str(conta_dto_origem.conta.id).rjust(size_conta, " "), lin_conta, col_conta)
                exibir_conteudo(doc_formatado.rjust(size_cpf_origem, " "), lin_cpf_origem, col_cpf_origem)
                exibir_conteudo(conta_dto_origem.nome_cliente[:size_nome_cliente].ljust(size_nome_cliente, " "), lin_nome_cliente, col_nome_cliente)
                break
            except Exception as ex:
                exibir_mensagem(ex, wait_key=True)
         
        exibir_conteudo(" ", lin_conta - 1, col_conta)
        if self._cancelar:
            return None
        return conta_dto_origem
    
    def get_conta_destino(self):
        lin_conta = self._app.campos_transacao["id_conta_destino"]["lin"]
        col_conta = self._app.campos_transacao["id_conta_destino"]["col"]
        size_conta = self._app.campos_transacao["id_conta_destino"]["size"]
        mensagem_conta = self._app.campos_transacao["id_conta_destino"]["mensagem"]
        lin_cpf_destino = self._app.campos_transacao["cpf_cnpj_destino"]["lin"]
        col_cpf_destino = self._app.campos_transacao["cpf_cnpj_destino"]["col"]
        size_cpf_destino = self._app.campos_transacao["cpf_cnpj_destino"]["size"]
        lin_nome_cliente = self._app.campos_transacao["nome_cliente_destino"]["lin"]
        col_nome_cliente = self._app.campos_transacao["nome_cliente_destino"]["col"]
        size_nome_cliente = self._app.campos_transacao["nome_cliente_destino"]["size"]
        while True:
            try:
                limpar_linha()
                exibir_conteudo("↓", lin_conta - 1, col_conta)
                exibir_mensagem(mensagem_conta)
                posicionar_cursor(lin_conta, col_conta)
                id_conta_destino = int(input())
                if id_conta_destino == 9:
                    self._cancelar = True
                    break
                conta_dto_destino, mensagem = self._repo_conta.get_by_id(id_conta_destino)
                if not conta_dto_destino:
                    exibir_mensagem(mensagem, wait_key=True)
                    continue
                if conta_dto_destino.cpf_cnpj != "":
                    _, doc_formatado = formatar_cpf_cnpj(conta_dto_destino.cpf_cnpj)
                else:
                    doc_formatado = ""
                exibir_conteudo(str(conta_dto_destino.conta.id).rjust(size_conta, " "), lin_conta, col_conta)
                exibir_conteudo(doc_formatado.rjust(size_cpf_destino, " "), lin_cpf_destino, col_cpf_destino)
                exibir_conteudo(conta_dto_destino.nome_cliente[:size_nome_cliente].ljust(size_nome_cliente, " "), lin_nome_cliente, col_nome_cliente)
                break
            except Exception as ex:
                exibir_mensagem(ex, wait_key=True)
        exibir_conteudo(" ", lin_conta - 1, col_conta)
        if self._cancelar:
            return None
        return conta_dto_destino

    def get_tipo_chave_pix(self):
        info = self._app.campos_transacao["tipo_chave_pix"]
        mensagem = info["mensagem"]
        tipo_atual = TipoChavePix.CPF.descricao
        while True:
            lin = info["lin"]
            col = info[tipo_atual]
            exibir_mensagem(mensagem)
            exibir_conteudo("↓", lin - 1, col)
            letra = esperar_tecla()
            if letra == "S":
                self._cancelar = True
                return
            tipo_chave_pix = letra_to_tipo_chave_pix.get(letra)
            if tipo_chave_pix is None:
                exibir_mensagem("Opção inválida! Tente novamente!")
                continue
            break
        exibir_conteudo(" ", lin - 1, col)
        if not self._cancelar:
            self._app.setar_tipo_chave_pix(tipo_chave_pix)
        return tipo_chave_pix
    
    def get_chave_pix(self, tipo_chave: TipoChavePix):
        info = self._app.campos_transacao["chave_pix"]
        mensagem = info["mensagem"]
        artigo = "um" if tipo_chave != TipoChavePix.CHAVE_ALEATORIA else "uma"
        valido = "valido" if tipo_chave != TipoChavePix.CHAVE_ALEATORIA else "valida"
        size = info["size"]

        while True:
            exibir_conteudo("↓", info["lin"] - 1, info["col"])
            exibir_mensagem(mensagem)
            posicionar_cursor(info["lin"], info["col"])
            chave_pix = input().strip()
            if chave_pix.upper() == "FIM":
                self._cancelar = True
                return
            if chave_pix == "":
                exibir_mensagem("Chave PIX não pode ficar em branco!", wait_key=True)
                continue
            if not TransacaoInputValidator.chave_pix_validate(chave_pix, tipo_chave):
                exibir_mensagem(f"Informe {artigo} {tipo_chave._name_} {valido} como chave PIX", wait_key=True)
                continue
            break
        exibir_conteudo(" ", info["lin"] - 1, info["col"])
        exibir_conteudo(chave_pix.ljust(size, " "), info["lin"], info["col"])
        return chave_pix

    def get_linha_digitavel(self):
        lin = self._app.campos_transacao["linha_digitavel"]["lin"]
        col = self._app.campos_transacao["linha_digitavel"]["col"]
        size = self._app.campos_transacao["linha_digitavel"]["size"]
        mensagem = self._app.campos_transacao["linha_digitavel"]["mensagem"]
        while True:
            exibir_mensagem(mensagem)
            exibir_conteudo("↓", lin - 1, col)
            posicionar_cursor(lin, col)
            linha_digitavel = input().strip()
            if linha_digitavel.upper() == "FIM":
                self._cancelar = True
                return
            if linha_digitavel == "":
                exibir_mensagem("Linha digitável não pode ficar em branco!", wait_key=True)
                continue
            break
        exibir_conteudo(" ", lin - 1, col)
        if not self._cancelar:
            exibir_conteudo(linha_digitavel.ljust(size, " "), lin, col)
        return linha_digitavel

    def get_valor_operacao(self):
        info_valor = self._app.campos_transacao["valor_operacao"]
        size = info_valor["size"]
        while True:
            try:
                exibir_conteudo("↓", info_valor["lin"] - 1, info_valor["col"])
                exibir_mensagem(info_valor["mensagem"])
                posicionar_cursor(info_valor["lin"], info_valor["col"])
                valor_operacao = float(input().replace(",","_").replace(".", ",").replace("_","."))
                if valor_operacao == 0:
                    self._cancelar = True
                    break
                valor_formatado = formatar_valor(valor_operacao)
                exibir_conteudo(valor_formatado.rjust(size, " "), info_valor["lin"], info_valor["col"])
                break
            except ValueError as ex:
                exibir_mensagem(ex, wait_key=True)
        exibir_conteudo(" ", info_valor["lin"] - 1 , info_valor["col"])
        return valor_operacao

    def get_nome_autor(self):
        info = self._app.campos_transacao["nome_autor"]
        size = info["size"]
        exibir_conteudo("↓", info["lin"] - 1, info["col"])
        exibir_mensagem(info["mensagem"])
        posicionar_cursor(info["lin"], info["col"])
        nome_autor = input().title().strip()
        if nome_autor.upper() == "FIM":
            self._cancelar = True
            return
        exibir_conteudo(nome_autor.ljust(size, " "), info["lin"], info["col"])
        exibir_conteudo(" ", info["lin"] - 1, info["col"])
        return nome_autor

    def get_mensagem_opcional(self):
        info = self._app.campos_transacao["mensagem_opcional"]
        size = info["size"]
        exibir_conteudo("↓", info["lin"] - 1, info["col"])
        exibir_mensagem(info["mensagem"])
        posicionar_cursor(info["lin"], info["col"])
        mensagem_opcional = input().title().strip()
        exibir_conteudo(mensagem_opcional.ljust(size, " "), info["lin"], info["col"])
        exibir_conteudo(" ", info["lin"] - 1, info["col"])
        if mensagem_opcional.upper() == "FIM":
            self._cancelar = True
        return mensagem_opcional

    def get_campos_comuns(self):
        valor_operacao = self.get_valor_operacao()
        if self._cancelar:
            return None, None, None
        nome_autor = self.get_nome_autor()
        if self._cancelar:
            return None, None, None
        mensagem_opcional = self.get_mensagem_opcional()
        if self._cancelar:
            return None, None, None
        return valor_operacao, nome_autor, mensagem_opcional
    
    def get_confirmar_dados(self):
        while True:
            limpar_linha()
            exibir_mensagem("Confirme os dados para essa operação")
            exibir_conteudo("↓", lin=27, col=28)
            posicionar_cursor(lin=28, col=28)
            confirmar = esperar_tecla(ocultar_cursor=False)
            if confirmar not in [ "S", "N" ]:
                exibir_mensagem("Informe apenas S ou N para confirmar ou não os dados!", wait_key=True)
                continue
            break
        return confirmar

    def efetuar_deposito(self):
        self._app.setar_tipo_transacao(TipoTransacao.DEPOSITO)
        conta_dto_destino = self.get_conta_destino()
        if self._cancelar:
            return
        valor_operacao, nome_autor, mensagem_opcional = self.get_campos_comuns()
        if self._cancelar:
            return
        confirmar_dados = self.get_confirmar_dados()
        if confirmar_dados == "N":
            return
        fl_ok = self.registrar_transacao(tipo_transacao = TipoTransacao.DEPOSITO, tipo_operacao = TipoOperacao.CREDITO, 
                                         id_conta_destino = conta_dto_destino.conta.id, 
                                         saldo_atual = conta_dto_destino.conta.saldo_atual, 
                                         saldo_final = conta_dto_destino.conta.saldo_atual + valor_operacao,
                                         valor_operacao = valor_operacao, nome_autor = nome_autor, 
                                         mensagem = mensagem_opcional)
        if fl_ok:
           self.atualizar_saldo(conta_dto_destino.conta.id, valor_operacao, TipoOperacao.CREDITO)
        
    def efetuar_saque(self):
        self._app.setar_tipo_transacao(TipoTransacao.SAQUE)
        conta_dto_origem = self.get_conta_origem()
        if self._cancelar:
            return
        valor_operacao, nome_autor, mensagem_opcional = self.get_campos_comuns()
        if self._cancelar:
            return
        confirmar_dados = self.get_confirmar_dados()
        if confirmar_dados == "N":
            return
        
        fl_ok = self.registrar_transacao(tipo_transacao = TipoTransacao.SAQUE, tipo_operacao = TipoOperacao.DEBITO, 
                                         id_conta_origem = conta_dto_origem.conta.id,
                                         saldo_atual = conta_dto_origem.conta.saldo_atual,
                                         saldo_final = conta_dto_origem.conta.saldo_atual - valor_operacao,
                                         valor_operacao = valor_operacao, nome_autor = nome_autor,
                                         mensagem = mensagem_opcional)
        if fl_ok:
            self.atualizar_saldo(conta_dto_origem.conta.id, valor_operacao, TipoOperacao.DEBITO)
            
    def efetuar_pix(self):
        self._app.setar_tipo_transacao(TipoTransacao.PIX)
        conta_dto_origem = self.get_conta_origem()
        if self._cancelar:
            return
        tipo_chave_pix = self.get_tipo_chave_pix()
        if self._cancelar:
            return
        chave_pix = self.get_chave_pix(tipo_chave_pix)
        if self._cancelar:
            return
        valor_operacao, nome_autor, mensagem_opcional = self.get_campos_comuns()
        if self._cancelar:
            return
        confirmar_dados = self.get_confirmar_dados()
        if confirmar_dados == "N":
            return
        
        fl_ok = self.registrar_transacao(tipo_transacao = TipoTransacao.PIX, tipo_operacao = TipoOperacao.DEBITO,
                                         id_conta_origem = conta_dto_origem.conta.id, 
                                         saldo_atual = conta_dto_origem.conta.saldo_atual,
                                         saldo_final = conta_dto_origem.conta.saldo_atual - valor_operacao,
                                         tipo_chave_pix = tipo_chave_pix, chave_pix = chave_pix, 
                                         valor_operacao = valor_operacao, nome_autor = nome_autor,
                                         mensagem = mensagem_opcional)
        if fl_ok:
            self.atualizar_saldo(conta_dto_origem.conta.id, valor_operacao, TipoOperacao.DEBITO)

    def efetuar_pagamento(self):
        self._app.setar_tipo_transacao(TipoTransacao.PAGAMENTO)
        conta_dto_origem = self.get_conta_origem()
        if self._cancelar:
            return
        linha_digitavel = self.get_linha_digitavel()
        if self._cancelar:
            return
        valor_operacao, nome_autor, mensagem_opcional = self.get_campos_comuns()
        if self._cancelar:
            return
        confirmar = self.get_confirmar_dados()
        if confirmar == "N":
            return
        
        fl_ok = self.registrar_transacao(tipo_transacao=TipoTransacao.PAGAMENTO, tipo_operacao=TipoOperacao.DEBITO,
                                         id_conta_origem = conta_dto_origem.conta.id,
                                         saldo_atual = conta_dto_origem.conta.saldo_atual,
                                         saldo_final = conta_dto_origem.conta.saldo_atual - valor_operacao,
                                         linha_digitavel = linha_digitavel, valor_operacao = valor_operacao,
                                         nome_autor = nome_autor, mensagem = mensagem_opcional)
        if fl_ok:
            self.atualizar_saldo(conta_dto_origem.conta.id, valor_operacao, TipoOperacao.DEBITO)
        
    def efetuar_transferencia(self):
        self._app.setar_tipo_transacao(TipoTransacao.TRANSFERENCIA)
        conta_dto_origem = self.get_conta_origem()
        if self._cancelar:
            return
        conta_dto_destino = self.get_conta_destino()
        if self._cancelar:
            return
        valor_operacao, nome_autor, mensagem_opcional = self.get_campos_comuns()
        if self._cancelar:
            return
        confirmar = self.get_confirmar_dados()
        if confirmar == "N":
            return
        
        fl_ok_debito = self.registrar_transacao(tipo_transacao=TipoTransacao.TRANSFERENCIA, tipo_operacao=TipoOperacao.DEBITO,
                                          id_conta_origem = conta_dto_origem.conta.id,
                                          id_conta_destino = conta_dto_destino.conta.id,
                                          saldo_atual = conta_dto_origem.conta.saldo_atual,
                                          saldo_final = conta_dto_origem.conta.saldo_atual - valor_operacao,
                                          valor_operacao = valor_operacao,
                                          nome_autor = nome_autor, mensagem = mensagem_opcional)
        if fl_ok_debito:
           fl_ok_credito = self.registrar_transacao(tipo_transacao=TipoTransacao.TRANSFERENCIA, tipo_operacao=TipoOperacao.Credito,
                                                    id_conta_origem=conta_dto_origem.conta.id,
                                                    id_conta_destino=conta_dto_destino.conta.id,
                                                    saldo_atual=conta_dto_destino.conta.saldo_atual,
                                                    valor_operacao=valor_operacao,
                                                    saldo_final=conta_dto_destino.saldo_atual + valor_operacao,
                                                    nome_autor=nome_autor, mensagem=mensagem_opcional)
        if fl_ok_debito:
            self.atualizar_saldo(conta_dto_origem.conta.id, valor_operacao, TipoOperacao.DEBITO)
        if fl_ok_credito:
            self.atualizar_saldo(conta_dto_destino.conta.id, valor_operacao, TipoOperacao.CREDITO)

    def efetuar_doc(self):
        self._app.setar_tipo_transacao(TipoTransacao.DOC)
        conta_dto_destino = self.get_conta_destino()
        if self._cancelar:
            return
        linha_digitavel = self.get_linha_digitavel()
        if self._cancelar:
            return
        valor_operacao, nome_autor, mensagem_opcional = self.get_campos_comuns()
        if self._cancelar:
            return
        confirmar_dados = self.get_confirmar_dados()
        if confirmar_dados == "N":
            return
        fl_ok = self.registrar_transacao(tipo_transacao = TipoTransacao.DOC, tipo_operacao = TipoOperacao.CREDITO, 
                                         id_conta_destino = conta_dto_destino.conta.id, 
                                         saldo_atual = conta_dto_destino.conta.saldo_atual, 
                                         saldo_final = conta_dto_destino.conta.saldo_atual + valor_operacao,
                                         linha_digitavel = linha_digitavel,
                                         valor_operacao = valor_operacao, nome_autor = nome_autor, 
                                         mensagem = mensagem_opcional)
        if fl_ok:
            self.atualizar_saldo(conta_dto_destino.conta.id, valor_operacao, TipoOperacao.CREDITO)

    def iniciar(self):
        while True:
            self._cancelar = False
            opcao = self._app.iniciar()
            if opcao == 9:
                break
            match opcao:
                case 1:
                    self.efetuar_deposito()
                case 2:
                    self.efetuar_saque()
                case 3:
                    self.efetuar_pix()
                case 4:
                    self.efetuar_pagamento()
                case 5:
                    self.efetuar_transferencia()
                case 6:
                    self.efetuar_doc()
        
        limpar_tela()
        limpar_linha()
