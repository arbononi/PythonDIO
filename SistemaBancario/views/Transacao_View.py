from datetime import datetime
from database import banco_dados
from views.telas_sistema import titulos_telas, layout_transacoes, layout_rel_transacoes, layout_tela_principal
from utils import user_functions
from utils.user_functions import posicionarCursor, limpar_linha, exibirMensagem, esperar_tecla, exibir_valor
from models.tiposenum import TipoTransacao, StatusContaCorrente
from models.transacao import Transacao
from models.saldocontas import SaldoConta

campos_transacao = {
    "id" : { "lin":  7, "col": 19, "size": 10 },
    "data_movto" : { "lin":  7, "col": 63, "size": 15 },
    "idconta" : { "lin":  9, "col": 19, "size": 10 },
    "nome_correntista" : { "lin": 10, "col": 5, "size": 41 },
    "saldo_anterior" : { "lin": 12, "col": 19, "size": 14 },
    "tipo_transacao" : { "lin": 12, "size" : 1, "deposito": 55, "saque": 70 },
    "saldo_atual" : { "lin": 14, "col": 19, "size": 14 },
    "valor_movto" : { "lin": 14, "col": 63, "size": 14}
}

lin_padrao = 30
col_padrao = 3
transacao_atual = None
numero_conta = None
tipo_transacao = None
saldo_conta = None

def limpar_campos_tela(flag_visualizar: bool = False):
    for campo, layout in campos_transacao.items():
        if campo == "tipo_transacao":
            limpar_linha(layout["lin"], layout["deposito"], layout["size"], not flag_visualizar)
            limpar_linha(layout["lin"], layout["saque"], layout["size"], not flag_visualizar)
        else:
            limpar_linha(layout["lin"], layout["col"], layout["size"], not flag_visualizar)

def preencher_tela_transacao(transacao: Transacao):
    Transacao.exibir_dados(transacao, campos_transacao)

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

def digitar_id():
    info = campos_transacao["id"]
    while True:
        try:
            limpar_linha()
            mensagem_padrao("Digite o número da transação ou 0 para sair", False)
            posicionarCursor(info["lin"], info["col"])
            id = int(input())
            break
        except ValueError:
            limpar_linha()
            exibirMensagem(lin_padrao, col_padrao, "Número da transação inválido!")
            esperar_tecla()
    limpar_linha()
    return id

def digitar_numero_conta():
    info = campos_transacao["idconta"]
    global transacao_atual
    global numero_conta
    global saldo_conta

    while True:
        try:
            limpar_linha()
            mensagem_padrao("Informe o número da conta")
            posicionarCursor(info["lin"], info["col"])
            str_idconta = input()
            if str_idconta.upper() == "FIM":
                return True, None
            numero_conta = int(str_idconta)
            conta_corrente = banco_dados.Lista_ContaCorrente.get(numero_conta)
            if not conta_corrente:
                limpar_linha()
                exibirMensagem(lin_padrao, col_padrao, "Conta não cadastrada!")
                esperar_tecla()
                continue
            elif conta_corrente.status != StatusContaCorrente.ATIVA:
                limpar_linha()
                exibirMensagem(lin_padrao, col_padrao, f"Está conta está {conta_corrente.status.name.title()}. Não pode ser movimentada!")
                esperar_tecla()
                continue
            fl_ok, mensagem = Transacao.check_numero_transacoes_dia(numero_conta, datetime.now());
            if not fl_ok:
                limpar_linha()
                exibirMensagem(lin_padrao, col_padrao, mensagem)
                esperar_tecla()
                continue
            info_correntista = campos_transacao["nome_correntista"]
            info_saldo_atual = campos_transacao["saldo_anterior"]
            correntista = banco_dados.Lista_Correntistas.get(conta_corrente.num_cpf)
            saldo_conta = banco_dados.Lista_SaldoContas.get(conta_corrente.num_conta)
            posicionarCursor(info_correntista["lin"], info_correntista["col"])
            if correntista is None:
                print(f"Correntista não encontrado: CPF: {user_functions.formatar_cpf(conta_corrente.num_cpf)}")
            else:
                print(correntista.nome.ljust(41, " ")[:41])
            if transacao_atual is None:
                posicionarCursor(info_saldo_atual["lin"], info_saldo_atual["col"])
                if saldo_conta is None:
                    print(user_functions.formatar_valor(float(0)).rjust(14, " "))
                else:
                    print(user_functions.formatar_valor(saldo_conta.saldo_atual).rjust(14, " "))
            break
        except ValueError:
            limpar_linha()
            exibirMensagem(lin_padrao, col_padrao, "Código da conta inválido!")
            esperar_tecla()
    return False

