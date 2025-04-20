import msvcrt
from enum import Enum
from datetime import date
from views.telas_sistema import titulos_telas, layout_correntistas, layout_rel_correntistas, layout_tela_principal
from utils import user_functions
from utils.user_functions import posicionarCursor
from models.tiposenum import StatusCorrentista
from models.tiposenum import MOSTRAR_CURSOR, OCULTAR_CURSOR
from models.correntista import Correntista
from database.tables import lista_correntistas

campos_correntista = {
    "num_cpf": { "lin": 7, "col" : 13, "size" : 14 },
    "data_cadastro" : { "lin": 7, "col" : 88, "size" : 10 },
    "nome" : { "lin": 9, "col" : 13, "size" : 49 },
    "data_nasc" : { "lin": 9, "col" : 76, "size" : 10 },
    "idade" : { "lin" : 9, "col" : 95, "size" : 3 },
    "endereco" : { "lin" : 11, "col" : 13, "size" : 63 },
    "numero" : { "lin": 11, "col" : 88, "size" : 10 },
    "complemento" : { "lin": 13, "col" : 13, "size" : 27 },
    "bairro" : { "lin" : 13, "col" : 51, "size" : 47 },
    "cidade" : { "lin" : 15, "col" : 13, "size" : 58 },
    "uf" : { "lin": 15, "col" : 78, "size" : 2 },
    "cep" : { "lin": 15, "col": 88, "size" : 10 },
    "telefone" : { "lin": 17, "col": 13, "size" : 13 },
    "status" : { "size" : 1,
                 "lin" : 17,
                 "ativo"    : { "col": 61, },
                 "restrito" : { "col": 73 },
                 "inativo"  : { "col" : 88 } }
                #  "ativo"    : {"lin": 17, "col": 61, },
                #  "restrito" : {"lin": 17, "col": 73 },
                #  "inativo"  : {"lin": 17, "col" : 88 } }
}

linha_mensagem = 30
status_permitidos = [ "", "X"]
correntista_atual = None

def preencher_tela(correntista: Correntista):
    correntista.exibir_dados_em_tela(campos_correntista)

def limpar_campos_tela(flag_visualizar: bool=False):
    for campo, valor in campos_correntista.items():
        if campo == "status":
            for status_tipo, status_info in valor.items():
                if status_tipo == "size":
                    size = status_info
                elif status_tipo == "lin":
                    lin = status_info
                else:
                    user_functions.limpar_linha(lin, status_info["col"], size, not flag_visualizar)
                    user_functions.limpar_linha(lin, status_info["col"], size, not flag_visualizar)
                    user_functions.limpar_linha(lin, status_info["col"], size, not flag_visualizar)
        else:
            user_functions.limpar_linha(valor["lin"], valor["col"], valor["size"], not flag_visualizar)

def mensagem_padrao(informacao: str="", exibir_mensagem_padrao: bool=True):
    user_functions.limpar_linha()
    if exibir_mensagem_padrao:
        user_functions.exibirMensagem(linha_mensagem, 3, f"{informacao}. A qualquer momento digite FIM para sair")
    else:
        user_functions.exibirMensagem(linha_mensagem, 3, informacao)

def limpar_tela_relatorio():
    info = layout_rel_correntistas[3]
    for linha in range(6, 29):
        posicionarCursor(linha, 1)
        print(info)

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
    global correntista_atual
    fl_sair = False
    while True:
        mensagem_padrao("Digite o nome")
        info = campos_correntista["nome"]
        posicionarCursor(info["lin"], info["col"])
        nome = input()
        if nome.upper() == "FIM":
            fl_sair = True
        elif nome.upper() == "" and correntista_atual:
            nome = correntista_atual.nome
        fl_ok, mensagem = Correntista.validar_nome(nome)
        if not fl_ok:
            user_functions.limpar_linha()
            user_functions.exibirMensagem(linha_mensagem, 3, mensagem)
            user_functions.esperar_tecla()
            continue
        nome = nome.title()
        user_functions.limpar_linha(info["lin"], info["col"], info["size"])
        posicionarCursor(info["lin"], info["col"])
        print(nome)
        break
    return fl_sair, nome

