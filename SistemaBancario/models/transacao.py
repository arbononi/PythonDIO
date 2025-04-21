from Models.TiposEnum import TipoTransacao
from datetime import datetime

class Transacao:
    def __init__(self, id: int, data_movto : datetime, idconta: int, tipo_transacao: TipoTransacao,
                 saldo_anterior: float, valor_transacao: float, saldo_atual: float, flag_conciliada : bool):
        self.id = id
        self.data_movto = data_movto
        self.idconta = idconta
        self.tipo_transacao = tipo_transacao
        self.saldo_anterior = saldo_anterior
        self.valor_transacao = valor_transacao
        self.saldo_atual = saldo_atual
        self.flag_conciliada = flag_conciliada

    def to_dict(self):
        return {
            "id": self.id,
            "data_movto": self.data_movto.isoformat(),
            "idconta": self.idconta,
            "tipo_transacao": self.tipo_transacao.name,
            "saldo_anterior": self.saldo_anterior,
            "valor_transacao": self.valor_transacao,
            "saldo_atual": self.saldo_atual,
            "flag_conciliada": self.flag_conciliada
        }