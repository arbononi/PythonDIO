from database.clientes_repository import ClientesRepository
from views.clientes_view import ClientesView
from utils.userfunctions import exibir_mensagem, limpar_tela, limpar_linha

class ClientesController:
    _repo = None
    _app = None

    def __init__(self):
        self._repo = ClientesRepository()
        self._app = ClientesView()
        self.pagina_atual = 1
        self.tamanho_pagina = 29
        self.total_registros = 0
        self.total_paginas = 1
        self.filtros = {}

    def aplicar_filtros(self, nome=None, cpf_cnpj=None, cidade=None, data_nascimento=None):
        self.filtros = {
            "nome": nome,
            "cpf_cnpj": cpf_cnpj,
            "cidade": cidade,
            "data_nascimento": data_nascimento
        }
        self.pagina_atual = 1  # Reinicia ao aplicar filtros

    def buscar_pagina_atual(self):
        clientes, total, _ = self._repo.buscar_com_filtros(
            filtros=self.filtros,
            pagina=self.pagina_atual,
            tamanho_pagina=self.tamanho_pagina
        )
        self.total_registros = total
        self.total_paginas = max(1, (total + self.tamanho_pagina - 1) // self.tamanho_pagina)
        return clientes
    
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

    def consultar_cliente(self):
        cliente_id = self._app.get_cliente_id()
        if cliente_id == 0:
            return
        cliente, mensagem = self._repo.get_by_id(cliente_id)
        if not cliente:
            exibir_mensagem(mensagem, wait_key=True)
            return
        self._app.exibir_dados_cliente(cliente, True)

    def incluir_cliente(self):
        cliente = self._app.incluir_cliente()
        if cliente:
            fl_ok, novo_id, mensagem = self._repo.add(cliente)
            if not fl_ok:
                exibir_mensagem(mensagem, wait_key=True)
            else:
                exibir_mensagem(f"Cliente incluído com sucesso. Código gerado: {novo_id}", wait_key=True)

    def alterar_cliente(self):
        cliente_id = self._app.get_cliente_id()
        if cliente_id == 0:
            return
        cliente, mensagem = self._repo.get_by_id(cliente_id)
        if not cliente:
            exibir_mensagem(mensagem, wait_key=True)
            return
        self._app.exibir_dados_cliente(cliente)
        cliente = self._app.alterar_cliente(cliente)
        if cliente:
            fl_ok, mensagem = self._repo.update(cliente)
            if not fl_ok:
                exibir_mensagem(mensagem, wait_key=True)
            else:
                exibir_mensagem("Cliente atualizado com sucesso!", wait_key=True)

    def excluir_cliente(self):
        cliente_id = self._app.get_cliente_id()
        if cliente_id == 0:
            return
        cliente, mensagem = self._repo.get_by_id(cliente_id)
        if not cliente:
            exibir_mensagem(mensagem, wait_key=True)
            return
        self._app.exibir_dados_cliente(cliente)
        if self._app.excluir_cliente():
            fl_ok, mensagem = self._repo.delete_by_id(cliente_id)
            if not fl_ok:
                exibir_mensagem(mensagem, wait_key=True)
            else:
                exibir_mensagem("Cliente excluído com sucesso!", wait_key=True)

    def listar_clientes(self):
        clientes = self.buscar_pagina_atual()
        while True:
            opcao = self._app.exibir_lista_clientes(clientes)
            if opcao == "R":
                break
            match opcao:
                case "N":
                    tipo_consulta, filtro = self._app.nova_consulta()
                    if not tipo_consulta:
                        continue
                    match tipo_consulta:
                        case 1:
                            self.aplicar_filtros(nome=filtro)
                        case 2:
                            self.aplicar_filtros(cpf_cnpj=filtro)
                        case 3:
                            self.aplicar_filtros(cidade=filtro)
                        case 4:
                            self.aplicar_filtros(data_nascimento=filtro)
                    clientes = self.buscar_pagina_atual()
                case "P":
                    if self.pagina_atual == self.total_paginas:
                        exibir_mensagem("Você já está na última página", wait_key=True)
                        continue
                    clientes = self.proxima_pagina()
                case "V":
                    if self.pagina_atual == self.total_paginas:
                        exibir_mensagem("Você já está na primeira página", wait_key=True)
                        continue
                    clientes = self.pagina_anterior()

    def iniciar(self):
        while True:
            opcao = self._app.iniciar()
            if opcao == "R":
                break
            match opcao:
                case "C":
                    self.consultar_cliente()
                    continue
                case "I":
                    self.incluir_cliente()
                    continue
                case "A":
                    self.alterar_cliente()
                    continue
                case "E":
                    self.excluir_cliente()
                    continue
                case "L":
                    self.aplicar_filtros()
                    self.listar_clientes()
                    continue

        limpar_tela()
        limpar_linha()