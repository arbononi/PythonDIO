from datetime import datetime, date
from database import bancodados
from utils import user_functions
from utils.user_functions import posicionarCursor, exibir_conteudo, exibir_mensagem, limpar_linha, limpar_tela, esperar_tecla, exibir_indicador
from layouts.layouts_telas import titulos_telas, layout_cadastro_clientes, opcoes_disponiveis
from models.clientes import Cliente
from models.tiposenum import TipoPessoa, StatusCliente

campos_clientes = {
    "tipo_pessoa" : { "lin" : 7, "fisica" : 23, "juridica": 35, "size" : 1, "mensagem" : "Tecle F o J para escolher o tipo de pessoa" },
    "cpf_cnpj" : { "lin" : 7, "col": 80, "size" : 18, "mensagem" : "Informe o {tipo_documento} ou SAIR para encerrar" },
    "nome_razaosocial" : { "lin": 9, "col" : 23, "size": 75, "mensagem" : "Informe o Nome/Razão Social ou SAIR para encerrar" },
    "endereco" : { "lin" : 11, "col": 23, "size": 55, "mensagem" : "Informe o Endereço ou SAIR para encerrar" },
    "numero" : { "lin" : 11, "col": 89, "size" : 10, "mensagem" : "Informe o Número do Endereço ou SAIR para encerrar" },
    "complemento" : { "lin": 13, "col": 23, "size": 75, "mensagem" : "Informe o Complemento do endereço ou SAIR para encerrar" },
    "bairro" : { "lin" : 15, "col" : 23, "size" : 75, "mensagem" : "Informe o Bairro ou SAIR para encerrar" },
    "cidade" : { "lin": 17, "col" : 23, "size": 66, "mensagem" : "Informe a Cidade ou SAIR para encerrar" },
    "estado" : { "lin": 17, "col" : 96, "size" : 2, "mensagem" : "Informe o Estado" },
    "cep" : { "lin" : 19, "col" : 23, "size": 10, "mensagem" : "Informe o CEP do Endereço ou SAIR para encerrar" },
    "telefone" : { "lin" : 19, "col": 85, "size": 13, "mensagem" : "Informe o número do Telefone com DDD ou SAIR para encerrar" },
    "status" : { "lin" : 21, "inativo" : 23, "ativo" : 44, "restrito" : 63, "bloqueado": 85, "size" : 1 , "mensagem" : "Selecione o status do cliente digitando a letra em destaque"},
    "data_cadastro" : { "lin" : 23, "col": 23, "size": 10 }
}

tipo_documento = ""
tipo_pessoa = None

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

def preparar_campo(lin, col, mensagem):
    limpar_linha()
    exibir_indicador(lin, col)
    exibir_conteudo(" " + mensagem)
    posicionarCursor(lin, col)

def setar_status(info: dict, status: StatusCliente):
    exibir_conteudo("•", info["lin"], info[status.name.lower])
    if status == StatusCliente.INATIVO:
       exibir_conteudo(" ", info["lin"], info["ativo"])
       exibir_conteudo(" ", info["lin"], info["restrito"])
       exibir_conteudo(" ", info["lin"], info["bloqueado"])
       return
    elif status == StatusCliente.ATIVO:
       exibir_conteudo(" ", info["lin"], info["inativo"])
       exibir_conteudo(" ", info["lin"], info["restrito"])
       exibir_conteudo(" ", info["lin"], info["bloqueado"])
       return
    elif status == StatusCliente.RESTRITO:
       exibir_conteudo(" ", info["lin"], info["inativo"])
       exibir_conteudo(" ", info["lin"], info["ativo"])
       exibir_conteudo(" ", info["lin"], info["bloqueado"])
       return
    else:
       exibir_conteudo(" ", info["lin"], info["inativo"])
       exibir_conteudo(" ", info["lin"], info["ativo"])
       exibir_conteudo(" ", info["lin"], info["restrito"])
    

