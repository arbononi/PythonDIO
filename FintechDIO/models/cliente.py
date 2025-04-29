from datetime import date
from database.banco import Banco
from models.tabela import Tabela
from models.tiposenum import TipoPessoa, StatusCliente, estados
from utils.userfunctions import date_to_iso

class Cliente(Tabela):

    def __init__(self, banco, **kwargs):
        super().__init__(banco)

        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def create_table(cls, banco):
        command_text = """
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
    telefone INTEGER NOT NULL,
    data_nascimento TEXT,
    status INTEGER NOT NULL,
    data_cadastro TEXT NOT NULL)"""
        banco.cursor, mensagem = banco.executar(query=command_text)
        if banco.cursor is None:
            return False, mensagem
        return True, None

    @classmethod
    def get_by_id(cls, banco: Banco, id:int):
        query = "Select * from clientes where id = :id"
        cursor, mensagem = banco.executar(query=query, params=(id,))
        if cursor:
            rows = cursor.fetchall()
            if len(rows) == 1:
                return cls(banco, **dict(zip([col[0] for col in cursor.description], rows[0])))
            else:
                return [cls(banco, **dict(zip([col[0] for col in cursor.description], row))) for row in rows]
        else:
            banco.mensagens.append(mensagem)
        return None
    
    @classmethod
    def get_by_cpf_cnpj(cls, banco: Banco, num_doc: str):
        query = "Select * from clientes where cpf_cnpj = :num_doc"
        cursor, mensagem = banco.executar(query=query, params=(num_doc,))
        if cursor:
            rows = cursor.fetchall()
            if len(rows) == 1:
                return cls(banco, **dict(zip([col[0] for col in cursor.description], rows[0])))
            else:
                return [cls(banco, **dict(zip([col[0] for col in cursor.description], row))) for row in rows]
        else:
            banco.mensagens.append(mensagem)
        return None

    @classmethod
    def get_all(cls, banco: Banco, condicao: str = None, params=()):
        query = "Select * from clientes"
        if condicao:
            query += " where " + condicao
        if params: 
            cursor, mensagem = banco.executar(query=query, params=params)
        else:
            cursor, mensagem = banco.executar(query=query)
        if cursor:
            rows = cursor.fetchall()
            return [cls(banco, **dict(zip([col[0] for col in cursor.description], row))) for row in rows]
        else:
            banco.mensagens.append(mensagem)
        return None
    
    def insert(cls):
        id_gerado = 0
        query = """Insert into clientes(tipo_pessoa, cpf_cnpj, nome, endereco, numero, complemento,
        bairro, cidade, uf, cep, telefone, data_nascimento, status, data_cadastro)
                     values(:tipo_pessoa, :cpf_cnpj, :nome, :endereco, :numero, :complemento, :bairro,
                :cidade, :uf, :cep, :telefone, :data_nascimento, :status, :data_cadastro);
        select seq from sqlite_sequence where name='clientes'"""
        params = (cls.tipo_pessoa, cls.cpf_cnpj, cls.nome, cls.endereco, cls.numero, cls.complemento,
                  cls.bairro, cls.cidade, cls.uf, cls.cep, cls.telefone, 
                  date_to_iso(cls.data_nascimento) if cls.data_nascimento else "", cls.status, 
                  date_to_iso(cls.data_cadastro))
        cursor, mensagem = cls.banco.executar(query=query, params=params)
        if cursor:
            rows = cursor.fetchone()
            if len(rows) == 1:
                id_gerado = rows[0][0]
        return id_gerado, mensagem
            
    def update(cls):
        query = """Update clientes set tipo_pessoa = :tipo_pessoa, cpf_cnpj = :cpf_cnpj, nome = :nome,
                          endereco = :endereco, numero = :numero, complemento = :complemento, bairro = :bairro,
                          cidade = :cidade, uf = :uf, cep = :cep, telefone = :telefone, 
                          data_nascimento = :data_nascimento, status = :status, data_cadastro = :data_cadastro
                   where id = :id"""
        params = (cls.tipo_pessoa, cls.cpf_cnpj, cls.nome, cls.endereco, cls.numero, cls.complemento, cls.bairro, 
                  cls.cidade, cls.uf, cls.cep, cls.telefone, 
                  date_to_iso(cls.data_nascimento) if cls.data_nascimento else "", cls.status, 
                  date_to_iso(cls.data_cadastro), cls.id)
        cursor, mensagem = cls.banco.executar(query=query, params=params)
        if cursor:
            return True, "Cliente atualizado com sucesso!"
        cls.banco.mensagens.append(mensagem)
        return None

    def delete(cls):
        query = "Delete from clientes where id = :id"
        cursor, mensagem = cls.banco.executar(query=query, params=(cls.id,))
        if cursor:
            return True, "Cliente excluído com sucesso!"
        cls.banco.mensagens.append(mensagem)
        return None
    
    def validar_cliente(self):
        mensagens = []
        if (self.tipo_pessoa == TipoPessoa.FISICA and len(self.cpf_cnpj) != 11) or (self.tipo_pessoa == TipoPessoa.JURIDICA and len(self.cpf_cnpj) != 14):
            mensagens.append("Número do CPF/CNPJ inválido!")
        if self.nome == "":
            mensagens.append("Nome não pode ficar em branco")
        if self.cep == 0 or not (self.cep, int):
            mensagens.append("CEP inválido")
        if not (self.data_nascimento, date):
            mensagens.append("Data de nascimento/fundação inválida")
        if self.uf not in estados:
            mensagens.append("UF inválida")
        return mensagens
    