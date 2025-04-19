from datetime import datetime, date
from enum import Enum
from models.tiposenum import StatusCorrentista
from utils import user_functions
from utils.user_functions import posicionarCursor

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

    def exibir_dados_em_tela(self, config_tela):
        for campo, valor in vars(self).items():
            layout = config_tela[campo]
            if campo == "status":
                if valor == StatusCorrentista.RESTRITO:
                    layout1 = layout["restrito"]
                elif valor == StatusCorrentista.INATIVO:
                    layout1 = layout["inativo"]
                else:
                    layout1 = layout["ativo"]
                posicionarCursor(layout1["lin"], layout1["col"])
                print("X")
            posicionarCursor(layout["lin"], layout["col"]) 
            if campo == "num_cpf":
               print(user_functions.formatar_cpf(valor)) 
            elif isinstance(valor, date):
                print(user_functions.formatar_data(valor))
            elif isinstance(valor, Enum):
                print(valor.name)
            else:
                print(valor)
    
    def validar_nome(nome: str):
        if nome == "":
            return False, "Nome do Correntista não pode ficar em branco!"
        return True, None
    
    def get_idade(data: date):
        idade = date.today().year - data.year
        if (date.today().month < data.month or (date.today().month == data.month and date.today().day < data.day)):
            idade -= 1
        return idade
