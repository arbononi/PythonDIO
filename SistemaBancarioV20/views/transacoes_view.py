from utils import user_functions
from utils.user_functions import limpar_linha, limpar_tela, exibir_conteudo, exibir_mensagem, esperar_tecla, exibir_titulo
from layouts.layouts_telas import titulos_telas, layout_menu_transacoes, layout_deposito_saque 
from layouts.layouts_telas import layout_transferencia_doc, layout_pix, layout_pagamentos


campos_deposito_saque = {
    "num_conta" : { "lin": 7, "col": 14, "size": 10 },
    "valor_transacao" : { "lin": 7, "col": 38, "size": 14 },
    "autor" : { "lin": 7, "col" : 66, "size" : 98 },
    "tipo" : { "lin": 9, "col": 7, "size": 14 }
}

campos_transferencia_doc = {
    "conta_origem" : { "lin": 8, "col": 14, "size": 10 },
    "cpf_cnpj_origem" : { "lin": 8, "col": 37, "size": 18 },
    "nome_cliente_origem" : { "lin": 8, "col": 57, "size": 39 },
    "conta_destino" : { "lin": 12, "col": 14, "size": 10 },
    "cpf_cnpj_destino" : { "lin": 12, "col": 37, "size": 18 },
    "nome_cliente_destino" : { "lin": 12, "col": 57, "size": 39 },
    "valor_transacao" : { "lin": 16, "col": 14, "size": 14 },
    "observacoes" : { "lin": 14, "col": 36, "size": 60 },
    "valor_taxa" : { "lin": 20, "col": 14, "size": 14 }
}

campos_pix = {
    "conta_origem" : { "lin": 8, "col": 14, "size": 10 },
    "tipo_chave" : { "lin": 13, "cnpj": 14, "cpf": 29, "telefone": 43, "email": 62, "chave": 78 },
    "chave_pix" : { "lin": 14, "col": 6, "size": 90 },
    "valor_transacao": { "lin": 18, "col": 14, "size": 14 },
    "observacoes": { "lin": 18, "col": 36, "size": 60 }
}

campos_pagamento = {
    "conta_origem" : { "lin": 8, "col": 14, "size": 10 },
    "cpf_cnpj_origem" : { "lin": 8, "col": 37, "size": 18 },
    "nome_cliente_origem" : { "lin": 8, "col": 57, "size": 39 },
    "codigo_barras" : { "lin": 12, "col": 6, "size": 90 },
    "data_vencto" : { "lin": 14, "col": 18, "size": 10 },
    "valor_pagto" : { "lin": 14, "col": 46, "size": 14 },
    "data_pagto" : { "lin": 14, "col": 86, "size": 10 }
}

def digitar_conta(info: dict):
    fl_sair = False
    while True:
        try:
            limpar_linha()
            exibir_conteudo("Informe o número da conta ou 0 para sair", 30, 3)
            user_functions.posicionarCursor(info["lin"], info["col"])
            num_conta = int(input())
            if num_conta == 0:
                fl_sair = True
                break
        except ValueError as error:
            exibir_mensagem(f"Número da Conta inválido: {error}")
    return fl_sair, num_conta

def processar_deposito_saque():
    info = campos_deposito_saque["num_conta"]
    fl_sair, num_conta = digitar_conta(info)
    if fl_sair:
        return

def processar_transferencia_doc():
    info = campos_transferencia_doc["conta_origem"]
    fl_sair, conta_origem = digitar_conta(info)

def processar_pix():
    info = campos_pix["conta_origem"]
    fl_sair, num_conta = digitar_conta(info)
    if fl_sair:
        return

def processar_pagamentos():
    info = campos_pagamento["conta_origem"]
    fl_sair, num_conta = digitar_conta(info)
    if fl_sair:
        return
        
def iniciar():
    while True:
        try:
            limpar_tela()
            user_functions.desenhar_tela(layout_menu_transacoes)
            limpar_linha()
            exibir_conteudo(" Escolha a opção desejada entre as disponíveis: ")
            opcao = int(esperar_tecla())
            break
        except ValueError:
            limpar_linha()
            exibir_mensagem("Opção inválida! Tente novamente!")
    return opcao

def depositar():
    limpar_tela()
    user_functions.desenhar_tela(layout_deposito_saque)
    exibir_titulo(titulos_telas["transacao_deposito"])
    processar_deposito_saque()

def sacar():
    limpar_tela();
    user_functions.desenhar_tela(layout_deposito_saque)
    exibir_titulo(titulos_telas["transacao_saque"])
    processar_deposito_saque()
    
def transferir():
    limpar_tela()
    user_functions.desenhar_tela(layout_transferencia_doc, 0, 19)
    exibir_titulo(titulos_telas["transacao_transferencia"])
    processar_transferencia_doc()

def efetuar_pix():
    limpar_tela()
    user_functions.desenhar_tela(layout_pix)
    exibir_titulo(titulos_telas["transacao_pix"])
    processar_pix()

def enviar_doc():
    limpar_tela()
    user_functions.desenhar_tela(layout_transferencia_doc)
    exibir_titulo(titulos_telas["transacao_doc"])
    processar_transferencia_doc()

def efetuar_pagamentos():
    limpar_tela()
    user_functions.desenhar_tela(layout_pagamentos)
    exibir_titulo(titulos_telas["transacao_pagamentos"])
    processar_pagamentos()
