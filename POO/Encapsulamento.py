from os import system as limp

class Conta:
    def __init__(self, nro_agencia, saldo):
        self.nro_agencia = nro_agencia
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor
    
    def exibir_saldo(self):
        return f"{self._saldo:.2f}"



print("cls")
conta = Conta("001", 100)
print(conta.nro_agencia, conta.exibir_saldo())