def digitar_tipo_transacao():
    global transacao_atual
    global tipo_transacao
    info = campos_transacao["tipo_transacao"]
    while True:
        limpar_linha()
        exibirMensagem(lin_padrao, col_padrao, "Escolha a transação que deseja realizar: [D]epósito [S]aque")
        opcao = esperar_tecla().upper()
        if opcao == "D":
            posicionarCursor(info["lin"], info["deposito"])
            print("•")
            tipo_transacao = TipoTransacao.DEPOSITO
            break
        elif opcao == "S":
            posicionarCursor(info["lin"], info["saque"])
            print("•")
            tipo_transacao = TipoTransacao.SAQUE
            break
        else:
            limpar_linha()
            exibirMensagem("Opção inválida. Tente de novo!")
            esperar_tecla()
            continue
        
def digitar_valor():
    global transacao_atual
    global tipo_transacao
    global numero_conta
    global saldo_conta
    saldo_atual = 0.0

    info = campos_transacao["valor_movto"]
    while True:
        try:
            limpar_linha()
            mensagem_padrao(f"Informe o valor do {tipo_transacao.name.title()}.")
            posicionarCursor(info["lin"], info["col"])
            str_valor = input().replace(",", "_").replace(".", ",").replace("_", ".")
            if str_valor.upper() == "FIM":
                return True, None
            valor_movto = float(str_valor)
            fl_ok, mensagem = Transacao.validar_valor_transacao(numero_conta, valor_movto, tipo_transacao)
            if not fl_ok:
                limpar_linha()
                exibirMensagem(lin_padrao, col_padrao, mensagem)
                esperar_tecla()
                continue
            posicionarCursor(info["lin"], info["col"])
            print(user_functions.formatar_valor(valor_movto).rjust(14, " "))
            break
        except ValueError:
            exibirMensagem(lin_padrao, col_padrao, "Valor do Movimento inválido!")
            esperar_tecla()

    if transacao_atual is None:
        if saldo_conta is None:
            saldo_atual = saldo_atual + valor_movto if tipo_transacao == TipoTransacao.DEPOSITO else saldo_atual - valor_movto
        else:
            saldo_atual = saldo_conta.saldo_atual + valor_movto if tipo_transacao == TipoTransacao.DEPOSITO else saldo_conta.saldo_atual - valor_movto
        info_saldo_atual = campos_transacao['saldo_atual']
        posicionarCursor(info_saldo_atual["lin"], info_saldo_atual["col"])
        print(user_functions.formatar_valor(saldo_atual).rjust(14, " "))

    return False, valor_movto

