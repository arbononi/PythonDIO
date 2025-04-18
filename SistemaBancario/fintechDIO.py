import locale
import csv
import msvcrt
from os import system as limp
from pathlib import Path
from time import sleep
from datetime import datetime, date
from models import tiposenum
from utils import user_functions
from database import tables
from views.telas_sistema import layout_tela_principal, titulos_telas

menu_principal_opcoes = "[1 - CORRENTISTAS]     [2 - CONTAS]     [3 - TRANSAÇÕES]     [4 - EXTRATOS]     [9 - SAIR]".center(98, " ")

locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.1252')
limp("cls")
linha_mensagem = 30
data_atual_str = user_functions.formatar_data(date.today(), True) 
opcao = 0
opcao_limite = 4
user_functions.desenhar_tela(layout_tela_principal)
user_functions.posicionarCursor(2, 2)
print(titulos_telas["menu_principal"].center(75, " "))
user_functions.posicionarCursor(2, 85)
print(data_atual_str)

while opcao != 9:
    try:
        user_functions.posicionarCursor(linha_mensagem, 2)
        print(menu_principal_opcoes)
        user_functions.posicionarCursor(linha_mensagem, 1)
        opcao = int(user_functions.esperar_tecla())

        if (opcao < 1 or opcao > opcao_limite) and opcao != 9:
            user_functions.limpar_linha(linha_mensagem, 2, 98)
            user_functions.exibirMensagem(linha_mensagem, 3, f"Opção inválida. Escolha entre 1 e {opcao_limite} ou 9 pra sair!")
            user_functions.esperar_tecla()
            user_functions.limpar_linha(linha_mensagem, 2, 98)
            continue

        if opcao == 9:
            break;

    except ValueError:
            user_functions.limpar_linha(linha_mensagem, 2, 98)
            user_functions.exibirMensagem(linha_mensagem, 3, f"Opção inválida. Escolha entre 1 e {opcao_limite} ou 9 pra sair!")
            user_functions.esperar_tecla()
            user_functions.limpar_linha(linha_mensagem, 2, 98)

user_functions.limpar_linha(linha_mensagem, 2, 98)
user_functions.exibirMensagem(linha_mensagem, 3, "Obrigador por usar nossa banco! Volte sempre!!!")
sleep(1)
limp("cls")
