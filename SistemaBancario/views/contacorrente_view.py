from datetime import date
from database import banco_dados
from views.telas_sistema import titulos_telas, layout_contacorrente, layout_rel_contas, layout_tela_principal
from utils import user_functions
from utils.user_functions import posicionarCursor, limpar_linha, exibir_valor, exibirMensagem, esperar_tecla
from models.tiposenum import TipoContaCorrente, StatusContaCorrente, TipoOperacao
from models.contacorrente import ContaCorrente


campos_contacorrente = {
    "num_conta" : { "lin":  7, "col": 14, "size": 10 },
    "data_abertura" : { "lin":  7, "col": 88, "size": 10 },
    "num_cpf": { "lin":  9, "col": 14, "size": 14 },
    "nome_cliente": { "lin":  9, "col": 30, "size": 40 },
    "data_cadastro": { "lin": 9, "col": 88, "size": 10 },
    "tipo_conta" : { "col" : 6, "size" : 1, "poupanca": 14, "conta_corrente": 15 },
    "limite_especial" : { "lin": 18, "col" : 10, "size" : 12 },
    "status" : { "col" : 29, "size" : 1, "pendente" : 14, "ativa": 15, "bloqueada": 16, "inativa" : 17, "encerrada" : 18 },
    "data_encerramento" : { "lin" : 18, "col": 43, "size": 10 }
}

linha_mensagem = 30
coluna_mensagem = 3
conta_atual = None

def limpar_campos_tela(flag_visualizar: bool= False):
    for campo, valor in campos_contacorrente.items():
        if campo == "tipo_conta":
            limpar_linha(valor["poupanca"], valor["col"], valor["size"], not flag_visualizar)
            limpar_linha(valor["conta_corrente"], valor["col"], valor["size"], not flag_visualizar)
        elif campo == "status":
            limpar_linha(valor["pendente"], valor["col"], valor["size"], not flag_visualizar)
            limpar_linha(valor["ativa"], valor["col"], valor["size"], not flag_visualizar)
            limpar_linha(valor["bloqueada"], valor["col"], valor["size"], not flag_visualizar)
            limpar_linha(valor["inativa"], valor["col"], valor["size"], not flag_visualizar)
            limpar_linha(valor["encerrada"], valor["col"], valor["size"], not flag_visualizar)
        else:
            limpar_linha(valor["lin"], valor["col"], valor["size"], not flag_visualizar)

def preencher_tela(conta_corrente: ContaCorrente):
    ContaCorrente.exibir_dados_conta(conta_corrente, campos_contacorrente)

def mensagem_padrao(mensagem: str, exibir: bool=False):
    limpar_linha()
    if exibir:
        exibirMensagem(linha_mensagem, coluna_mensagem, f"{mensagem}. Digite FIM para encerrar.")
    else:
        exibirMensagem(linha_mensagem, coluna_mensagem, mensagem)

def digitar_num_conta():
    info = campos_contacorrente["num_conta"]
    while True:
        try:
            limpar_linha()
            mensagem_padrao("Digite o número da conta. 0 para sair")
            posicionarCursor(info["lin"], info["col"])
            num_conta = int(input())
            break
        except ValueError as error:
            exibirMensagem(linha_mensagem, coluna_mensagem, error)
            esperar_tecla()
    limpar_linha()
    return num_conta

def digitar_cpf():
    info = campos_contacorrente["num_cpf"]
    while True:
        try:
            limpar_linha()
            mensagem_padrao("Digite o CPF do cliente. 99999999999 (11 números 9) para sair")
            posicionarCursor(info["lin"], info["col"])
            str_num_cpf = input()
            if str_num_cpf == "99999999999":
                return 99999999999
            if str_num_cpf == "" and conta_atual:
                num_cpf = conta_atual.num_cpf
            else:
                num_cpf = int(str_num_cpf)
            correntista = banco_dados.Lista_Correntistas.get(num_cpf)
            if not correntista:
                exibirMensagem(linha_mensagem, coluna_mensagem, "CPF não cadastrado!")
                esperar_tecla()
                continue
            nome_cliente = campos_contacorrente["nome_cliente"]
            data_cadastro = campos_contacorrente["data_cadastro"]
            posicionarCursor(nome_cliente["lin"], nome_cliente["col"])
            print(correntista.nome.ljust(40, " ")[:40])
            posicionarCursor(data_cadastro["lin"], data_cadastro["col"])
            print(user_functions.formatar_data(correntista.data_cadastro))
            break
        except ValueError as error:
            exibirMensagem(linha_mensagem, coluna_mensagem, error)
            esperar_tecla()
    limpar_linha()
    return num_cpf

