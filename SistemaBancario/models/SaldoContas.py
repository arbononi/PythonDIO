from datetime import datetime
from Database import banco_dados
from Models.TiposEnum import TipoTransacao

class SaldoConta:
    def __init__(self, num_conta: int, data_saldo: datetime, saldo_atual: float):
        self.num_conta = num_conta
        self.data_saldo = data_saldo
        self.saldo_atual = saldo_atual

    def to_dict(self):
        return {
            'num_conta': self.num_conta,
            'data_saldo': self.data_saldo.isoformat() if self.data_saldo else datetime.now().isoformat(),
            'saldo_atual': self.saldo_atual
        }
    
    def add_saldo(self):
        banco_dados.Lista_SaldoContas[self.num_conta] = self
        banco_dados.salvar_saldo_contas()

    def atualizar_saldo(num_conta: int, valor_movto: float, tipo_movto: TipoTransacao):
        if tipo_movto == TipoTransacao.CREDITO:
            banco_dados.Lista_SaldoContas[num_conta].saldo_atual += valor_movto
        elif tipo_movto == TipoTransacao.DEBITO:
            banco_dados.Lista_SaldoContas[num_conta].saldo_atual -= valor_movto
        banco_dados.salvar_saldo_contas()
        
    def excluir_saldo(num_conta: int):
        saldo = banco_dados.Lista_SaldoContas.pop(num_conta)
        if saldo:
            banco_dados.salvar_saldo_contas()
        return saldo
    
    def exibir_dados_saldo(self, config_tela):
        pass