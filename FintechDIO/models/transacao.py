from datetime import datetime
from database.banco import Banco
from models.tabela import Tabela
from models.tiposenum import TipoOperacao, TipoTransacao
from utils.userfunctions import datetime_to_iso

class Transacao(Tabela):
    def __init__(self, banco: Banco, **kwargs):
                #  id: int, data_movto: datetime, idconta: int, tipo_operacao: TipoOperacao,
                #  tipo_transacao: TipoTransacao, saldo_anterior: float, valor_movto: float,
                #  saldo_final: float, nome_autor: str, mensagem: str):
        super().__init__(banco)

        for key, value in kwargs.items():
            setattr(self, key, value)

        # self.id = id
        # self.data_movto = data_movto if data_movto else datetime.now()
        # self.idconta = idconta
        # self.tipo_operacao = tipo_operacao
        # self.tipo_transacao = tipo_transacao
        # self.saldo_anterior = saldo_anterior
        # self.valor_movto = valor_movto
        # self.saldo_final = saldo_final
        # self.nome_autor = nome_autor
        # self.mensagem = mensagem

    @classmethod
    def create_table(cls, banco):
        command_text = """
CREATE TABLE IF NOT EXISTS transacoes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_movto TEXT NOT NULL,
    idconta INTEGER NOT NULL,
    tipo_operacao INTEGER NOT NULL,
    tipo_transacao INTEGER NOT NULL,
    saldo_anterior DECIMAL NOT NULL,
    valor_movto DECIMAL NOT NULL,
    saldo_atual DECIMAL NOT NULL,
    nome_autor TEXT NOT NULL,
    mensagem TEXT NOT NULL
    )"""
        banco.cursor, mensagem = banco.executar(command_text)
        if banco.cursor is None:
            return False, mensagem
        return True, None
    
    def insert(cls):
        query = """Insert into transacoes(data_movto, idconta, tipo_operacao, tipo_transacao,
                        saldo_anterior, valor_movto, saldo_final, nome_autor, mensagem)
                    values(:data_movto, :idconta, :tipo_operacao, :tipo_transacao,
                        :saldo_anterior, :valor_movto, :saldo_final, :nome_autor, :mensagem)"""
        params = (datetime_to_iso(cls.data_movto), cls.idconta, cls.tipo_operacao.value,
                  cls.tipo_transacao.value, cls.saldo_anterior, cls.valor_movto, cls.saldo_final,
                  cls.nome_autor, cls.mensagem)
        cursor, mensagem = cls.banco.executar(query=query, params=params)
        if cursor:
            return True, "Transação inserida com sucesso!"
        return False, mensagem
    
    def update(cls):
        return False, "Transação não pode ser alterada!"

    def delete(cls):
        return False, "Transação não pode ser excluída!"

    @staticmethod
    def select(banco: Banco, idconta: int, data_inicio, data_fim):
        query = """Select * from transacoes 
                    where idconta = :idconta
                      and data_movto between :dataini and :datafim
                    order by data_movto asc"""
        params=(idconta, data_inicio, data_fim)
        cursor, mensagem = banco.executar(query, params)
        if cursor:
            return [Transacao(banco, **dict(zip([col[0] for col in cursor.description], row))) for row in cursor.fechall()]
        return None
