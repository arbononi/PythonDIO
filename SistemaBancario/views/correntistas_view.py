import msvcrt
from enum import Enum
from datetime import date
from views.telas_sistema import titulos_telas, layout_correntistas
from utils import user_functions
from utils.user_functions import posicionarCursor
from models.tiposenum import TipoOperacao as operacao, Estados, StatusCorrentista
from models.tiposenum import MOSTRAR_CURSOR, OCULTAR_CURSOR, PRETO_NO_BRANCO
from models.correntista import Correntista
from database.tables import lista_correntistas

campos_correntista = {
    "num_cpf": { "lin": 7, "col" : 13, "size" : 14 },
    "data_cadastro" : { "lin": 7, "col" : 88, "size" : 10 },
    "nome" : { "lin": 8, "col" : 13, "size" : 49 },
    "data_nasc" : { "lin": 8, "col" : 76, "size" : 10 },
    "idade" : { "lin" : 8, "col" : 95, "size" : 3 },
    "endereco" : { "lin" : 9, "col" : 13, "size" : 63 },
    "numero" : { "lin": 9, "col" : 88, "size" : 10 },
    "complemento" : { "lin": 10, "col" : 13, "size" : 27 },
    "bairro" : { "lin" : 10, "col" : 51, "size" : 47 },
    "cidade" : { "lin" : 11, "col" : 13, "size" : 58 },
    "uf" : { "lin": 11, "col" : 78, "size" : 2 },
    "cep" : { "lin": 11, "col": 88, "size" : 10 },
    "telefone" : { "lin": 12, "col": 13, "size" : 13 },
    "status" : { "size" : 1,
                 "ativo"    : {"lin": 12, "col": 61, },
                 "restrito" : {"lin": 12, "col": 73 },
                 "inativo"  : {"lin": 12, "col" : 88 } }
}

linha_mensagem = 30
status_cad = operacao.CONSULTA
status_permitidos = [ "", "X"]

def preencher_tela(correntista: Correntista):
    correntista.exibir_dados_em_tela(campos_correntista)

def limpar_tela():
    for campo, valor in campos_correntista.items():
        if campo == "status":
            for status_tipo, status_info in valor.items():
                if status_tipo == "size":
                    size = status_info
                else:
                    user_functions.limpar_linha(status_info["lin"], status_info["col"], size, True)
                    user_functions.limpar_linha(status_info["lin"], status_info["col"], size, True)
                    user_functions.limpar_linha(status_info["lin"], status_info["col"], size, True)
        else:
            user_functions.limpar_linha(valor["lin"], valor["col"], valor["size"], PRETO_NO_BRANCO)

def mensagem_padrao():
    user_functions.limpar_linha()
    user_functions.exibirMensagem(linha_mensagem, 3, "A qualquer momento digite FIM para sair")

def digitar_cpf():
    info = campos_correntista["num_cpf"]
    while True:
        try:
            user_functions.limpar_linha()
            user_functions.exibirMensagem(linha_mensagem, 3, "Digite o Número do CPF ou 999999999999 pra sair")
            posicionarCursor(info["lin"], info["col"])
            num_cpf = int(input())
            break
        except ValueError:
            user_functions.exibirMensagem(linha_mensagem, 3, "Número do CPF inválido. Digite apenas os números")
            user_functions.esperar_tecla()
            user_functions.limpar_linha()
    user_functions.limpar_linha()
    return num_cpf

def digitar_nome():
    fl_sair = False
    while True:
        mensagem_padrao()
        info = campos_correntista["nome"]
        posicionarCursor(info["lin"], info["col"])
        nome = input()
        if nome.upper() == "FIM":
            fl_sair = True
        fl_ok, mensagem = Correntista.validar_nome(nome)
        if not fl_ok:
            user_functions.limpar_linha()
            user_functions.exibirMensagem(linha_mensagem, 3, mensagem)
            user_functions.esperar_tecla()
            continue
        break
    nome = nome.replace("_","").title()
    user_functions.limpar_linha(info["lin"], info["col"], info["size"])
    posicionarCursor(info["lin"], info["col"])
    print(nome)
    return fl_sair, nome