def processar_digitacao(idtransacao: int):
    global transacao_atual
    global numero_conta
    global tipo_transacao
    if not transacao_atual:
        info_id = campos_transacao["id"]
        posicionarCursor(info_id["lin"], info_id["col"])
        print(user_functions.formatar_valor(idtransacao).rjust(10, " "))
        info_data_movto = campos_transacao["data_movto"]
        posicionarCursor(info_data_movto["lin"], info_data_movto["col"])
        print(user_functions.formatar_data_hora(datetime.now()))
        data_movto = datetime.now()
    fl_sair = digitar_numero_conta()
    if fl_sair:
        return
    digitar_tipo_transacao()
    fl_sair, valor_movto = digitar_valor()
    if fl_sair:
        return
    while True:
        limpar_linha()
        exibirMensagem(lin_padrao, col_padrao, "Confirma os dados (S/N)? ")
        confirmar = esperar_tecla().upper()
        if confirmar not in ["S", "N"]:
            limpar_linha()
            exibirMensagem(lin_padrao, col_padrao, "Digite apenas S ou N...")
            esperar_tecla()
            continue
        break
    if confirmar == "N":
        return
    saldo_anterior = 0.0
    saldo_atual = 0.0
    if saldo_conta is None:
        saldo_atual = saldo_atual + valor_movto if tipo_transacao == TipoTransacao.DEPOSITO else saldo_atual - valor_movto
    else:
        saldo_anterior = saldo_conta.saldo_atual
        saldo_atual = saldo_conta.saldo_atual - valor_movto if tipo_transacao == TipoTransacao.SAQUE else saldo_conta.saldo_atual + valor_movto
    transacao = Transacao(idtransacao, data_movto, numero_conta, tipo_transacao, saldo_anterior, valor_movto, saldo_atual, False)
    if not Transacao.add_transacao(transacao):
        limpar_linha()
        exibirMensagem(lin_padrao, col_padrao, "Problemas ao confirmar transação!")
        esperar_tecla()
        return
    SaldoConta.atualizar_saldo(numero_conta, valor_movto, tipo_transacao)

def iniciar():
    user_functions.limpar_tela()
    posicionarCursor(4, 2)
    print(titulos_telas["lancamento_transacao"])
    user_functions.desenhar_tela(layout_transacoes)
    limpar_campos_tela()
    posicionarCursor(lin_padrao, col_padrao)
    opcao = esperar_tecla().upper()
    return opcao

def nova_transacao():
    limpar_campos_tela()
    idtransacao = Transacao.get_proximo_id()
    processar_digitacao(idtransacao)
    limpar_campos_tela()
    
def visualizar_relatorio():
    user_functions.limpar_tela()
    limpar_linha(2, 2, 75)
    posicionarCursor(2, 2)
    print(titulos_telas["relatorio_transacao"])
    user_functions.desenhar_tela(layout_rel_transacoes, 6, 28)
    if not banco_dados.Lista_Transacoes:
        exibirMensagem(lin_padrao, col_padrao, "Nenhuma transação para ser exibida!")
        esperar_tecla()
    else:
        linha = 5
        posicionarCursor(lin_padrao, 33)
        for id, transacao in sorted(banco_dados.Lista_Transacoes.items(), key=lambda t: t[1].data_movto):
            linha += 1
            data_hora = user_functions.formatar_data_hora(transacao.data_movto)
            saldo_anterior = user_functions.formatar_valor(transacao.saldo_anterior).rjust(15, " ")
            valor_movto = user_functions.formatar_valor(transacao.valor_transacao).rjust(14, " ")
            saldo_final = user_functions.formatar_valor(transacao.saldo_atual).rjust(15, " ")
            posicionarCursor(linha, 3)
            print(data_hora, str(transacao.idconta).rjust(10, " "), " "  + transacao.tipo_transacao.name.title().ljust(9, " "),
                  saldo_anterior, valor_movto, saldo_final, sep = " ║ ", end="")
            if linha == 28:
                posicionarCursor(lin_padrao, 10)
                opcao = esperar_tecla()
                if opcao == "R":
                    break
                else:
                    limpar_tela_relatorio()
        limpar_linha()
        exibirMensagem(lin_padrao, col_padrao, "Fim da listagem. Pressione qualquer tecla para retornar ")
        esperar_tecla()
    user_functions.limpar_tela()
    posicionarCursor(2, 2)
    print(titulos_telas["menu_principal"])
    posicionarCursor(4, 2)
    print(titulos_telas["lancamento_transacao"])
    linha3 = layout_tela_principal[2]
    linha29 = layout_tela_principal[28]
    user_functions.exibir_valor(linha3["lin"], linha3["col"], linha3["value"])
    user_functions.exibir_valor(linha29["lin"], linha29["col"], linha29["value"])
    user_functions.desenhar_tela(layout_transacoes)