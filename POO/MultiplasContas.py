class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

class SistemaBancario:
    def __init__(self):
        self.listaconta = []

    def criar_conta(self, titular, saldo):
        self.listaconta.append(ContaBancaria(titular, saldo))

    def listar_contas(self):
        result = ""
        for conta in self.listaconta:
            if result != "":
                result += f", {conta.titular}: R$ {conta.saldo}"
            else: 
                result = f"{conta.titular}: R$ {conta.saldo}"
        print(result)

sistema = SistemaBancario()

while True:
    print()
    print("Informe o nome do Titular e o saldo inicial ou fim para encerrar")
    entrada = input().strip()
    if entrada.upper() == "FIM":  
        break
    titular, saldo = entrada.split(", ")
    sistema.criar_conta(titular, int(saldo))

sistema.listar_contas()
