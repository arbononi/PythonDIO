import os
import sqlite3
from sqlite3 import Error

CONNECTION_STRING = os.path.join(os.path.dirname(__file__), "dados", "FintechDIO.db")

class BancoDeDados:
    def __init__(self, nome_banco: str):
        self.nome_banco = nome_banco
        self.conn = None
        self.cursor = None

    def criar_banco_dados(self):
        try:
            # Conecta ao banco de dados (se não existir, ele será criado)
            self.conn = sqlite3.connect(self.nome_banco)
            self.cursor = self.conn.cursor()
            print(f'Banco de dados "{self.nome_banco}" criado ou aberto com sucesso.')
        except Error as e:
            print(f'Erro ao criar o banco de dados: {e}')

    def abrir_conexao(self):
        try:
            if not self.conn:
                self.conn = sqlite3.connect(self.nome_banco)
                self.cursor = self.conn.cursor()
            print(f'Conexão aberta com o banco de dados "{self.nome_banco}".')
        except Error as e:
            print(f'Erro ao abrir a conexão: {e}')

    def obter_registro_por_primary_key(self, tabela: str, pk: str, valor_pk):
        try:
            self.cursor.execute(f'SELECT * FROM {tabela} WHERE {pk} = ?', (valor_pk,))
            return self.cursor.fetchone()  # Retorna o primeiro registro encontrado
        except Error as e:
            print(f'Erro ao obter o registro: {e}')
            return None

    def inserir_registro(self, tabela: str, colunas: tuple, valores: tuple):
        try:
            query = f'INSERT INTO {tabela} ({", ".join(colunas)}) VALUES ({", ".join(["?" for _ in valores])})'
            self.cursor.execute(query, valores)
            self.conn.commit()
            print(f'Registro inserido na tabela {tabela} com sucesso.')
        except Error as e:
            print(f'Erro ao inserir o registro: {e}')
            self.conn.rollback()

    def atualizar_registro(self, tabela: str, colunas_valores: dict, pk: str, valor_pk):
        try:
            set_clause = ", ".join([f"{k} = ?" for k in colunas_valores.keys()])
            valores = tuple(colunas_valores.values()) + (valor_pk,)
            query = f'UPDATE {tabela} SET {set_clause} WHERE {pk} = ?'
            self.cursor.execute(query, valores)
            self.conn.commit()
            print(f'Registro da tabela {tabela} atualizado com sucesso.')
        except Error as e:
            print(f'Erro ao atualizar o registro: {e}')
            self.conn.rollback()

    def excluir_registro(self, tabela: str, pk: str, valor_pk):
        try:
            self.cursor.execute(f'DELETE FROM {tabela} WHERE {pk} = ?', (valor_pk,))
            self.conn.commit()
            print(f'Registro excluído da tabela {tabela} com sucesso.')
        except Error as e:
            print(f'Erro ao excluir o registro: {e}')
            self.conn.rollback()

    def listar_registros(self, tabela: str):
        try:
            self.cursor.execute(f'SELECT * FROM {tabela}')
            return self.cursor.fetchall()  # Retorna todos os registros
        except Error as e:
            print(f'Erro ao listar registros: {e}')
            return None

    def fechar_conexao(self):
        if self.conn:
            self.conn.close()
            print('Conexão com o banco de dados fechada.')

