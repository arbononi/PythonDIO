from os import system as limp
from time import sleep
from datetime import date
from Database import banco_dados
from Utils import user_functions
from Views.Telas_Sistema import layout_tela_principal, titulos_telas
from Controllers.Correntistas_Controller import ConrrentistasController
from Controllers.ContaCorrente_Controller import ContaCorrentesController

menu_principal_opcoes = "[1 - CORRENTISTAS]  [2 - CONTAS]  [3 - TRANSAÇÕES]  [4 - EXTRATOS]  [5 - IMPORTAR]  [9 - SAIR]".center(98, " ")

opcoes_disponiveis = [
    "[1 - CORRENTISTAS]",
    "[2 - CONTAS]",
    "[3 - TRANSAÇÕES]",
    "[4 - EXTRATOS]",
    "[5 - IMPORTAR],"
    "[9 - SAIR]"
]

limp("cls")
linha_mensagem = 30
data_atual_str = user_functions.formatar_data(date.today(), True) 
opcao = 0
opcao_limite = 5

def limpar_tela():
    for linha in layout_tela_principal:
         if (linha["lin"] < 4):
              continue
         if linha["lin"] > 28:
              break
         else:
              user_functions.posicionarCursor(linha["lin"], linha["col"])
              print(linha["value"])
    user_functions.posicionarCursor(2, 2)

user_functions.desenhar_tela(layout_tela_principal)
user_functions.posicionarCursor(2, 2)
print(titulos_telas["menu_principal"])
user_functions.posicionarCursor(2, 85)
print(data_atual_str)
user_functions.configurar_locale()

while opcao != 9:
    try:
        user_functions.posicionarCursor(linha_mensagem, 2)
        print(menu_principal_opcoes)
        user_functions.posicionarCursor(linha_mensagem, 1)
        opcao = int(user_functions.esperar_tecla())

        if (opcao < 1 or opcao > opcao_limite) and opcao != 9:
            user_functions.limpar_linha()
            user_functions.exibirMensagem(linha_mensagem, 3, f"Opção inválida. Escolha entre 1 e {opcao_limite} ou 9 pra sair!")
            user_functions.esperar_tecla()
            user_functions.limpar_linha()
            continue

        if opcao == 9:
            break
    
        if opcao == 1:
            app = ConrrentistasController()
            app.iniciar()
        elif opcao == 2:
            app = ContaCorrentesController()
            app.iniciar()
        elif opcao == 5:
             banco_dados.carregar_correntistas()
             banco_dados.carregar_contas()
        else:
            user_functions.limpar_linha()
            user_functions.exibir_valor(30, 3, f"A opção {opcoes_disponiveis[opcao - 1]} ainda não está disponível")
            user_functions.esperar_tecla()
        limpar_tela()
    except ValueError:
            user_functions.limpar_linha()
            user_functions.exibirMensagem(linha_mensagem, 3, f"Opção inválida. Escolha entre 1 e {opcao_limite} ou 9 pra sair!")
            user_functions.esperar_tecla()
            user_functions.limpar_linha()

user_functions.limpar_linha()
user_functions.exibirMensagem(linha_mensagem, 3, "Obrigador por usar nossa banco! Volte sempre!!!")
sleep(1)
limp("cls")
