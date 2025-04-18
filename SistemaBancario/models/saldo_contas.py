from datetime import datetime

class SaldoConta:
    def __init__(self, num_conta: int, data_saldo: datetime, saldo_atual: float):
        self.num_conta = num_conta
        self.data_saldo = data_saldo
        self.data_saldo = saldo_atual