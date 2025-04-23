from layouts.layouts_telas import titulos_telas, layout_cadastro_clientes, opcoes_disponiveis
from utils import user_functions
from utils.user_functions import posicionarCursor, exibir_conteudo, exibir_mensagem, limpar_linha, limpar_tela, esperar_tecla

campos_clientes = {
    "tipo_pessoa" : { "lin" : 7, "fisica" : 23, "juridica": 35, "size" : 1 },
    "cpf_cnpj" : { "lin" : 7, "col": 80, "size" : 18 },
    "nome_razaosocial" : { "lin": 9, "col" : 23, "size": 75 },
    "endereco" : { "lin" : 11, "col": 23, "size": 55 },
    "numero" : { "lin" : 11, "col": 89, "size" : 10 },
    "complemento" : { "lin": 13, "col": 23, "size": 75 },
    "bairro" : { "lin" : 15, "col" : 23, "size" : 75 },
    "cidade" : { "lin": 17, "col" : 23, "size": 66 },
    "estado" : { "lin": 17, "col" : 96, "size" : 2 },
    "cep" : { "lin" : 19, "col" : 23, "size": 10 },
    "telefone" : { "lin" : 19, "col": 85, "size": 13 },
    "status" : { "lin" : 21, "inativo" : 23, "ativo" : 35, "restrito" : 45, "bloqueado": 58, "size" : 1 },
    "data_cadastro" : { "lin" : 21, "col": 88, "size": 10 }
}

def limpar_campos_tela(flag_visualizacao: bool=False):
    for campo, valor in campos_clientes.items():
        if campo == "tipo_pessoa":
            limpar_linha(valor["lin"], valor["fisica"], valor["size"], not flag_visualizacao)
            limpar_linha(valor["lin"], valor["juridica"], valor["size"], not flag_visualizacao)
        elif campo == "status":
            limpar_linha(valor["lin"], valor["inativo"], valor["size"], not flag_visualizacao)
            limpar_linha(valor["lin"], valor["ativo"], valor["size"], not flag_visualizacao)
            limpar_linha(valor["lin"], valor["restrito"], valor["size"], not flag_visualizacao)
            limpar_linha(valor["lin"], valor["bloqueado"], valor["size"], not flag_visualizacao)
        else:
            limpar_linha(valor["lin"], valor["col"], valor["size"], not flag_visualizacao)

def iniciar():
    limpar_tela()
    exibir_conteudo(titulos_telas["cadastro_clientes"], 4, 2)
    user_functions.desenhar_tela(layout_cadastro_clientes)
    exibir_conteudo(opcoes_disponiveis["cadastros"])
    limpar_campos_tela()
    return esperar_tecla().upper()
    
    