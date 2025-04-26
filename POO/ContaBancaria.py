class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
        self.transacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append(f"+{valor}")

    def sacar(self, valor):
        if (valor * -1) > self.saldo:
            self.transacoes.append("Saque não permitido")
        else:
            self.saldo += valor
            self.transacoes.append(valor)

    def saldo_atual(self):
        return f"Saldo: {self.saldo}"
    
    def extrato(self):
        print(f"Operações: {", ".join([f"{valor}" for valor in self.transacoes])}; Saldo: {self.saldo}")

print()
nome_titular = input("Nome do titular: ").strip()
conta = ContaBancaria(nome_titular)

entrada_transacoes = input("Informe o valor das operações separadas por vírgulas: ").strip()
transacoes = [int(valor) for valor in entrada_transacoes.split(",")]

for valor in transacoes:
    if valor > 0:
        conta.depositar(valor)
    else:
        conta.sacar(valor)

conta.extrato()