def digitar_data_nasc():
    fl_sair = False
    while True:
        user_functions.limpar_linha()
        info = campos_correntista["data_nasc"]
        posicionarCursor(info["lin"], info["col"])
        str_data = input()
        if str_data.upper() == "FIM":
            fl_sair = True
            break
        fl_ok, data_nasc, mensagem = user_functions.validar_data(str_data)
        if not fl_ok:
            user_functions.limpar_linha()
            user_functions.exibirMensagem(linha_mensagem, 3, mensagem)
            user_functions.esperar_tecla()
            user_functions.limpar_linha()
            continue
        posicionarCursor(info["lin"], info["col"])
        print(user_functions.formatar_data(data_nasc))
        posicionarCursor(campos_correntista["idade"]["lin"], campos_correntista["idade"]["col"])
        print(str(Correntista.get_idade(data_nasc)).rjust(3, " "))
        break

    return fl_sair, data_nasc

def digitar_endereco():
    fl_sair = False
    info = campos_correntista["endereco"]
    mensagem_padrao()
    posicionarCursor(info["lin"], info["col"])
    endereco = input()
    if endereco.upper() == "FIM":
        fl_sair = True
    user_functions.limpar_linha(info["lin"], info["col"], info["size"])
    posicionarCursor(info["lin"], info["col"])
    print(endereco.title())
    return fl_sair, endereco.title()

def digitar_numero():
    fl_sair = False
    info = campos_correntista["numero"]
    mensagem_padrao()
    posicionarCursor(info["lin"], info["col"])
    numero = input()
    if numero.upper() == "FIM":
        fl_sair = True
    user_functions.limpar_linha(info["lin"], info["col"], info["size"])
    posicionarCursor(info["lin"], info["col"])
    print(numero)
    return fl_sair, numero

def digitar_complemento():
    fl_sair = False
    info = campos_correntista["complemento"]
    mensagem_padrao()
    posicionarCursor(info["lin"], info["col"])
    complemento = input()
    if complemento.upper() == "FIM":
        fl_sair = True
    user_functions.limpar_linha(info["lin"], info["col"], info["size"])
    posicionarCursor(info["lin"], info["col"])
    print(complemento.title())
    return fl_sair, complemento.title()

def digitar_bairro():
    fl_sair = False
    info = campos_correntista["bairro"]
    mensagem_padrao()
    posicionarCursor(info["lin"], info["col"])
    bairro = input()
    if bairro.upper() == "FIM":
        fl_sair = True
    user_functions.limpar_linha(info["lin"], info["col"], info["size"])
    posicionarCursor(info["lin"], info["col"])
    print(bairro.title())
    return fl_sair, bairro.title()

def digitar_cidade():
    fl_sair = False
    info = campos_correntista["cidade"]
    mensagem_padrao()
    posicionarCursor(info["lin"], info["col"])
    cidade = input()
    if cidade.upper() == "FIM":
        fl_sair = True
    user_functions.limpar_linha(info["lin"], info["col"], info["size"])
    posicionarCursor(info["lin"], info["col"])
    print(cidade.title())
    return fl_sair, cidade.title()

def digitar_uf():
    fl_sair = False
    while True:
        user_functions.limpar_linha()
        info = campos_correntista["uf"]
        posicionarCursor(info["lin"], info["col"])
        uf = input().upper()
        if uf == "":
            fl_sair = True
            break
        fl_ok, uf, mensagem = user_functions.validar_estado(uf)
        if not fl_ok:
            user_functions.exibirMensagem(linha_mensagem, 3, "UF inválida!")
            user_functions.esperar_tecla()
            user_functions.limpar_linha()
            continue
    return fl_sair, uf

def digitar_cep():
    fl_sair = False
    info = campos_correntista["cep"]
    while True:
        mensagem_padrao()
        posicionarCursor(info["lin"], info["col"])
        cep = input()
        if cep.upper() == "FIM":
            fl_sair = True
            break
        fl_ok, cep, mensagem = user_functions.validar.cep(cep)
        if not fl_ok:
            user_functions.limpar_linha()
            user_functions.exibirMensagem(linha_mensagem, 3, mensagem)
            user_functions.esperar_tecla()
            continue
    if fl_ok:
        str_cep = user_functions.formatar_cep(cep)
        posicionarCursor(info["lin"], info["col"])
        print(str_cep)

    return fl_sair, cep

def digitar_telefone():
    fl_sair = False
    info = campos_correntista["telefone"]
    mensagem_padrao()
    posicionarCursor(info["lin"], info["col"])
    telefone = input()
    if telefone.upper() == "FIM":
        fl_sair = True
    user_functions.limpar_linha(info["lin"], info["col"], info["size"])
    posicionarCursor(info["lin"], info["col"])
    print(telefone)
    return fl_sair, telefone

