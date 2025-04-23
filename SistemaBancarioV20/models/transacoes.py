from datetime import datetime
from models.tiposenum import TipoTransacao, TipoOperacao

class Transacao:
    def __init__(self, id: int, data_movto: datetime, numero_conta: int, tipo: TipoTransacao, operacao: TipoOperacao, saldo_anterior: float,
                 valor_movto: float, saldo_final: float):
        self.id = id
        self.data_movto = data_movto
        self.numero_conta = numero_conta
        self.tipo = tipo
        self.operacao = operacao
        self.saldo_anterior = saldo_anterior
        self.valor_movto = valor_movto
        self.saldo_final = saldo_final

    def to_dict(self):
        return {
            "id" : self.id,
            "data_movto" : self.data_movto.isoformat(),
            "numero_conta" : self.numero_conta,
            "tipo" : self.tipo.name,
            "operacao" : self.operacao.name,
            "saldo_anterior" : self.saldo_anterior,
            "valor_movto" : self.valor_movto,
            "saldo_final" : self.saldo_final
        }