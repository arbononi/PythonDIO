import locale
from os import system as limp
from time import sleep
from datetime import date
from layouts.layouts_telas import layout_padrao, layout_abertura, titulos_telas, opcoes_disponiveis
from utils import user_functions
from controllers.clientes_controller import ClienteController
from controllers.contas_controller import ContaController
from controllers.transacoes_controller import TransacaoController
from controllers.saldos_controller import SaldoController
from controllers.extratos_controller import ExtratoController

def exibir_abertura():
    user_functions.desenhar_tela(layout_abertura)
    user_functions.exibir_conteudo(titulos_telas["titulo_principal"], 2, 2)

locale.setlocale(locale.LC_ALL, 'pt_BR')
limp("cls")
data_atual_str = user_functions.formatar_data(date.today(), True)
opcao = 0
opcao_limite = 5
user_functions.posicionarCursor(1, 1)
print(layout_padrao, end="")
user_functions.exibir_conteudo(data_atual_str, 2, 85)
exibir_abertura()

while opcao != 9:
    try:
        user_functions.exibir_conteudo(opcoes_disponiveis["menu_principal"])
        opcao = int(user_functions.esperar_tecla())
        if opcao == 9:
            break
        if (opcao < 1 or opcao > opcao_limite) and opcao != 9:
            user_functions.exibir_mensagem(f"Opção inválida. Escolha uma opção entre 1 e {opcao_limite}.")
            user_functions.limpar_linha()
            continue
        elif opcao == 1:
            app = ClienteController()
            app.iniciar()
        elif opcao == 2:
            app = ContaController()
            app.iniciar()
        elif opcao == 3:
            app = TransacaoController()
            app.iniciar()
        elif opcao == 4:
            app = ExtratoController()
            app.iniciar()
        elif opcao == 5:
            app = SaldoController()
            app.iniciar()
        exibir_abertura()
    except ValueError:
        user_functions.exibir_mensagem("Opção inválida! Digite apenas números!")
user_functions.limpar_linha()
user_functions.exibir_conteudo(" Obrigado por usar nosso banco! Volte Sempre!!!")
sleep(1)
limp("cls")
