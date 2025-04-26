from utils import user_functions
from utils.user_functions import limpar_linha, limpar_tela, exibir_conteudo, exibir_mensagem, esperar_tecla, exibir_titulo
from layouts.layouts_telas import layout_consulta_extratos, titulos_telas , opcoes_disponiveis

campos_filtros = {
    "num_conta" : { "lin" : 6, "col" : 14, "size" : 10 },
    "nome_cliente" : {"lin" : 6, "col" : 26, "size" : 40 },
    "data_inicial" : { "lin" : 6, "col" : 73, "size" : 10 },
    "data_final" : { "lin" : 6, "col" : 88, "size" : 10 }
}

def iniciar():
    limpar_tela()
    user_functions.desenhar_tela(layout_consulta_extratos, 10, 28)
    exibir_titulo(titulos_telas["consulta_extratos"])
    exibir_conteudo(opcoes_disponiveis["consulta_extratos"])

    while True:
        opcao = esperar_tecla().upper()
        if opcao == "R":
            break
        elif opcao == "P":
            user_functions.desenhar_tela(layout_consulta_extratos, 10, 28)
    
