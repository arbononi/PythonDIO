from abc import ABC, abstractmethod
from datetime import datetime

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self._saldo

        if valor > saldo:
            return False, "Operação falhou! Você não tem saldo suficiente"
        elif valor > 0:
            self._saldo -= valor
            return True, "Saque realizado com sucesso!"
        
        return False, "Operação falhou. Valor informado é inválido!"

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return True, "Depósito efetuado com sucesso!"
        
        return False, "Operação falhou! Valor informado é inválido!"

        
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saque=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saque

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name___])

        if valor > self.limite:
            return False, "Operação falhou. Valor do saque excede o limite permitido"
        if numero_saques > self.limite_saque:
            return False, "Operação falhou. Número de saques permitidos atingiu o limite"
        
        return super().sacar(valor)
    
    def __str__(self):
        return f"""\n
                Agência: \t{self.agencia}
                C/C: \t\t{self.numero}
                Titular: \t{self.cliente.nome}
        """
    