from datetime import date
from typing import List, Tuple, Optional
from database.banco import Banco
from database.filtro_sql import FiltroSQL
from models.cliente import Cliente
from database.base_repository import BaseRepository

class ClientesRepository(BaseRepository[Cliente]):
    def __init__(self):
        super().__init__(Banco.get_instance(), Cliente, "clientes")

    def create_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS clientes(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          tipo_pessoa INTEGER NOT NULL,
          cpf_cnpj TEXT NOT NULL,
          nome TEXT NOT NULL,
          endereco TEXT NOT NULL,
          numero TEXT NOT NULL,
          complemento TEXT NOT NULL,
          bairro TEXT NOT NULL,
          cidade TEXT NOT NULL,
          uf TEXT NOT NULL,
          cep INTEGER NOT NULL,
          telefone TEXT NOT NULL,
          data_nascimento TEXT,
          status INTEGER NOT NULL,
          data_cadastro TEXT NOT NULL
        )"""
        return self.banco.executar(sql)

    def buscar_com_filtros(self, filtros: dict, pagina: int=1, tamanho_pagina: int=29):
        filtros_sql = FiltroSQL()
        filtros_sql.adicionar_like("nome", filtros.get("nome"))
        filtros_sql.adicionar_like("cpf_cnpj", filtros.get("cpf_cnpj"))
        filtros_sql.adicionar_like("cidade", filtros.get("cidade"))
        filtros_sql.adicionar_igual("data_nascimento", filtros.get("data_nascimento"))

        where_sql = filtros_sql.where_clause()
        params = filtros_sql.get_params()

        offset = (pagina - 1) * tamanho_pagina
        query = f"""
        select * from clientes
        {where_sql}
        order by nome
        limit ? offset ?
        """

        params.extend([tamanho_pagina, offset])
        cursor, mensagem = self.banco.executar(query, params)
        if not cursor:
            return [], mensagem
        
        rows = cursor.fetchall()
        clientes = [self._from_row(row) for row in rows]

        # Total de registros
        count_query = f"SELECT COUNT(*) FROM clientes {where_sql}"
        cursor_count, _ = self.banco.executar(count_query, filtros_sql.get_params())
        total = cursor_count.fetchone()[0] if cursor_count else 0
        return clientes, total, mensagem
    
    def listar_clientes(self, nome: Optional[str] = None, cpf_cnpj: Optional[str] = None,
                        cidade: Optional[str] = None, data_nascimento: Optional[date]=None,
                        limit: int=29, offset: int = 0) -> Tuple[List[Cliente], Optional[str]]:
        filtro = FiltroSQL()
        filtro.adicionar_like("nome", nome)
        filtro.adicionar_like("cpf_cnpj", cpf_cnpj)
        filtro.adicionar_like("cidade", cidade)
        filtro.adicionar_igual("data_nascimento", data_nascimento.isoformat() if data_nascimento else None)

        where = filtro.where_clause()
        params = filtro.get_params()

        query = f"""
        SELECT * FROM clientes
        {where}
        ORDER by nome
        LIMIT ? OFFSET ?
        """

        params.extend([limit, offset])
        cursor, mensagem = self.banco.executar(query, params)
        if not cursor:
            return [], mensagem
        
        rows = cursor.fetchall()
        clientes = [self._from_row(row) for row in rows]
        return clientes, None

    def search_by_name(self, nome: str, limit=29, offset=0):
        sql = """
          SELECT * FROM clientes
          WHERE nome LIKE ?
          ORDER BY nome
          LIMIT ? OFFSET ?
        """
        cur, err = self.banco.executar(sql, (f"%{nome}%", limit, offset))
        rows = cur.fetchall() if cur else []
        return ([self._from_row(r) for r in rows], "") if cur else ([], err)

    def count_by_name(self, nome: str):
        sql = "SELECT COUNT(*) as total FROM clientes WHERE nome LIKE ?"
        cur, err = self.banco.executar(sql, (f"%{nome}%",))
        return (cur.fetchone()["total"], "") if cur else (0, err)

    def contar_com_filtros(self, nome: Optional[str] = None, cpf_cnpj: Optional[str] = None,
                           cidade: Optional[str] = None, data_nascimento: Optional[date] = None) -> Tuple[int, Optional[str]]:
        filtro = FiltroSQL()
        filtro.adicionar_like("nome", nome)
        filtro.adicionar_like("cpf_cnpj", cpf_cnpj)
        filtro.adicionar_like("cidade", cidade)
        filtro.adicionar_igual("data_nascimento", data_nascimento.isoformat() if data_nascimento else None)

        where = filtro.where_clause()
        params = filtro.get_params()

        query = f"""
        SELECT COUNT(*) as total FROM clientes
        {where}
        """

        cursor, mensagem = self.banco.executar(query, params)
        if not cursor:
            return 0, mensagem

        total = cursor.fetchone()[0]
        return total, None

    def get_by_cpf_cnpj(self, cpf_cnpj: str) -> Cliente:
        if cpf_cnpj == "":
            return None, "CPF/CNPJ não informado para consulta"
        filtros = FiltroSQL()
        filtros.adicionar_igual("cpf_cnpj", cpf_cnpj)
        
        where = filtros.where_clause()
        params = filtros.get_params()

        query = f"select * from clientes {where}"
        cursor, mensagem = self.banco.executar(query, params)

        if not cursor:
            return None, mensagem
        row = cursor.fetchone()
        return (self._from_row(row), "") if row else (None, "CPF/CNPJ não encontrado!")
    