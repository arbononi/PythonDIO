from dataclasses import fields
from datetime import datetime
from database.banco import Banco
from database.filtro_sql import FiltroSQL
from database.base_repository import BaseRepository
from database.contas_repository import ContasRepository
from models.transacao import Transacao, TransacaoDTO
from models.conta import ContaDTO

class TransacoesRepository(BaseRepository[Transacao]):
    def __init__(self, contas_repository: ContasRepository):
        super().__init__(Banco.get_instance(), Transacao, "transacoes")
        self.contas_repository = contas_repository

    def create_table(self):
        sql = """
        CREATE TABLE "transacoes" (
	      "id"               INTEGER,
	      "data_movto"       TEXT NOT NULL,
	      "id_conta_origem"  INTEGER NOT NULL,
          "id_conta_destino" INTEGER NOT NULL,
	      "tipo_operacao"    INTEGER NOT NULL,
	      "tipo_transacao"   INTEGER NOT NULL,
          "tipo_chave_pix"   INTEGER NOT NULL,
          "chave_pix"        TEXT NOT NULL,
          "linha_digitavel"  TEXT NOT NULL,
	      "saldo_anterior"   DECIMAL NOT NULL,
	      "valor_movto"	     DECIMAL NOT NULL,
	      "saldo_final"	     DECIMAL NOT NULL,
	      "nome_autor"	     TEXT NOT NULL,
	      "mensagem"	     TEXT NOT NULL,
	    PRIMARY KEY("id" AUTOINCREMENT)
        );"""
        return self.banco.executar(sql)

    def get_by_id(self, id: int):
        try:
            transacao, _ = super().get_by_id(id)
            if not transacao:
                return None, "Transação não encontrada"
            conta_dto_origem = self.contas_repository.get_by_id(transacao.id_conta_origem)
            conta_dto_destino = self.contas_repository.get_by_id(transacao.id_conta_destino)

            return TransacaoDTO(
                transacao = transacao,
                conta_dto_origem = conta_dto_origem if conta_dto_origem else None,
                conta_dto_destino = conta_dto_destino if conta_dto_destino else None
            )
        except Exception as ex:
            return None, f"Erro ao obter dados da transação: {ex}"
    
    def buscar_com_filtros(self, filtros: dict, pagina:int=1, tamanho:int=21):
        try:
            query = """
            Select * from transacoes
                where (id_conta_origem = :id_conta or id_conta_destino = :id_conta) 
                and data_movto between :data_inicial and :data_final
                order by data_movto
                limit :limite offset :salto"""
            offset = (pagina - 1) * tamanho
            params = {
                "id_conta": filtros.get("id_conta"),
                "data_inicial" : filtros.get("data_inicial"),
                "data_final" : filtros.get("data_final"),
                "limite": tamanho,
                "salto": offset
            }
            cursor, _ = self.banco.executar(query, params)
            if not cursor:
                return None, 0, "Nenhuma transação encontrada"
            rows = cursor.fetchall()
            transacoes = [self._from_row(row) for row in rows]
            
            count_query = """Select count(*) from transacoes
                where (id_conta_origem = :id_conta or id_conta_destino = :id_conta) 
                and data_movto between :data_inicial and :data_final
            """
            cursor_count, _ = self.banco.executar(count_query, params)
            total = cursor_count.fetchone()[0] if cursor_count else 0
            return transacoes, total, "Consulta realizada com sucesso!"            
        except Exception as ex:
            raise ex