def digitar_tipo_conta():
    info = campos_contacorrente["tipo_conta"]
    tipo_conta = None
    
    while not tipo_conta:
        limpar_linha()
        exibirMensagem(linha_mensagem, coluna_mensagem, "Escolha o tipo da conta: [P]oupança [C]onta Corrente")
        escolha = esperar_tecla(False).upper()
        if escolha == "P":
            exibir_valor(info["poupanca"], info["col"], "•")
            exibir_valor(info["conta_corrente"], info["col"], " ")
            tipo_conta = TipoContaCorrente.POUPANCA
        elif escolha == "C":
            exibir_valor(info["poupanca"], info["col"], " ")
            exibir_valor(info["conta_corrente"], info["col"], "•")
            tipo_conta = TipoContaCorrente.CONTA_CORRENTE
        else:
            exibirMensagem(linha_mensagem, coluna_mensagem, "Escolha um tipo conta: P para Poupança ou C pra Conta Corrente!")
            esperar_tecla()
            continue
    return tipo_conta

def digitar_limite_especial():
    info = campos_contacorrente["limite_especial"]
    while True:
        try:
            limpar_linha()
            mensagem_padrao("Informe o valor do limite. 0 para continuar")
            posicionarCursor(info["lin"], info["col"])
            str_valor_limite = input().replace(",", "_").replace(".", ",").replace("_", ".")
            if str_valor_limite == "" and conta_atual:
                valor_limite = conta_atual.limite_especial
            else:
                valor_limite = float(str_valor_limite)
            break
        except ValueError as error:
            exibirMensagem(linha_mensagem, coluna_mensagem, error)
            esperar_tecla()
    if valor_limite == 0 and conta_atual:
        valor_limite = conta_atual.limite_especial
    valor_formatado = user_functions.formatar_valor(valor_limite)
    posicionarCursor(info["lin"], info["col"])
    print(valor_formatado.rjust(12, " "))
    return valor_limite

def digitar_status():
    info = campos_contacorrente["status"]
    info_data_encerramento = campos_contacorrente["data_encerramento"]
    status = None
    while not status:
        limpar_linha()
        exibirMensagem(linha_mensagem, coluna_mensagem, "Escolha o status: [P]endente [A]tiva [B]loqueada [I]nativa [E]ncerrada: ")
        marcado = esperar_tecla(False).upper()
        if marcado == "P":
            status = StatusContaCorrente.PENDENTE
            exibir_valor(info["pendente"], info["col"], "•")
            exibir_valor(info["ativa"], info["col"], " ")
            exibir_valor(info["bloqueada"], info["col"], " ")
            exibir_valor(info["inativa"], info["col"], " ")
            exibir_valor(info["encerrada"], info["col"], " ")
            exibir_valor(info_data_encerramento["lin"], info_data_encerramento["col"], " " * 10)
            break
        elif marcado == "A":
            status = StatusContaCorrente.ATIVA
            exibir_valor(info["pendente"], info["col"], " ")
            exibir_valor(info["ativa"], info["col"], "•")
            exibir_valor(info["bloqueada"], info["col"], " ")
            exibir_valor(info["inativa"], info["col"], " ")
            exibir_valor(info["encerrada"], info["col"], " ")
            exibir_valor(info_data_encerramento["lin"], info_data_encerramento["col"], " " * 10)
            break
        elif marcado == "B":
            status = StatusContaCorrente.BLOQUEADA
            exibir_valor(info["pendente"], info["col"], " ")
            exibir_valor(info["ativa"], info["col"], " ")
            exibir_valor(info["bloqueada"], info["col"], "•")
            exibir_valor(info["inativa"], info["col"], " ")
            exibir_valor(info["encerrada"], info["col"], " ")
            exibir_valor(info_data_encerramento["lin"], info_data_encerramento["col"], " " * 10)
        elif marcado == "I":
            status = StatusContaCorrente.INATIVA
            exibir_valor(info["pendente"], info["col"], " ")
            exibir_valor(info["ativa"], info["col"], " ")
            exibir_valor(info["bloqueada"], info["col"], " ")
            exibir_valor(info["inativa"], info["col"], "•")
            exibir_valor(info["encerrada"], info["col"], " ")
            exibir_valor(info_data_encerramento["lin"], info_data_encerramento["col"], " " * 10)
        elif marcado == "E":
            status = StatusContaCorrente.ENCERRADA
            exibir_valor(info["pendente"], info["col"], " ")
            exibir_valor(info["ativa"], info["col"], " ")
            exibir_valor(info["bloqueada"], info["col"], " ")
            exibir_valor(info["inativa"], info["col"], " ")
            exibir_valor(info["encerrada"], info["col"], "•")
        else:
            exibirMensagem(linha_mensagem, 3, "Opção inválida! Tente novamente")
            esperar_tecla()
            continue
    return status

