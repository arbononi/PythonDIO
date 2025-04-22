''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''
from os import system as limp

def calcular_saldo(transacoes):
    saldo = 0

    # TODO: Itere sobre cada transação na lista:
    for valor in transacoes:
        # TODO: Adicione o valor da transação ao saldo
        saldo += valor
    # TODO: Retorne o saldo formatado em moeda brasileira com duas casas decimais:
    return f"R$ {saldo:.2f}"
    
limp("cls")
continuar = ""

while continuar != "N":
    entrada_usuario = input("Digite o valores: ")

    entrada_usuario = entrada_usuario.strip("[]").replace(" ", "")

    transacoes = [float(valor) for valor in entrada_usuario.split(",")]

    # TODO: Calcule o saldo com base nas transações informadas:
    resultado = calcular_saldo(transacoes)

    print(resultado)

    continuar = input("Continuar (S/N) : ").upper()