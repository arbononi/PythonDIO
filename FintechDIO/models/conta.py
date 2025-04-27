from datetime import date
from database.banco import Banco
from models.tabela import Tabela
from models.tiposenum import TipoConta, StatusConta
from utils.userfunctions import date_to_iso

class Conta(Tabela):
    def __init__(self, banco, **kwargs):
        super().__init__(banco)

        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def saldo_disponivel(self):
        return self.saldo_atual + self.limite_especial

    @classmethod
    def create_table(cls, banco):
        command_text = """
CREATE TABLE IF NOT EXISTS contas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_abertura TEXT NOT NULL,
    idcliente INTEGER NOT NULL,
    tipo INTEGER NOT NULL,
    status INTEGER NOT NULL,
    limite_especial DECIMAL NOT NULL,
    saldo_atual DECIMAL NOT NULL,
    data_encerramento TEXT
    )"""
        banco.cursor, mensagem = banco.executar(query=command_text)
        if banco.cursor is None:
            return False, mensagem
        return True, None

    @classmethod
    def get_by_id(cls, banco: Banco, id:int):
        query = "Select * from contas where id = :id"
        cursor, mensagem = banco.executar(query=query, params=(id,))
        if cursor:
            rows = cursor.fetchall()
            if len(rows) == 1:
                return cls(banco, **dict(zip([col[0] for col in cursor.description], rows[0])))
        banco.mensagens.append(mensagem)
        return None
                
    def insert(cls):
        id_gerado = 0
        query = """Insert into contas(data_abertura, idcliente, tipo, status, limite_especial, saldo_atual, data_encerramento)
        values(:data_abertura, :idcliente, :tipo, :status, :limite_especial, :saldo_atual, :data_encerramento);
        select seq from sqlite_sequence where name = 'contas'"""
        params = (date_to_iso(cls.data_abertura), cls.idcliente, cls.tipo.value, cls.status.value, cls.limite_especial,
                  cls.saldo_atual, date_to_iso(cls.data_encerramento) if cls.data_encerramento else "")
        cursor, mensagem = cls.banco.executar(query, params)
        if cursor:
            rows = cursor.fetchall()
            if len(rows) == 1:
                id_gerado = rows[0][0]
        return id_gerado, mensagem

    def update(cls):
        query = """Update contas set data_abertura = :data_abertura, idcliente = :idcliente, tipo = :tipo, 
                       status = :status, limite_especial = :limite_especial, 
                       saldo_atual = :saldo_atual, data_encerramento = :data_encerramento
                    where id = : id"""
        params = (date_to_iso(cls.data_abertura), cls.idcliente, cls.tipo.value, cls.status.value, cls.limite_especial,
                  cls.saldo_atual, date_to_iso(cls.data_encerramento) if cls.data_encerramento else "", cls.id)
        cursor, mensagem = cls.banco.executar(query, params)
        if cursor:
            return True, "Conta atualizada com sucesso!"
        return False, mensagem

    def delete(cls):
        query = "Delete from contas where id = :id"
        cursor, mensagem = cls.banco.executar(query=query, params=(id,))
        if cursor:
            return True, "Conta excluída com sucesso!"
        return False, mensagem

    def select(self):
        pass