def digitar_data_nasc():
    fl_sair = False
    global correntista_atual
    while True:
        mensagem_padrao("Digite a data de nascimento")
        info = campos_correntista["data_nasc"]
        posicionarCursor(info["lin"], info["col"])
        str_data = input()
        if str_data.upper() == "FIM":
            fl_sair = True
            break
        elif str_data == "" and correntista_atual:
            str_data = user_functions.formatar_data(correntista_atual.data_nasc)
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
    global correntista_atual
    info = campos_correntista["endereco"]
    mensagem_padrao("Digite o Endereço")
    posicionarCursor(info["lin"], info["col"])
    endereco = input()
    if endereco.upper() == "FIM":
        fl_sair = True
    elif endereco == "" and correntista_atual:
        endereco = correntista_atual.endereco
    user_functions.limpar_linha(info["lin"], info["col"], info["size"])
    posicionarCursor(info["lin"], info["col"])
    print(endereco.title())
    return fl_sair, endereco.title()

def digitar_numero():
    fl_sair = False
    global correntista_atual
    info = campos_correntista["numero"]
    mensagem_padrao("Digite o número do endereço")
    posicionarCursor(info["lin"], info["col"])
    numero = input()
    if numero.upper() == "FIM":
        fl_sair = True
    elif numero == "" and correntista_atual:
        numero = correntista_atual.numero
    user_functions.limpar_linha(info["lin"], info["col"], info["size"])
    posicionarCursor(info["lin"], info["col"])
    print(numero)
    return fl_sair, numero

def digitar_complemento():
    fl_sair = False
    global correntista_atual
    info = campos_correntista["complemento"]
    mensagem_padrao("Digite o complemento")
    posicionarCursor(info["lin"], info["col"])
    complemento = input()
    if complemento.upper() == "FIM":
        fl_sair = True
    elif complemento == "" and correntista_atual:
        complemento = correntista_atual.complemento
    user_functions.limpar_linha(info["lin"], info["col"], info["size"])
    posicionarCursor(info["lin"], info["col"])
    print(complemento.title())
    return fl_sair, complemento.title()

def digitar_bairro():
    fl_sair = False
    global correntista_atual
    info = campos_correntista["bairro"]
    mensagem_padrao("Digite o bairro")
    posicionarCursor(info["lin"], info["col"])
    bairro = input()
    if bairro.upper() == "FIM":
        fl_sair = True
    elif bairro == "" and correntista_atual:
        bairro = correntista_atual.bairro
    user_functions.limpar_linha(info["lin"], info["col"], info["size"])
    posicionarCursor(info["lin"], info["col"])
    print(bairro.title())
    return fl_sair, bairro.title()

def digitar_cidade():
    fl_sair = False
    global correntista_atual
    info = campos_correntista["cidade"]
    mensagem_padrao("Digite a cidade")
    posicionarCursor(info["lin"], info["col"])
    cidade = input()
    if cidade.upper() == "FIM":
        fl_sair = True
    elif cidade == "" and correntista_atual:
        cidade = correntista_atual.cidade
    user_functions.limpar_linha(info["lin"], info["col"], info["size"])
    posicionarCursor(info["lin"], info["col"])
    print(cidade.title())
    return fl_sair, cidade.title()

def digitar_uf():
    fl_sair = False
    global correntista_atual
    while True:
        mensagem_padrao("Digite o Estado")
        info = campos_correntista["uf"]
        posicionarCursor(info["lin"], info["col"])
        uf = input().upper()
        if uf == "" and not correntista_atual:
            fl_sair = True
            break
        elif uf == "" and correntista_atual:
            uf = correntista_atual.uf
        fl_ok, uf, mensagem = user_functions.validar_estado(uf)
        if not fl_ok:
            user_functions.exibirMensagem(linha_mensagem, 3, mensagem)
            user_functions.esperar_tecla()
            user_functions.limpar_linha()
            continue
        posicionarCursor(info["lin"], info["col"])
        print(uf)
        break
    return fl_sair, uf

def digitar_cep():
    fl_sair = False
    global correntista_atual
    info = campos_correntista["cep"]
    while True:
        mensagem_padrao("Informe o CEP")
        posicionarCursor(info["lin"], info["col"])
        str_cep = input()
        if str_cep.upper() == "FIM":
            fl_sair = True
            break
        elif str_cep == "" and correntista_atual:
            str_cep = str(correntista_atual.cep)
        fl_ok, cep, mensagem = user_functions.validar_cep(str_cep)
        if not fl_ok:
            user_functions.limpar_linha()
            user_functions.exibirMensagem(linha_mensagem, 3, mensagem)
            user_functions.esperar_tecla()
            continue
        str_cep = user_functions.formatar_cep(cep)
        posicionarCursor(info["lin"], info["col"])
        print(str_cep)
        break

    return fl_sair, cep

