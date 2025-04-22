from datetime import datetime, date
from database import banco_dados
from models.tiposenum import TipoTransacao

class SaldoConta:
    def __init__(self, num_conta: int, data_saldo: date, saldo_atual: float):
        self.num_conta = num_conta
        self.data_saldo = data_saldo
        self.saldo_atual = saldo_atual

    def to_dict(self):
        return {
            'num_conta': self.num_conta,
            'data_saldo': self.data_saldo.isoformat() if self.data_saldo else date.today().isoformat(),
            'saldo_atual': self.saldo_atual
        }
    
    def add_saldo(self):
        banco_dados.Lista_SaldoContas[self.num_conta] = self
        banco_dados.salvar_saldo_contas()

    def atualizar_saldo(num_conta: int, valor_movto: float, tipo_movto: TipoTransacao):
        saldo = banco_dados.Lista_SaldoContas.get(num_conta)
        if saldo is None:
            saldo = SaldoConta(num_conta, date.today(), 0)
            SaldoConta.add_saldo(saldo)
        if tipo_movto == TipoTransacao.DEPOSITO:
            banco_dados.Lista_SaldoContas[num_conta].saldo_atual += valor_movto
        elif tipo_movto == TipoTransacao.SAQUE:
            banco_dados.Lista_SaldoContas[num_conta].saldo_atual -= valor_movto
        banco_dados.Lista_SaldoContas[num_conta].data_saldo = date.today()
        banco_dados.salvar_saldo_contas()
        
    def excluir_saldo(num_conta: int):
        saldo = banco_dados.Lista_SaldoContas.pop(num_conta)
        if saldo:
            banco_dados.salvar_saldo_contas()
        return saldo
    
    def exibir_dados_saldo(self, config_tela):
        pass