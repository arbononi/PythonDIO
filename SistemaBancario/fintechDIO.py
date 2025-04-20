import locale
import csv
import msvcrt
from os import system as limp
from pathlib import Path
from time import sleep
from datetime import datetime, date
from models import tiposenum
from models.correntista import Correntista
from utils import user_functions
from database import tables
from views.telas_sistema import layout_tela_principal, titulos_telas
from controllers.correntistas_controller import ConrrentistasController
from controllers.contacorrentes_controller import ContaCorrentesController

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
pasta_projeto = Path().resolve()
caminho_arquivo_correntistas = pasta_projeto / "lista_correntistas.csv"
#caminho_arquivo_historicos = pasta_projeto / "Lista_Historicos.csv"

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

def carregar_correntistas_arquivo(leitura_inicial: bool=False):
    if not caminho_arquivo_correntistas.exists():
        user_functions.posicionarCursor(30, 2, f"Arquivo {caminho_arquivo_correntistas} não encontrado!")
        user_functions.esperar_tecla()
        return
    with open(caminho_arquivo_correntistas, newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=";")
        for linha in leitor:
            fl_cpf_ok, mensagem = user_functions.validar_cpf(int(linha["num_cpf"]))
            fl_cep_ok, cep, mensagem = user_functions.validar_cep(linha["cep"])
            fl_data_nasc_ok, data_nasc, mensagem = user_functions.validar_data(linha["data_nasc"])
            if not fl_cpf_ok:
                continue
            if not fl_cep_ok:
               cep = 0
            if not fl_data_nasc_ok:
                data_nasc = date.min.date()
            status = Correntista.get_status_by_name(linha["status"])
            correntista = Correntista(int(linha["num_cpf"]), linha["nome"].title(), linha["endereco"].title(), linha["numero"].title(), 
                                      linha["complemento"].title(), linha["bairro"].title(), linha["cidade"].title(), linha["uf"].upper(),
                                      cep, data_nasc, linha["telefone"], status, date.today())
            Correntista.salvar_correntista(correntista)
    if not leitura_inicial:
        user_functions.exibirMensagem(linha_mensagem, 3, "Correntistas importados com sucesso!")
        user_functions.esperar_tecla()


user_functions.desenhar_tela(layout_tela_principal)
user_functions.posicionarCursor(2, 2)
print(titulos_telas["menu_principal"])
user_functions.posicionarCursor(2, 85)
print(data_atual_str)
user_functions.configurar_locale()

if (caminho_arquivo_correntistas.exists()):
    carregar_correntistas_arquivo(True)

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
             carregar_correntistas_arquivo()
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
