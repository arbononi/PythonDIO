from datetime import datetime
from models.tiposenum import TipoTransacao, TipoOperacao

class Transacao:
    def __init__(self, id: int, data_movto: datetime, numero_conta: int, tipo: TipoTransacao, operacao: TipoOperacao, saldo_anterior: float,
                 valor_movto: float, saldo_final: float, nome_autor: str):
        self.id = id
        self.data_movto = data_movto
        self.numero_conta = numero_conta
        self.tipo = tipo
        self.operacao = operacao
        self.saldo_anterior = saldo_anterior
        self.valor_movto = valor_movto
        self.saldo_final = saldo_final
        self.nome_autor = nome_autor

    def to_dict(self):
        return { 
            self.id : { f"{", ".join([f"{chave}: {valor}" for chave, valor in self.__dict__.items()])}" }
        }
