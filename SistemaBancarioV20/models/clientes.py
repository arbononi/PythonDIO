from datetime import date
from models.tiposenum import TipoPessoa, StatusCliente

class Cliente:
    def __init__(self, tipo_pessoa: TipoPessoa, cpf_cnpj: str, nome: str, endereco: str, numero: str, complemento: str,
                 bairro: str, cidade: str, estado: str, cep: int, telefone: str, status: StatusCliente, data_cadastro: date):
        self.tipo_pessoa = tipo_pessoa
        self.cpf_cnpj = cpf_cnpj
        self.nome = nome
        self.endereco = endereco
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.telefone = telefone,
        self.status = status
        self.data_cadastro = data_cadastro

    # def __str__(self):
    #     pass

    def to_dict(self):
        return {
            "tipo_pessoa" : self.tipo_pessoa.value,
            "cpf_cnpj" : self.cpf_cnpj,
            "nome" : self.nome,
            "endereco" : self.endereco,
            "numero" : self.numero,
            "complemento" : self.complemento,
            "bairro" : self.bairro,
            "cidade" : self.cidade,
            "estado" : self.estado,
            "cep" : self.cep,
            "telefone": self.telefone,
            "status" : self.status.name,
            "data_cadastro" : self.data_cadastro.isoformat()
        }
    
    def set_status(self, status: int):
        self.status = status
    
    def get_status(self):
        return self.status