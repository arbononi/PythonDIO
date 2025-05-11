from dataclasses import dataclass
from datetime import date
from models.tiposenum import TipoPessoa, StatusCliente

@dataclass
class Cliente:
    id: int
    tipo_pessoa: TipoPessoa
    cpf_cnpj: str
    nome: str
    endereco: str
    numero: str
    complemento: str
    bairro: str
    cidade: str
    uf: str
    cep: int
    telefone: str
    status: StatusCliente
    data_nascimento: date
    data_cadastro: date

    def as_tuple(self):
        return (
            self.tipo_pessoa.value,
            self.cpf_cnpj,
            self.nome,
            self.endereco,
            self.numero,
            self.complemento,
            self.bairro,
            self.cidade,
            self.uf,
            self.cep,
            self.telefone,
            self.data_nascimento.isoformat(),
            self.status.value,
            self.data_cadastro.isoformat()
        )    
    