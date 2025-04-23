from datetime import date
from models.tiposenum import TipoConta, StatusConta

class Conta:
    def __init__(self, numero: int, data_abertura: date, cpf_cnpj: str, tipo: TipoConta, 
                 valor_limite: float, saldo_atual: float, status: StatusConta, data_encerramento = None):
        self.numero = numero
        self.data_abertura = data_abertura
        self.cpf_cnpj = cpf_cnpj
        self.tipo = tipo
        self._valor_limite = valor_limite
        self._saldo_atual = saldo_atual
        self.status = status
        self.data_encerramento = data_encerramento

    @property
    def valor_disponivel(self):
        saldo_atual = self._saldo_atual or 0
        valor_limite = self._valor_limite or 0
        return saldo_atual + valor_limite

    def to_dict(self):
        return {
            "numero" : self.numero,
            "data_abertura" : self.data_abertura.isoformat(),
            "cpf_cnpj" : self.cpf_cnpj,
            "tipo" : self.tipo.name,
            "valor_limite" : self.valor_limite,
            "saldo_atual" : self._saldo_atual,
            "status" : self.status.name,
            "data_encerramento" : self.data_encerramento.isoformat() if self.data_encerramento else None
        }
    
    def depositar(self, valor: float):
        saldo_atual = self._saldo_atual or 0
        if valor <= 0:
            return False, "Valor de depósito dever ser superior a zero!"
        self._saldo_atual = saldo_atual + valor
    
        return True, "Depósito efetuado com sucesso!"
    
    def sacar(self, valor: float):
        saldo_atual = self._saldo_atual or 0
        valor_limite = self._valor_limite or 0
        if valor <= 0:
            return False, "Valor do saque dever ser superior a zero!"
        elif valor > self.valor_disponivel:
            return False, "Saldo disponível insuficiente para o saque!"
        elif valor > 500.0:
            return False, "Valor do saque maior que limite permitido!"
        self._saldo_atual = saldo_atual - valor
        return True, "Saque efetuado com sucesso!"
        