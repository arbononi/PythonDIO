from layouts.layouts_telas import layout_contas, titulos_telas, opcoes_disponiveis
from utils import user_functions
from utils.user_functions import posicionarCursor, exibir_conteudo, exibir_mensagem, limpar_linha, limpar_tela, esperar_tecla

campos_conta = {
    "num_conta" : { "lin" : 7, "col" : 14, "size" : 10 },
    "data_abertura" : { "lin": 7, "col" : 88, "size" : 10 },
    "tipo_conta" : { "lin" : 9, "poupanca" : 14, "conta_corrente" : 27, "aplicacao" : 46, "size" : 1 },
    "cpf_cnpj" : { "lin" : 11, "col" : 14, "size" : 18 },
    "nome_cliente": { "lin" : 11, "col" : 34, "size" : 64 },
    "limite_especial" : { "lin": 13, "col" : 14, "size" : 14 },
    "status" : { "lin" : 13, "pendente": 61, "ativa": 75, "suspensa" : 87, "size" : 1 },
    "status1" : { "lin": 15, "bloqueada" : 61, "inativa" : 75, "encerrada": 87, "size" : 1 },
    "data_encerramento" : { "lin" : 17, "col" : 88, "size": 10 }
}

def limpar_campos_tela(flag_visualizacao: bool=False):
    for campo, valor in campos_conta.items():
        if campo == "tipo_conta":
            limpar_linha(valor["lin"], valor["poupanca"], valor["size"], not flag_visualizacao)
            limpar_linha(valor["lin"], valor["conta_corrente"], valor["size"], not flag_visualizacao)
            limpar_linha(valor["lin"], valor["aplicacao"], valor["size"], not flag_visualizacao)
        elif campo == "status":
            limpar_linha(valor["lin"], valor["pendente"], valor["size"], not flag_visualizacao)
            limpar_linha(valor["lin"], valor["ativa"], valor["size"], not flag_visualizacao)
            limpar_linha(valor["lin"], valor["suspensa"], valor["size"], not flag_visualizacao)
        elif campo == "status1":
            limpar_linha(valor["lin"], valor["bloqueada"], valor["size"], not flag_visualizacao)
            limpar_linha(valor["lin"], valor["inativa"], valor["size"], not flag_visualizacao)
            limpar_linha(valor["lin"], valor["encerrada"], valor["size"], not flag_visualizacao)
        else:
            limpar_linha(valor["lin"], valor["col"], valor["size"], not flag_visualizacao)

def iniciar():
    limpar_tela()
    exibir_conteudo(titulos_telas["cadastro_contas"], 4, 2)
    user_functions.desenhar_tela(layout_contas)
    exibir_conteudo(opcoes_disponiveis["cadastros"])
    limpar_campos_tela()
    return esperar_tecla().upper()