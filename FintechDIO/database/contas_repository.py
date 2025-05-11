from dataclasses import fields
from datetime import date
from typing import List, Tuple, Optional
from database.banco import Banco
from database.filtro_sql import FiltroSQL
from database.base_repository import BaseRepository
from database.clientes_repository import ClientesRepository
from models.conta import Conta, ContaConsulta, ContaDTO, ChavesPix
from models.tiposenum import TipoOperacao, TipoChavePix

class ContasRepository(BaseRepository[Conta]):
    def __init__(self, cliente_repository: ClientesRepository):
        super().__init__(Banco.get_instance(), Conta, "contas")
        self.cliente_repository = cliente_repository
        
    def create_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS contas(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          data_abertura TEXT NOT NULL,
          id_cliente INTEGER NOT NULL,
          tipo INTEGER NOT NULL,
          status INTEGER NOT NULL,
          limite_especial DECIMAL NOT NULL,
          saldo_atual DECIMAL NOT NULL,
          data_encerramento TEXT
        )"""
        return self.banco.executar(sql)

    def get_by_id(self, id_conta:int):
        try:
            conta, _ = super().get_by_id(id_conta)
            if not conta:
                return None, "Conta não cadastrada!"
            cliente, _ = self.cliente_repository.get_by_id(conta.id_cliente)
            nome_cliente = cliente.nome if cliente else "Cliente não cadastrado"
            cpf_cnpj = cliente.cpf_cnpj if cliente else ""
            return ContaDTO(
                conta=conta,
                nome_cliente=nome_cliente,
                cpf_cnpj=cpf_cnpj
            ), ""
        
        except Exception as error:
            return None, f"Erro ao obter dados da conta: {error}"
    
    def atualizar_saldo(self, id_conta: int, valor_operacao: float, tipo_operacao: TipoOperacao):
        query = """
           Update contas Set saldo_atual = case when :tipo_operacao = 1 then saldo_atual + :valor_operacao
                      else saldo_atual - :valor_operacao end 
            where id = :id_conta"""
        params = {
            "tipo_operacao" : tipo_operacao.value,
            "valor_operacao" : valor_operacao,
            "id_conta" : id_conta
        }

        cursor, mensagem = self.banco.executar(query, params)
        if not cursor:
            return False, mensagem
        return True, "Saldo atualizado com sucesso!"
    
    def listar_contas(self, limite: int=21, offset:int=0) -> list[ContaConsulta]:
        query = """Select c.id, cli.nome as nome_cliente, cli.telefone, c.data_abertura, c.status
        from contas c
        left join clientes cli on cli.id = c.id_cliente
        order by cli.nome
        LIMIT ? OFFSET ?"""
        params = [limite, offset]
        cursor, mensagem = self.banco.executar(query, params)
        if not cursor:
            return None, mensagem
        rows = cursor.fetchall()
        lista_contas = []
        for row in rows:
            kwargs = {}
            for f in fields(ContaConsulta):
                v = row[f.name]
                if hasattr(f.type, "__members__"):
                    v = f.type(v)
                elif f.type.__name__=="date" and v:
                    v = date.fromisoformat(v)
                kwargs[f.name] = v
            lista_contas.append(ContaConsulta(**kwargs))
        if len(lista_contas) > 0:
            return lista_contas, "Consulta efetuada com sucesso!"
        return None, "Nenhuma conta encontrada"
                
