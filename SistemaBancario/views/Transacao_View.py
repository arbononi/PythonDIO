from datetime import datetime
from Database import banco_dados
from Views.Telas_Sistema import layout_transacoes, layout_rel_transacoes, layout_tela_principal
from Utils import user_functions
from Utils.user_functions import posicionarCursor, limpar_linha, exibirMensagem, esperar_tecla
from Models.TiposEnum import TipoTransacao
from Models.Transacao import Transacao

campos_transacao = {
    "id" : { "lin":  7, "col": 19, "size": 10 },
    "data_movto" : { "lin":  8, "col": 61, "size": 15 },
    "idconta" : { "lin":  9, "col": 19, "size": 10 },
    "nome_correntista" : { "lin": 10, "col": 5, "size": 41 },
    "saldo_anterior" : { "lin": 12, "col": 19, "size": 14 },
    "tipo_transacao" : { "lin": 12, "size" : 1, "deposito": 55, "saque": 70 },
    "saldo_atual" : { "lin": 14, "col": 19, "size": 14 },
    "valor_movto" : { "lin": 14, "col": 63, "size": 14}
}

lin_padrao = 30
col_padrao = 3

def preencher_tela_transacao(transacao: Transacao):
    Transacao.exibir_dados(transacao, campos_transacao)

def limpar_campos_tela(flag_visualizar: bool = False):
    for campo, layout in campos_transacao.items():
        if campo == "tipo_transacao":
            posicionarCursor(layout["lin"], layout["deposito"], not flag_visualizar)
            print(" ")
            posicionarCursor(layout["lin"], layout["saque"], not flag_visualizar)
            print(" ")
        else:
            posicionarCursor(layout["lin"], layout["col"] not flag_visualizar)
            print(" " * layout["size"])

def mensagem_padrao(mensagem: str, exibir_mensagem_padrao: bool=True):
    limpar_linha()
    if exibir_mensagem_padrao:
        exibirMensagem(lin_padrao, col_padrao, f"{mensagem}. Digite FIM para encerrar.")
    else:
        exibirMensagem(lin_padrao, col_padrao, mensagem)

def limpar_tela_relatorio():
    info = layout_rel_transacoes[3]
    for linha in range(6, 29):
        posicionarCursor(linha, 1)
        print(info["value"])

