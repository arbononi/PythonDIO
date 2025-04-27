from datetime import date
from database.banco import Banco
from models.tabela import Tabela

class Versao(Tabela):
    _versao = 1
    _release = 2025
    _build = 4
    _compile = 0

    def __init__(self, banco, **kwargs):
        super().__init__(banco)

        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def create_table(cls, banco):
        command_text = """
CREATE TABLE IF NOT EXISTS versoes(
    versao INTEGER NOT NULL PRIMARY KEY,
    release INTEGER NOT NULL,
    build INTEGER NOT NULL,
    compile INTEGER NOT NULL
    )"""
        banco.cursor, mensagem = banco.executar(command_text)
        if banco.cursor is None:
            return False, mensagem
        return True, None

    @classmethod
    def get_by_id(cls, banco: Banco, versao:int):
        query = "Select * from versoes where versao = :versao"
        cursor, mensagem = banco.executar(query=query, params=(versao,))
        if cursor:
            rows = cursor.fetchall()
            if len(rows) == 1:
               return cls(banco, **dict(zip([col[0] for col in cursor.description], rows[0])))
        banco.mensagens.append(mensagem)
        return None

    def insert(cls):
        query = "Insert into versoes(versao, release, build, compile) values(:versao, :release, :build, :compile)"
        cursor, mensagem = cls.banco.executar(query=query, params=(cls.versao, cls.release, cls.build, cls.compile))
        if cursor is None:
            cls.banco.mensagens.append(mensagem)
        return cursor
    
    def update(cls):
        query = "Update versoes set release = :release, build = :build, compile =: compile where versao = :versao"
        cursor, mensagem = cls.banco.executar(query=query, params=(cls.versao, cls.release, cls.build, cls.compile))
        if cursor is None:
            cls.banco.mensagens.append(mensagem)
        return cursor
    
    def delete(cls):
        query = "Delete from versoes where versao = :versao"
        cursor, mensagem = cls.banco.executar(query=query, params=(cls.versao,))
        if cursor is None:
            cls.banco.mensagens.append(mensagem)
        return cursor
    