def digitar_data_encerramento():
    info = campos_contacorrente["data_encerramento"]
    while True:
        limpar_linha()
        exibirMensagem(linha_mensagem, coluna_mensagem, "Digite a data de encerramento!", True)
        str_data = input()
        if str_data.upper() == "FIM":
            fl_sair = True
            break
        elif str_data == "" and conta_atual:
            str_data = user_functions.formatar_data(conta_atual.data_encerramento)
        fl_ok, data_encerramento, mensagem = user_functions.validar_data(str_data)
        if not fl_ok:
            limpar_linha()
            exibirMensagem(linha_mensagem, coluna_mensagem, mensagem)
            esperar_tecla()
            limpar_linha()
            continue
        posicionarCursor(info["lin"], info["col"])
        print(user_functions.formatar_data(data_encerramento))
        break
    return fl_sair, data_encerramento

def processar_digitacao(num_conta: int, status_cad: TipoOperacao):
    global conta_atual
    num_cpf = digitar_cpf()
    if num_cpf == 99999999999:
        return
    tipo_conta = digitar_tipo_conta()
    if tipo_conta == TipoContaCorrente.CONTA_CORRENTE:
        valor_limite = digitar_limite_especial()
    else:
        valor_limite = 0
    status = digitar_status()
    if status == StatusContaCorrente.ENCERRADA:
        fl_sair, data_encerramento = digitar_data_encerramento()
        if fl_sair:
            return
    else:
        data_encerramento = date.min
        
    while True:
        exibirMensagem(linha_mensagem, coluna_mensagem, "Confirma os dados (S/N): ")
        confirmar = esperar_tecla().upper()
        if confirmar != "S" and confirmar != "N":
            exibirMensagem(linha_mensagem, coluna_mensagem, "Tecle apenas S ou N")
            continue
        break
    if confirmar == "S":
        if status_cad == TipoOperacao.INCLUSAO:
            data_abertura = date.today()
            operacao = "incluída"
        else:
            data_abertura = conta_atual.data_abertura
            operacao = "alterada"
        ContaCorrente.add_conta(ContaCorrente(num_conta, num_cpf, data_abertura, valor_limite, tipo_conta, status, data_encerramento))
        exibirMensagem(linha_mensagem, coluna_mensagem, f"Conta {operacao} com sucesso!")
        esperar_tecla()

def limpar_tela_relatorio():
    info = layout_rel_contas[3]
    for linha in range(6, 29):
        posicionarCursor(linha, info["col"])
        print(info["value"])

