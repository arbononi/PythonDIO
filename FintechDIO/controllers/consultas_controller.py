from datetime import datetime, date
from database.transacoes_repository import TransacoesRepository
from database.clientes_repository import ClientesRepository
from database.contas_repository import ContasRepository
from models.conta import ContaDTO
from models.versao import Versao
from views.consultas_view import ConsultasView
from utils.userfunctions import limpar_linha, limpar_tela, exibir_conteudo, exibir_mensagem, posicionar_cursor
from utils.userfunctions import validar_data, formatar_data, formatar_data_hora, esperar_tecla
from layouts.layouts import titulo_telas, operacoes_disponiveis, restaurar_linha_29, restaurar_linha

class ConsultasController:
    _app = None
    _repo_cliente = None
    _repo_conta = None
    _repo_transacao = None
    _cancelar = False
    _tipo_consulta = None

    def __init__(self):
        self._app = ConsultasView()
        self._repo_cliente = ClientesRepository()
        self._repo_conta = ContasRepository(self._repo_cliente)
        self._repo_transacao = TransacoesRepository(self._repo_conta)
        self.pagina_atual = 1
        self.tamanho_pagina = 21
        self.total_registros = 0
        self.total_paginas = 1
        self.filtros = {}

    def aplicar_filtros(self, id_conta=None, data_inicial=None, data_final=None):
        data_inicial_formatada = data_inicial.strftime("%Y-%m-%d %H:%M:%S") if data_inicial else ""
        if data_final:
            data_final_formatada = datetime(data_final.year, data_final.month, data_final.day, 23, 59, 59).strftime("%Y-%m-%d %H:%M:%S")
        else:
            data_final_formatada = "9999-12-31 23:59:59"
        self.filtros = {
            "id_conta": id_conta,
            "data_inicial": data_inicial_formatada,
            "data_final": data_final_formatada
        }

    def buscar_pagina_atual(self):
        try:
            transacoes, total, mensagem = self._repo_transacao.buscar_com_filtros(
                filtros = self.filtros,
                pagina = self.pagina_atual,
                tamanho = self.tamanho_pagina
            )
            self.total_registros = total
            self.total_paginas = max(1, (total + self.tamanho_pagina - 1) // self.tamanho_pagina)
            
            return transacoes
        except Exception as ex:
            exibir_mensagem(ex, wait_key=True)
            
    def proxima_pagina(self):
        if self.pagina_atual < self.total_paginas:
            self.pagina_atual += 1
        return self.buscar_pagina_atual()
    
    def pagina_anterior(self):
        if self.pagina_atual > 1:
            self.pagina_atual -= 1
        return self.buscar_pagina_atual()
    
    def get_status_paginacao(self):
        return {
            "pagina_atual": self.pagina_atual,
            "total_paginas": self.total_paginas,
            "total_registros": self.total_registros
        }
    
    def recuperar_tela(self):
        titulo_tela = titulo_telas["menu_principal"].replace(" - MENU PRINCIPAL", "").strip() + " - " + Versao.get_init_version().to_str()
        exibir_conteudo(titulo_tela.center(75, " "), lin=2, col=2)
        exibir_conteudo(restaurar_linha["linha_vazia"], lin=7, col=1)
        exibir_conteudo(restaurar_linha["separadora"], lin=29, col=1)

    def get_conta(self, info):
        conta_dto = None
        while True:
            try:
                if self._tipo_consulta == 1:
                   exibir_conteudo("↓", info["lin"] - 1, info["col"])
                else:
                    exibir_conteudo("→", info["lin"], info["col"] - 2)
                exibir_mensagem(info["mensagem"])
                posicionar_cursor(info["lin"], info["col"])
                id_conta = int(input())
                if id_conta == 0:
                    self._cancelar = True
                    break
                conta_dto, mensagem = self._repo_conta.get_by_id(id_conta)
                if not conta_dto:
                    exibir_mensagem(mensagem, wait_key=True)
                    continue
                break
            except Exception as ex:
                exibir_mensagem(ex, wait_key=True)
        if self._tipo_consulta == 1:
            exibir_conteudo(" ", info["lin"] - 1, info["col"])
        else:
            exibir_conteudo("═", info["lin"], info["col"] - 2)
        return conta_dto        

    def get_data_inicial(self):
        info = self._app.campos_consulta_extrato["data_inicial"]
        data_inicial = None
        while True:
            exibir_conteudo("→", info["lin"], info["col"] - 2)
            exibir_mensagem(info["mensagem"])
            posicionar_cursor(info["lin"], info["col"])
            str_data_inicial = input()
            if str_data_inicial == "0":
                self._cancelar = True
                break
            if str_data_inicial == "":
                data_inicial = date.today()
                fl_ok = True
            else:
                fl_ok, data_inicial, mensagem = validar_data(str_data_inicial)
            if not fl_ok:
                exibir_mensagem(mensagem, wait_key=True)
                continue
            data_formatada = formatar_data(data_inicial)
            if data_formatada:
                exibir_conteudo(data_formatada, info["lin"], info["col"])
            break
        exibir_conteudo(" ", info["lin"], info["col"] - 2)
        return data_inicial

    def get_data_final(self, data_inicial: date):
        info = self._app.campos_consulta_extrato["data_final"]
        data_final = None
        while True:
            exibir_conteudo("→", info["lin"], info["col"] - 2)
            exibir_mensagem(info["mensagem"])
            posicionar_cursor(info["lin"], info["col"])
            str_data_final = input()
            if str_data_final == "0":
                self._cancelar = True
                break
            if str_data_final == "":
                exibir_conteudo("31/12/9999", info["lin"], info["col"])
                break
            fl_ok, data_final, mensagem = validar_data(str_data_final)
            if not fl_ok:
                exibir_mensagem(mensagem, wait_key=True)
                continue
            if data_final < data_inicial:
                exibir_mensagem("Data Final não pode ser menor que a data inicial!", wait_key=True)
                continue
            data_formatada = formatar_data(data_final)
            if data_formatada:
                exibir_conteudo(data_formatada, info["lin"], info["col"])
            break
        exibir_conteudo(" ", info["lin"], info["col"] - 2)
        return data_final

    def get_campos_extratos(self):
        info = self._app.campos_consulta_extrato["id_conta"]
        conta_dto = self.get_conta(info)
        if self._cancelar:
            return None, None, None
        info_conta = self._app.campos_consulta_extrato["id_conta"]
        info_nome = self._app.campos_consulta_extrato["nome_cliente"]
        exibir_conteudo(str(conta_dto.conta.id).rjust(info_conta["size"], " "), info_conta["lin"], info_conta["col"])
        exibir_conteudo(conta_dto.nome_cliente[:info_nome["size"]].ljust(info_nome["size"], " "), info_nome["lin"], info_nome["col"])
        data_inicial = self.get_data_inicial()
        if self._cancelar:
            return None, None, None
        data_final = self.get_data_final(data_inicial)
        if self._cancelar:
            return None, None, None
        return conta_dto, data_inicial, data_final

    def consulta_saldo(self):
        info = self._app.campos_consulta_saldo["id_conta"]
        self._tipo_consulta = 1
        while True:
            self._app.desenhar_consulta_saldo()
            conta_dto = self.get_conta(info)
            if self._cancelar:
                return
            self._app.exibir_dados_conta(conta_dto)

    def consulta_extratos(self, opcao="N"):
           
        while True:
            if opcao == "R":
                break
            if opcao not in operacoes_disponiveis["opcoes_consultas"]:
                exibir_mensagem("Opção inválida! Tente Novamente!", wait_key=True)
                continue
            match opcao:
                case "N":
                    self._app.desenhar_consulta_extratos()
                    conta_dto, data_inicial, data_final = self.get_campos_extratos()
                    if self._cancelar or conta_dto == None:
                        break
                    self.aplicar_filtros(conta_dto.conta.id, data_inicial, data_final)
                    transacoes = self.buscar_pagina_atual()
                case "P":
                    if self.pagina_atual == self.total_registros:
                        exibir_mensagem("Você já está na última página", wait_key=True)
                        continue
                    transacoes = self.proxima_pagina()
                case "V":
                    if self.pagina_atual == 1:
                        exibir_mensagem("Você já está na primeira página", wait_key=True)
                        continue
                    transacoes = self.pagina_anterior()
            if not self._cancelar:
                opcao = self._app.exibir_dados_extratos(transacoes, conta_dto.conta.id)
        
    def iniciar(self):
        while True:
            self._cancelar = False
            opcao = self._app.iniciar()
            if opcao == "R":
                break
            if opcao not in operacoes_disponiveis["menu_consultas"]:
                exibir_mensagem("Opção inválida! Tente novamente!", wait_key=True)
                continue
            fl_redesenhar_tela = False
            match opcao:
                case "S":
                    self.consulta_saldo()
                case "E":
                    self.consulta_extratos()
                    fl_redesenhar_tela = True
            if fl_redesenhar_tela:
                self.recuperar_tela()

        limpar_linha()
        limpar_tela()