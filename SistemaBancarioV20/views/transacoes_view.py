from utils import user_functions
from utils.user_functions import limpar_linha, limpar_tela, exibir_conteudo, exibir_mensagem, esperar_tecla
from layouts.layouts_telas import layout_menu_transacoes, titulos_telas

def iniciar():
    limpar_tela()
    user_functions.desenhar_tela(layout_menu_transacoes)
    try:
        limpar_linha()
        exibir_conteudo(" Escolha a opção desejada entre as disponíveis: ")
        opcao = int(esperar_tecla())
        return opcao
    except ValueError:
        limpar_linha()
        exibir_mensagem("Opção inválida! Tente novamente!")
