import sys
import msvcrt
from models.tiposenum import estados, MOSTRAR_CURSOR, OCULTAR_CURSOR, TipoPessoa
from datetime import datetime, date

def esperar_tecla(ocultar_cursor: bool=True):
    if ocultar_cursor:
        print(OCULTAR_CURSOR)
    opcao = msvcrt.getch().decode("utf-8").upper()
    if ocultar_cursor:
        print(MOSTRAR_CURSOR)
    return opcao

def limpar_linha(linha: int=30, coluna: int=2, tamanho: int=98, background=False):
    posicionarCursor(linha, coluna)
    spaces = " " * tamanho
    if background:
        spaces = "_" * tamanho
        print(spaces, end="")
    else:
        print(spaces, end="")
    posicionarCursor(linha, coluna)

def posicionarCursor(linha: int, coluna: int):
    sys.stdout.write(f"\033[{linha};{coluna}H")

def exibir_mensagem(mensagem: str, linha=30, coluna=3):
    limpar_linha(linha)
    posicionarCursor(linha, coluna)
    print(mensagem, end="")
    return esperar_tecla()

def exibir_conteudo(conteudo: str, linha=30, coluna=3):
    posicionarCursor(linha, coluna)
    print(conteudo, end="")

def limpar_tela(start: int=4, stop: int=29, column: int=2, size: int=98):
    for linha in range(start, stop):
        posicionarCursor(linha, column)
        print(" " * size, end="")

def desenhar_tela(layout, line_loop=0, stop_loop=0):
    for linha in layout:
        if line_loop == linha["lin"] and stop_loop > 0:
            processar = True
            while processar:
                posicionarCursor(line_loop, linha["col"])
                print(linha["value"])
                if line_loop < stop_loop:
                    line_loop += 1
                else:
                    processar = False
        else:
            posicionarCursor(linha["lin"], linha["col"])
            print(linha["value"])

def validar_documento(cpf_cnpj: str, tipo_pessoa: TipoPessoa):
    if tipo_pessoa == TipoPessoa.FISICA and len(cpf_cnpj) != 11:
        return False, "CPF deve possuir, exatamente, 11 dígitos"
    elif tipo_pessoa == TipoPessoa.JURIDICA and len(cpf_cnpj) != 14:
        return False, "CNPJ deve possuir, exatamente, 14 dígitos"
    return True, None

def validar_estado(uf: str):
    if uf.upper() not in estados:
        return False, None, "UF inválida!"
    return True, uf.upper(), None

def validar_cep(cep: str):
    if (len(cep) < 8):
        return False, None, "CEP incompleto"
    try:
        cep_num = int(cep)
        return True, cep_num, None
    except ValueError as error:
        return False, None, f"Erro ao validar CEP: {error}!"

def formatar_documento(cpf_cnpj: str, tipo_pessoa: TipoPessoa):
    try:
        numero_documento = int(cpf_cnpj)

        if tipo_pessoa == TipoPessoa.FISICA:
            cpf_formatado = f"{numero_documento:011d}"
            return True, f"{cpf_formatado[:3]}.{cpf_formatado[3:6]}.{cpf_formatado[6:9]}-{cpf_formatado[9:]}"
        
        cnpj_formatado = f"{numero_documento:014d}"
        return True, f"{cnpj_formatado[:2]}.{cnpj_formatado[2:5]}.{cnpj_formatado[5:8]}/{cnpj_formatado[88:12]}-{cnpj_formatado[12:]}"
    except ValueError as error:
        return False, f"Erro ao formatar CPF/CNPJ: {error}"

def formatar_cep(cep: int):
    try:
        cep_formatado = f"{cep:008d}"
        return f"{cep_formatado[:2]}.{cep_formatado[2:5]}-{cep_formatado[5:]}"
    except ValueError as error:
        return False, f"Erro ao formatar CEP: {error}"
    
def formatar_data(data: date, exibir_dia_semana=False, antes=False):
    if exibir_dia_semana:
        if antes:
           return data.strftime("%a %d/%m/%Y")
        else:
            return data.strftime("%d/%m/%Y") + " " + data.strftime("%a")
        
    return data.strftime("%d/%m/%Y")

def formatar_data_hora(data: datetime):
    return data.strftime("%d/%m/%Y %H:%M")

def formatar_valor(valor, isMoeda: bool=False) -> str:
    valor_formatado = ""
    try:
        if not isinstance(valor, float):
            valor_formatado = f"{valor:,.0f}".replace(",", "X").replace(".", ",").replace("X", ".")
        else:
            valor_formatado = f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        return True, valor_formatado
    except Exception as error:
        return False, f"Erro ao formatar valor: {error}"
    
def validar_data(entrada: str, permitir_futuro=False):
    formatos_aceitos = [
        "%d/%m/%Y",
        "%d-%m-%Y",
        "%Y-%m-%d",
        "%d.%m.%Y",
        "%d %m %Y",
        "%d/%m/%y",
        "%d-%m-%y",
        "%d%m%Y",
        "%d%m%y"
    ]

    for formato in formatos_aceitos:
        try:
            data = datetime.strptime(entrada, formato).date()
            if not permitir_futuro and data > date.today():
                return False, None, "A data não pode ser no futuro."
            return True, data, None
        except ValueError:
            continue  # Tenta o próximo formato
    return False, None, "Formato inválido. Tente novamente com um dos formatos aceitos."

def validar_data_hora(entrada: str, permitir_futuro=False):
    formatos_aceitos = [
        "%d/%m/%Y %H:%M",
        "%d-%m-%Y %H:%M",
        "%Y-%m-%d %H:%M",
        "%d.%m.%Y %H:%M",
        "%d %m %Y %H:%M",
        "%d/%m/%y %H:%M",
        "%d-%m-%y %H:%M",
        "%d%m%Y%H%M",
        "%d%m%y%H%M"
    ]

    for formato in formatos_aceitos:
        try:
            data = datetime.strptime(entrada, formato)
            if not permitir_futuro and data.date() > date.today():
                return False, None, "A data não pode ser no futuro."
            return True, data, None
        except ValueError:
            continue  # Tenta o próximo formato
    return False, None, "Formato inválido. Tente novamente com um dos formatos aceitos."