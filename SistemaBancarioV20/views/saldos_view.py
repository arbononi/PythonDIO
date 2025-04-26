from utils import user_functions
from utils.user_functions import limpar_linha, limpar_tela, exibir_conteudo, exibir_mensagem, esperar_tecla, exibir_titulo
from layouts.layouts_telas import layout_consulta_saldo, titulos_telas

campos_saldo = {
    "num_conta" : { "lin" : 7, "col" : 21, "size" : 10 },
    "cpf_cnpj" :  { "lin": 7, "col": 44, "size": 18 },
    "nome_cliente" : {"lin" : 7, "col" : 64, "size" : 34 },
    "saldo_atual" : { "lin" : 9, "col" : 21, "size" : 15 },
    "valor_limite" : { "lin" : 9, "col" : 50, "size" : 14 },
    "saldo_disponivel" : { "lin" : 9, "col" : 83, "size" : 15 },
}

def iniciar():
    limpar_tela()
    user_functions.desenhar_tela(layout_consulta_saldo)
    exibir_titulo(titulos_telas["consulta_saldo"])

    while True:
        try:
            limpar_linha()
            info = campos_saldo["num_conta"]
            exibir_conteudo(" Informe o número da conta ou 0 para sair")
            user_functions.posicionarCursor(info["lin"], info["col"])
            num_conta = int(input())
            if num_conta == 0:
                break
        except ValueError as error:
            exibir_mensagem(f"Número da conta inválido: {error}")
            esperar_tecla()