def iniciar():
    user_functions.limpar_tela()
    posicionarCursor(4, 2)
    print(titulos_telas["cadastro_contacorrente"])
    user_functions.desenhar_tela(layout_contacorrente)
    limpar_campos_tela()
    posicionarCursor(linha_mensagem, coluna_mensagem)
    return esperar_tecla().upper()

def novo_cadastro():
    limpar_campos_tela()
    num_conta = ContaCorrente.proximo_num_conta()
    info = campos_contacorrente["num_conta"]
    posicionarCursor(info["lin"], info["col"])
    print(str(num_conta).rjust(10, "0"))
    info = campos_contacorrente["data_abertura"]
    posicionarCursor(info["lin"], info["col"])
    print(user_functions.formatar_data(date.today()))
    processar_digitacao(num_conta, TipoOperacao.INCLUSAO)

def alterear_cadastro():
    global conta_atual
    while True:
        limpar_campos_tela(True)
        num_conta = digitar_num_conta()
        if num_conta == 0:
            break
        conta_atual = banco_dados.Lista_ContaCorrente.get(num_conta)
        if not conta_atual:
            exibirMensagem(linha_mensagem, coluna_mensagem, "Conta não cadastrada!")
            esperar_tecla()
            limpar_linha()
            continue
        preencher_tela(conta_atual)
        processar_digitacao(num_conta, TipoOperacao.ALTERACAO)

def visualizar_cadastro():
    while True:
        limpar_campos_tela(True)
        num_conta = digitar_num_conta()
        if num_conta == 0:
            break
        conta_atual = banco_dados.Lista_ContaCorrente.get(num_conta)
        if not conta_atual:
            exibirMensagem(linha_mensagem, coluna_mensagem, "Conta não cadastrada!")
            esperar_tecla()
            limpar_linha()
            continue
        ContaCorrente.exibir_dados_conta(conta_atual, campos_contacorrente)
        exibirMensagem(linha_mensagem, coluna_mensagem, "Pressione qualquer tecla...")
        esperar_tecla()

def visualizar_relatorio():
    user_functions.limpar_tela()
    user_functions.limpar_linha(2, 2, 75)
    posicionarCursor(2, 2)
    print(titulos_telas["relatorio_contacorrente"])
    user_functions.desenhar_tela(layout_rel_contas, 6, 28)
    if not banco_dados.Lista_ContaCorrente:
        exibirMensagem(30, 3, "Não há contas cadastradas!")
        esperar_tecla()
    else:
        linha = 6
        for num_conta, conta in banco_dados.Lista_ContaCorrente.items():
            cpf_formatado = user_functions.formatar_cpf(conta.num_cpf)
            correntista = banco_dados.Lista_Correntistas.get(conta.num_cpf)
            data_abertura = user_functions.formatar_data(conta.data_abertura)
            if not correntista:
                nome_cliente = "Não encontrado".ljust(36, " ")[:36]
            else:
                nome_cliente = correntista.nome.ljust(36, " ")[:36]
            posicionarCursor(linha, 3)
            print(str(num_conta).rjust(10, " "), conta.tipo_conta.name.ljust(14, " "), cpf_formatado,
                   nome_cliente, data_abertura, sep = " ║ ", end="")
            if linha == 28:
                posicionarCursor(linha_mensagem, 10)
                opcao = esperar_tecla().upper()
                if opcao == "R":
                    break
                else:
                    limpar_tela_relatorio()
            linha += 1
        limpar_linha()
        exibirMensagem(30, 3, "Fim da listagem. Pressione qualquer tecla para retornar...")
        esperar_tecla()
        user_functions.limpar_tela()
    posicionarCursor(2, 2)
    print(titulos_telas["menu_principal"])
    posicionarCursor(4, 2)
    print(titulos_telas["cadastro_contacorrente"])
    linha3 =  layout_tela_principal[2]
    linha29 = layout_tela_principal[28]
    user_functions.exibir_valor(linha3["lin"], linha3["col"], linha3["value"])
    user_functions.exibir_valor(linha29["lin"], linha29["col"], linha29["value"])
    user_functions.desenhar_tela(layout_contacorrente)