def digitar_telefone():
    fl_sair = False
    global correntista_atual
    info = campos_correntista["telefone"]
    mensagem_padrao("Digite o número do telefone com DDD")
    posicionarCursor(info["lin"], info["col"])
    telefone = input()
    if telefone.upper() == "FIM":
        fl_sair = True
    elif telefone == "" and correntista_atual:
        telefone = correntista_atual.telefone
    user_functions.limpar_linha(info["lin"], info["col"], info["size"])
    posicionarCursor(info["lin"], info["col"])
    print(telefone)
    return fl_sair, telefone

def digitar_status():
    fl_sair = False
    global correntista_atual
    info = campos_correntista["status"]
    ativo = info["ativo"]
    restrito = info["restrito"]
    inativo = info["inativo"]
    user_functions.limpar_linha()
    flag_status = ""
    status = None
    lin = info["lin"]
    col = ativo["col"]
    while not status:
        mensagem_padrao("Marque X no status correspondente", False)
        posicionarCursor(lin, col)
        flag_status = input().upper()
        if flag_status == "X":
            if col == ativo["col"]:
                status = StatusCorrentista.ATIVO
            elif col == restrito["col"]:
                status = StatusCorrentista.RESTRITO
            else:
                status = StatusCorrentista.INATIVO
            break
        elif col == ativo["col"]:
            col = restrito["col"]
            continue
        elif col == restrito["col"]:
            col = inativo["col"]
            continue
        elif flag_status not in status_permitidos:
            user_functions.exibirMensagem("Informe X para marcar o status ou deixe em branco!")
            user_functions.esperar_tecla()
            user_functions.limpar_linha()
        break
    
    if not status:
        if correntista_atual:
            status = correntista_atual.status
        else:
            status = StatusCorrentista.ATIVO
    
    if correntista_atual and status != correntista_atual.status:
        if status == StatusCorrentista.ATIVO:
            user_functions.exibir_valor(info["lin"], ativo["col"], "X")
            user_functions.exibir_valor(info["lin"], restrito["col"], " ")
            user_functions.exibir_valor(info["lin"], inativo["col"], " ")
        elif status == StatusCorrentista.RESTRITO:
            user_functions.exibir_valor(info["lin"], ativo["col"], " ")
            user_functions.exibir_valor(info["lin"], restrito["col"], "X")
            user_functions.exibir_valor(info["lin"], inativo["col"], " ")
        else:
            user_functions.exibir_valor(info["lin"], ativo["col"], " ")
            user_functions.exibir_valor(info["lin"], restrito["col"], " ")
            user_functions.exibir_valor(info["lin"], inativo["col"], "X")

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
    fl_sair, uf = digitar_uf()
    if fl_sair:
        return
    fl_sair, cep = digitar_cep()
    if fl_sair:
        return
    fl_sair, telefone = digitar_telefone()
    if fl_sair:
        return
    fl_sair, status = digitar_status()
    if fl_sair:
        return

    while True:
        user_functions.exibirMensagem(linha_mensagem, 3, "Confirma os dados (S/N): ")
        confimar = user_functions.esperar_tecla().upper()
        if confimar != "S" and confimar != "N":
            user_functions.exibirMensagem(linha_mensagem, 3, "Digite apenas S ou N")
            user_functions.esperar_tecla()
            continue
        break
    if confimar == "S":
        Correntista.salvar_correntista(Correntista(num_cpf, nome, endereco, numero, complemento, bairro,
                                            cidade, uf, cep, data_nasc, telefone, status, date.today()))
        
def iniciar():
    user_functions.limpar_tela()
    user_functions.posicionarCursor(4, 2)
    print(titulos_telas["cadastro_correntista"])
    user_functions.desenhar_tela(layout_correntistas)
    limpar_campos_tela()
    posicionarCursor(linha_mensagem, 2)
    opcao = user_functions.esperar_tecla().upper()
    return opcao

def novo_cadastro():
    while True:
        num_cpf = digitar_cpf()
        if num_cpf == 99999999999:
            break
        correntista = Correntista.get_correntista_por_cpf(num_cpf)
        if correntista:
            user_functions.exibirMensagem(linha_mensagem, 3, "CPF já cadastrado!")
            user_functions.esperar_tecla()
            user_functions.limpar_linha()
            continue
        processar_digitacao(num_cpf)
        break

