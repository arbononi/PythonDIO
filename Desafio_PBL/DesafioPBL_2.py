def filtrar_transacoes(transacoes, limite):
    transacoes_filtradas = []

    # TODO: Itere sobre cada transação na lista:
    for t in transacoes:
        # TODO: Verifique se o valor absoluto da transação é maior que o limite:
        if abs(t) > limite:
            # TODO: Adicione a transação à lista filtrada:
            transacoes_filtradas.append(t)

    # Retorna a lista de transações filtradas
    return transacoes_filtradas


for i in range(1, 4):
    if i == 1:
       transacoes = [ 100, -50, 300, -150]
       limite = 100
    elif i == 2:
       transacoes = [ 200, -50, 400 ]
       limite = 150
    else:
        transacoes = [ 1000, -75, 800 ]
        limite = 500

# entrada = input()

# entrada_transacoes, limite = entrada.split("],")
# entrada_transacoes = entrada_transacoes.strip("[]").replace(" ", "") 
# limite = float(limite.strip())  # Converte o limite para float


# transacoes = [int(valor) for valor in entrada_transacoes.split(",")]

# TODO: Filtre as transações que ultrapassam o limite:
    resultado = filtrar_transacoes(transacoes, limite)

    print()
    print(f"Transações entrada {i}: {resultado}")