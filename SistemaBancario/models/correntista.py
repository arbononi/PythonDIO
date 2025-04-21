from datetime import date
from enum import Enum
from Models.TiposEnum import StatusCorrentista
from Utils import user_functions
from Utils.user_functions import posicionarCursor
from Database import banco_dados

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

    def to_dict(self):
        return {
            "num_cpf": self.num_cpf,
            "nome": self.nome,
            "endereco": self.endereco,
            "numero": self.numero,
            "complemento": self.complemento,
            "bairro": self.bairro,
            "cidade": self.cidade,
            "uf": self.uf,
            "cep": self.cep,
            "data_nasc": self.data_nasc.isoformat(),
            "telefone": self.telefone,
            "status": str(self.status.name),
            "data_cadastro": self.data_cadastro.isoformat()
        }   
    

    def add_correntista(self):
        banco_dados.Lista_Correntistas[self.num_cpf] = self
        banco_dados.salvar_correntistas()

    def get_correntista_por_cpf(num_cpf: int):
        return banco_dados.Lista_Correntistas.get(num_cpf)

    def excluir_correntista(num_cpf: int):
        return banco_dados.Lista_Correntistas.pop(num_cpf, None)

    def exibir_dados_em_tela(self, config_tela):
        for campo, valor in vars(self).items():
            layout = config_tela.get(campo)
            if not layout:
                continue
            if campo == "status":
                name = valor.name.lower()
                posicionarCursor(layout["lin"], layout[name])
                print("•")
                continue
            else:
                posicionarCursor(layout["lin"], layout["col"]) 
            if campo == "num_cpf":
               print(user_functions.formatar_cpf(valor)) 
            elif isinstance(valor, date):
                print(user_functions.formatar_data(valor))
                if campo == "data_nasc":
                    info = config_tela.get("idade")
                    if info:
                        posicionarCursor(info["lin"], info["col"])
                        print(str(Correntista.get_idade(self.data_nasc)).rjust(3, " "))
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
    
    def get_status_by_name(name: str):
        if name == StatusCorrentista.RESTRITO.name:
            return StatusCorrentista.RESTRITO
        elif name == StatusCorrentista.INATIVO.name:
            return StatusCorrentista.INATIVO
        else:
            return StatusCorrentista.ATIVO