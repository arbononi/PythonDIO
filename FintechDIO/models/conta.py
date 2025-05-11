from dataclasses import dataclass, fields
from datetime import date
from models.tiposenum import TipoConta, StatusConta, TipoChavePix

@dataclass
class Conta:
    id: int
    data_abertura: date
    id_cliente: int
    tipo: TipoConta
    status: StatusConta
    limite_especial: float
    saldo_atual: float
    data_encerramento: date

    def as_tuple(self):
        return (
            self.data_abertura.isoformat(),
            self.id_cliente,
            self.tipo.value,
            self.status.value,
            self.limite_especial,
            self.saldo_atual,
            self.data_encerramento.isoformat()
        )
    
    @property
    def saldo_disponivel(self):
        return self.saldo_atual + self.limite_especial
    
@dataclass
class ContaConsulta:
    id: int
    nome_cliente: str
    telefone: str
    data_abertura: date
    status: StatusConta

    def as_tuple(self):
        return (
            self.id,
            self.nome_cliente,
            self.telefone,
            self.data_abertura.isoformat(),
            self.status.value
        )

@dataclass
class ContaDTO:
    conta: Conta
    cpf_cnpj: str
    nome_cliente: str

@dataclass
class ChavesPix:
    conta: ContaDTO
    id_conta: int
    tipo_chave: TipoChavePix
    chave_pix: str

    def as_tuble(self):
        return (
            self.id_conta,
            self.tipo_chave,
            self.chave_pix
        )