def alterar_cadastro():
    global correntista_atual
    while True:
        num_cpf = digitar_cpf()
        if num_cpf == 99999999999:
            break
        correntista_atual = Correntista.get_correntista_por_cpf(num_cpf)
        if not correntista_atual:
            user_functions.exibirMensagem(linha_mensagem, 3, "CPF não cadastrado!")
            user_functions.esperar_tecla()
            user_functions.limpar_linha()
            continue
        limpar_campos_tela(True)
        Correntista.exibir_dados_em_tela(correntista_atual, campos_correntista)
        processar_digitacao(num_cpf)
        break

def excluir_cadastro():
    global correntista_atual
    while True:
        num_cpf = digitar_cpf()
        if num_cpf == 99999999999:
            break
        correntista_atual = Correntista.get_correntista_por_cpf(num_cpf)
        if not correntista_atual:
            user_functions.exibirMensagem(linha_mensagem, 3, "CPF não cadastrado!")
            user_functions.esperar_tecla()
            user_functions.limpar_linha()
            continue
        limpar_campos_tela(True)
        Correntista.exibir_dados_em_tela(correntista_atual, campos_correntista)
        user_functions.exibirMensagem(linha_mensagem, 3, "Deseja realmente excluir este correntinta? (S/N) ")
        confirmar = ""
        while confirmar != "S" and confirmar != "N":
            confirmar = user_functions.esperar_tecla()
            if confirmar == "S":
                excluido = Correntista.excluir_correntista(num_cpf)
                if excluido:
                    user_functions.exibirMensagem(linha_mensagem, 3, "Correntista excluído com sucesso!")
                    user_functions.esperar_tecla()
                    break
                else:
                    user_functions.exibirMensagem(linha_mensagem, 3, "Exclusão não efetuada! Problemas no processo!")
                    user_functions.esperar_tecla()
                    break
        break

def consultar_cadastro():
    global correntista_atual
    while True:
        num_cpf = digitar_cpf()
        if num_cpf == 99999999999:
            break
        correntista_atual = Correntista.get_correntista_por_cpf(num_cpf)
        if not correntista_atual:
            user_functions.exibirMensagem(linha_mensagem, 3, "CPF não cadastrado!")
            user_functions.esperar_tecla()
            user_functions.limpar_linha()
            continue
        limpar_campos_tela(True)
        Correntista.exibir_dados_em_tela(correntista_atual, campos_correntista)
        user_functions.exibirMensagem(linha_mensagem, 3, "Pressione qualquer tecla para continuar...")
        user_functions.esperar_tecla()
        break

def visualizar_relatorio():
    user_functions.limpar_tela()
    user_functions.limpar_linha(2, 2, 75)
    posicionarCursor(2, 2)
    print(titulos_telas["relatorio_correntista"])
    user_functions.desenhar_tela(layout_rel_correntistas, 6, 28)
    if not lista_correntistas:
        user_functions.exibirMensagem(linha_mensagem, 3, "Nenhum correntista cadastrado!")
        user_functions.esperar_tecla()
        return
    else:
        linha = 5
        for cpf, correntista in sorted(lista_correntistas.items(), key=lambda item: item[1].nome):
            linha += 1
            cpf_formatado = user_functions.formatar_cpf(correntista.num_cpf)
            data_formatada = user_functions.formatar_data(correntista.data_nasc)
            posicionarCursor(linha, 3)
            print(cpf_formatado, correntista.nome.ljust(50, " "), correntista.telefone.ljust(13, " "), data_formatada, sep= " ║ ")
            if linha == 28:
                posicionarCursor(linha_mensagem, 10)
                opcao = user_functions.esperar_tecla().upper()
                if opcao == "R":
                    break
                else:
                    limpar_tela_relatorio()
    user_functions.limpar_linha()
    user_functions.exibirMensagem(linha_mensagem, 3, "Fim da listagem. Pressione qualquer tecla para retornar ")
    user_functions.esperar_tecla()
    user_functions.limpar_tela()
    user_functions.posicionarCursor(4, 2)
    print(titulos_telas["cadastro_correntista"])
    linha3 = layout_tela_principal[2]
    linha29 = layout_tela_principal[28]
    user_functions.exibir_valor(linha3["lin"], linha3["col"], linha3["value"])
    user_functions.exibir_valor(linha29["lin"], linha29["col"], linha29["value"])
    user_functions.desenhar_tela(layout_correntistas)
