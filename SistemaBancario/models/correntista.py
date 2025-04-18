from datetime import datetime, date
from tiposenum import StatusCorrentista

class Correntista:
    def __init__(self, num_cpf: int, nome: str, endereco: str, numero: str, complemento: str, bairro: str,
                 cidade: str, uf: str, cep: int, data_nasc: date, telefone: str, status : StatusCorrentista, data_cadastro: date):
        self.num_cpf = num_cpf
        self.nome = nome
        self.endereco = endereco
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep
        self.data_nasc = data_nasc
        self.telefone = telefone
        self.status = status
        self.data_cadastro = data_cadastro