def digitar_status():
    fl_sair = False
    info = campos_correntista["status"]
    ativo = info["ativo"]
    restrito = info["restrito"]
    inativo = info["inativo"]
    user_functions.limpar_linha()

    while True:
        posicionarCursor(ativo["lin"], ativo["col"])
        status = input().upper()
        if status not in status_permitidos:
            user_functions.exibirMensagem("Informe X para marcar o status ou deixe em branco!")
            user_functions.esperar_tecla()
            user_functions.limpar_linha()
            continue
        if status == "X":
            status = StatusCorrentista.ATIVO
            break
    
    if isinstance(status, Enum):
        return fl_sair, status

    while True:
        posicionarCursor(restrito["lin"], restrito["col"])
        status = input().upper()
        if status not in status_permitidos:
            user_functions.exibirMensagem("Informe X para marcar o status ou deixe em branco!")
            user_functions.esperar_tecla()
            user_functions.limpar_linha()
            continue
        if status == "X":
            status = StatusCorrentista.RESTRITO
            break

    if isinstance(status, Enum):
        return fl_sair, status
    
    while True:
        posicionarCursor(inativo["lin"], restrito["col"])
        status = input().upper()
        if status not in status_permitidos:
            user_functions.exibirMensagem("Informe X para marcar o status ou deixe em branco!")
            user_functions.esperar_tecla()
            user_functions.limpar_linha()
            continue
        if status == "X":
            status = StatusCorrentista.INATIVO
            break
    return fl_sair, status
    
def processar_digitacao(num_cpf: int):
    cpf_formatado = user_functions.formatar_cpf(num_cpf)
    posicionarCursor(campos_correntista["num_cpf"]["lin"], campos_correntista["num_cpf"]["col"])
    print(cpf_formatado)
    posicionarCursor(campos_correntista["data_cadastro"]["lin"], campos_correntista["data_cadastro"]["col"])
    print(user_functions.formatar_data(date.today()))
    fl_sair, nome = digitar_nome()
    if fl_sair:
        return
    fl_sair, data_nasc = digitar_data_nasc()
    if fl_sair:
        return
    fl_sair, endereco = digitar_endereco()
    if fl_sair:
        return
    fl_sair, numero = digitar_numero()
    if fl_sair:
        return
    fl_sair, complemento = digitar_complemento()
    if fl_sair:
        return
    fl_sair, bairro = digitar_bairro()
    if fl_sair:
        return
    fl_sair, cidade = digitar_cidade()
    if fl_sair:
        return
    fl_sair, uf = Estados(digitar_uf())
    if fl_sair:
        return
    fl_sair, cep = int(digitar_cep)
    if fl_sair:
        return
    fl_sair, telefone = digitar_telefone()
    if fl_sair:
        return
    fl_sair, status = StatusCorrentista(digitar_status)
    if fl_sair:
        return

    lista_correntistas[str(num_cpf)] = Correntista(num_cpf, nome, endereco, numero, complemento, bairro,
                                                   cidade, uf.name, cep, data_nasc, telefone, status, date.today())
    
def iniciar():
    user_functions.limpar_tela()
    user_functions.posicionarCursor(4, 2)
    print(titulos_telas["cadastro_correntista"])
    user_functions.desenhar_tela(layout_correntistas)
    limpar_tela()
    posicionarCursor(linha_mensagem, 2)
    print(OCULTAR_CURSOR)
    opcao = msvcrt.getch().decode("utf-8").upper()
    print(MOSTRAR_CURSOR)
    return opcao

def novo_cadastro():
    status_cad = operacao.INCLUSAO
    while True:
        num_cpf = digitar_cpf()
        if num_cpf == 99999999999:
            break
        correntista = lista_correntistas.get(str(num_cpf))
        if correntista:
            user_functions.exibirMensagem(linha_mensagem, 3, "CPF já cadastrado!")
            user_functions.esperar_tecla()
            user_functions.limpar_linha()
            continue
        processar_digitacao(num_cpf)
        break

def alterar_cadastro():
    status_cad = operacao.ALTERACAO
    while True:
        num_cpf = digitar_cpf()
        if num_cpf == 99999999999:
            break
        correntista = lista_correntistas.get(str(num_cpf))
        if not correntista:
            user_functions.exibirMensagem(linha_mensagem, 3, "CPF não cadastrado!")
            user_functions.esperar_tecla()
            user_functions.limpar_linha()
            continue
        Correntista.exibir_dados_em_tela(campos_correntista)
        user_functions.esperar_tecla()