def get_tipo_pessoa():
    global tipo_documento
    global tipo_pessoa
    info = campos_clientes["tipo_pessoa"]
    titulo = "fisica"
    tipo_documento = "CPF"

    while True:
        preparar_campo(info["lin"], info[titulo], info["mensagem"])
        escolha = esperar_tecla().upper()
        if escolha != "F" and escolha != "J":
            exibir_mensagem("Pressione apenas F ou J para escolher o tipo de pessao!")
            if titulo.upper() == "FISICA":
                exibir_indicador(info["lin"], info[titulo], False)
                titulo = "juridica"
            else:
                exibir_indicador(info["lin"], info[titulo], False)
                titulo = "fisica"
            continue
        elif escolha == 'F':
            tipo_pessoa = TipoPessoa.FISICA
            titulo = "fisica"
            tipo_documento = "CPF"
        else:
            tipo_pessoa = TipoPessoa.JURIDICA
            titulo = "juridica"
            tipo_documento = "CNPJ"
        exibir_conteudo("•", info["lin"], info[titulo])
        break

    exibir_indicador(info["lin"], info['fisica'], False)
    exibir_indicador(info["lin"], info['juridica'], False)

    return tipo_pessoa
        
def get_cpf_cnpj():
    global tipo_documento
    info = campos_clientes["cpf_cnpj"]
    fl_sair = False
    while True:
        preparar_campo(info["lin"], info["col"], info["mensagem"].format(tipo_documento=tipo_documento))
        cpf_cnpj = input()
        if cpf_cnpj.upper() == "SAIR":
            fl_sair = True
            break
        fl_ok, mensagem = user_functions.validar_documento(cpf_cnpj, tipo_pessoa)
        if not fl_ok:
            exibir_mensagem(mensagem)
            continue
        break
    exibir_indicador(info["lin"], info["col"], False)
    fl_ok, cpf_cnpj_formatado = user_functions.formatar_documento(cpf_cnpj, tipo_pessoa)
    if not fl_ok:
        exibir_conteudo(cpf_cnpj, info["lin"], info["col"])
    else:
        exibir_conteudo(cpf_cnpj_formatado.rjust(18, " "), info["lin"], info["col"])
    return fl_sair, cpf_cnpj

def get_nome_razao_social():
    info = campos_clientes["nome_razaosocial"]
    fl_sair = False
    while True:
        preparar_campo(info["lin"], info["col"], info["mensagem"])
        nome_razao_social = input().title()
        if nome_razao_social.upper() == "SAIR":
            fl_sair = True
            break
        fl_ok, mensagem = Cliente.validar_nome_razao_social(nome_razao_social)
        if not fl_ok:
            exibir_mensagem(mensagem)
            esperar_tecla()
            continue
        break
    exibir_indicador(info["lin"], info["col"], False)
    exibir_conteudo(nome_razao_social, info["lin"], info["col"])
    return fl_sair, nome_razao_social

def get_endereco():
    info = campos_clientes["endereco"]
    fl_sair = False
    preparar_campo(info["lin"], info["col"], info["mensagem"])
    endereco = input().title()
    if endereco.upper() == "SAIR":
        fl_sair = True
    exibir_indicador(info["lin"], info["col"], False)
    exibir_conteudo(endereco, info["lin"], info["col"])
    return fl_sair, endereco

def get_numero():
    info = campos_clientes["numero"]
    fl_sair = False
    preparar_campo(info["lin"], info["col"], info["mensagem"])
    numero = input().title()
    if numero.upper() == "SAIR":
        fl_sair = True
    exibir_indicador(info["lin"], info["col"], False)
    exibir_conteudo(numero, info["lin"], info["col"])
    return fl_sair, numero

def get_complemento():
    info = campos_clientes["complemento"]
    fl_sair = False
    preparar_campo(info["lin"], info["col"], info["mensagem"])
    complemento = input().title()
    if complemento.upper() == "SAIR":
        fl_sair = True
    exibir_indicador(info["lin"], info["col"], False)
    exibir_conteudo(complemento, info["lin"], info["col"])
    return fl_sair, complemento

def get_bairro():
    info = campos_clientes["bairro"]
    fl_sair = False
    preparar_campo(info["lin"], info["col"], info["mensagem"])
    bairro = input().title()
    if bairro.upper() == "SAIR":
        fl_sair = True
    exibir_indicador(info["lin"], info["col"], False)
    exibir_conteudo(bairro, info["lin"], info["col"])
    return fl_sair, bairro

def get_cidade():
    info = campos_clientes["cidade"]
    fl_sair = False
    preparar_campo(info["lin"], info["col"], info["mensagem"])
    cidade = input().title()
    if cidade.upper() == "SAIR":
        fl_sair = True
    exibir_indicador(info["lin"], info["col"], False)
    exibir_conteudo(cidade, info["lin"], info["col"])
    return fl_sair, cidade

def get_estado():
    info = campos_clientes["estado"]
    while True:
        preparar_campo(info["lin"], info["col"], info["mensagem"])
        estado = input().upper()
        fl_ok, uf, mensagem = user_functions.validar_estado(estado)
        if not fl_ok:
            exibir_mensagem(mensagem)
            continue
        break
    exibir_indicador(info["lin"], info["col"], False)
    exibir_conteudo(estado, info["lin"], info["col"])
    return estado

def get_cep():
    info = campos_clientes["cep"]
    fl_sair = False
    while True:
        preparar_campo(info["lin"], info["col"], info["mensagem"])
        str_cep = input().replace(".","").replace("-","")
        if str_cep.upper() == "SAIR":
            fl_sair = True
            break
        fl_ok, cep, mensagem = user_functions.validar_cep(str_cep)
        if not fl_ok:
            exibir_mensagem(mensagem)
            continue
        break
    exibir_indicador(info["lin"], info["col"], False)
    fl_ok, cep_formatado = user_functions.formatar_cep(cep)
    if not fl_ok:
        exibir_mensagem(cep_formatado)
    else:
        exibir_conteudo(cep_formatado, info["lin"], info["col"])
    return fl_sair, cep

def get_telefone():
    info = campos_clientes["telefone"]
    fl_sair = False
    preparar_campo(info["lin"], info["col"], info["mensagem"])
    telefone = input()
    if telefone.upper() == "SAIR":
        fl_sair = True
    return fl_sair, telefone

def get_status():
    info = campos_clientes["status"]
    titulo = "inativo"
    status = None
    while True:
        preparar_campo(info["lin"], info[titulo], info["mensagem"])
        escolha = esperar_tecla().upper()
        if escolha not in ["I", "A", "R", "B"]:
            exibir_mensagem("Opção inválida! Escolha uma das letras em destaque!")
        elif escolha == "I":
            status = StatusCliente.INATIVO
            break
        elif escolha == "A":
            status = StatusCliente.ATIVO
            break
        elif escolha == "R":
            status = StatusCliente.RESTRITO
        else:
            status = StatusCliente.BLOQUEADO
            break
        if status != None:
            setar_status(info, status)
        else:
            exibir_mensagem("Escolha um status para o cliente pressionando uma das letras em destaque!")
    
    return status

def processar_digitacao():
    tipo_pessoa = get_tipo_pessoa()
    fl_sair, cpf_cnpj = get_cpf_cnpj()
    if fl_sair:
        return
    fl_sair, nome_razao_social = get_nome_razao_social()
    if fl_sair:
        return
    fl_sair, endereco = get_endereco()
    if fl_sair:
        return
    fl_sair, numero = get_numero()
    if fl_sair:
        return
    fl_sair, complemento = get_complemento()
    if fl_sair:
        return
    fl_sair, bairro = get_bairro()
    if fl_sair:
        return
    fl_sair, cidade = get_cidade()
    if fl_sair:
        return
    estado = get_estado()
    fl_sair, cep = get_cep()
    if fl_sair:
        return
    fl_sair, telefone = get_telefone()
    if fl_sair:
        return
    status = get_status()
    info = campos_clientes["data_cadastro"]
    data_cadastro = date.today()
    data_atual_str = user_functions.formatar_data(data_cadastro)
    exibir_conteudo(data_atual_str, info["lin"], info["col"])

    cliente = Cliente(tipo_pessoa, cpf_cnpj, nome_razao_social, endereco, numero, complemento, 
                      bairro, cidade, estado, cep, telefone, status, data_cadastro)
    
    result = bancodados.add_update_cliente(cliente)
    if result is None:
        exibir_mensagem("Erro ao salvar Cliente!")
    
def iniciar():
    limpar_tela()
    exibir_conteudo(titulos_telas["cadastro_clientes"], 4, 2)
    user_functions.desenhar_tela(layout_cadastro_clientes)
    exibir_conteudo(opcoes_disponiveis["cadastros"])
    limpar_campos_tela()
    return esperar_tecla().upper()
    
def incluir():
    limpar_campos_tela(True)
    processar_digitacao()
