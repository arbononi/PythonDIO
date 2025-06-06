import sys
import msvcrt
import shutil
from datetime import datetime, date
from models.tiposenum import estados, TipoPessoa

OCULTAR_CURSOR = '\033[?25l'
MOSTRAR_CURSOR = '\033[?25h'

def esperar_tecla(ocultar_cursor: bool=True):
    if ocultar_cursor:
        print(OCULTAR_CURSOR, end="")
    tecla = msvcrt.getch().decode("utf-8").upper()
    if ocultar_cursor:
        print(MOSTRAR_CURSOR, end="")
    if tecla == "\r":
        tecla = ""
    return tecla

def posicionar_cursor(lin, col):
    sys.stdout.write(f"\033[{lin};{col}H")

def limpar_linha(lin=30, col=2, size=98, background=False):
    posicionar_cursor(lin, col)
    if background:
        print("_" * size, end="")
    else:
        print(" " * size, end="")
    posicionar_cursor(lin, col)

def exibir_mensagem(mensagem: str, lin=30, col=3, skip_line: str="", wait_key: bool=False):
    limpar_linha(lin, col, size=97)
    posicionar_cursor(lin, col)
    print(mensagem, end=skip_line)
    if wait_key:
        esperar_tecla()

def exibir_conteudo(conteudo: str, lin: int=30, col: int=3, desativada=False):
    posicionar_cursor(lin, col)
    if desativada:
        print(f"\033[38;5;250;48;5;240m{conteudo}\033[0m")
    else:
        print(conteudo, end="")

def limpar_tela(start: int=4, stop: int=29, col: int=2, size: int=98):
    for lin in range(start, stop):
        posicionar_cursor(lin, col)
        print(" " * size, end="")

def desenhar_tela(layout, line_loop=0, stop_loop=0):
    for config in layout:
        if line_loop == config["lin"] and stop_loop > 0:
            process = True
            while process:
                posicionar_cursor(line_loop, config["col"])
                print(config["value"], end="")
                if line_loop < stop_loop:
                    line_loop += 1
                else:
                    process = False
        else:
            posicionar_cursor(config["lin"], config["col"])
            print(config["value"], end="")

def get_data_atual():
    return datetime.now().date()

def validar_cpf_cnpj(num_cpf_cnpj: str, tipo_pessoa: TipoPessoa=None):
    size = len(num_cpf_cnpj)
    if tipo_pessoa != None:
        match tipo_pessoa:
            case TipoPessoa.FISICA:
                if size != 11:
                    return False, "Número de dígitos inválido para CPF"
            case TipoPessoa.JURIDICA:
                if size != 14:
                    return False, "Número de dígitos inválido para CNPJ"
            case None:
                return False, "Tipo de pessoa não informada para validação CPF/CNPJ"
    return True, None

def validar_estado(uf: str):
    if uf.upper() not in estados:
        return False, "UF inválida!"
    return True, None

def validar_cep(cep: str):
    if (len(cep) < 8):
        return False, None, "CEP incompleto"
    try:
        cep_num = int(cep)
        return True, cep_num, None
    except ValueError:
        return False, None, "CEP não é um número válido!"
    
def formatar_cpf_cnpj(num_cpf_cnpj: str):
    try:
        if len(num_cpf_cnpj) == 11:
           cpf_formatado = f"{int(num_cpf_cnpj):011d}"
           return True, f"{cpf_formatado[:3]}.{cpf_formatado[3:6]}.{cpf_formatado[6:9]}-{cpf_formatado[9:]}"
        elif len(num_cpf_cnpj) == 14:
            return True, f"{num_cpf_cnpj[0:2]}.{num_cpf_cnpj[2:5]}.{num_cpf_cnpj[5:8]}/{num_cpf_cnpj[8:12]}-{num_cpf_cnpj[12:14]}"
    except ValueError as e:
        return False, f"CPF/CNPJ não é um número válido!: {num_cpf_cnpj}"
         
def formatar_cep(cep: int):
    #14160530
    try:
        cep_formatado = f"{cep:008d}"
        return f"{cep_formatado[:2]}.{cep_formatado[2:5]}-{cep_formatado[5:]}"
    except ValueError as error:
        exibir_mensagem(30, 3, error, wait_key=True)
    
def formatar_data(data: date, exibir_dia_semana=False, antes=False):
    if exibir_dia_semana:
        if antes:
           return data.strftime("%a %d/%m/%Y")
        else:
            return data.strftime("%d/%m/%Y") + " " + data.strftime("%a")
        
    return data.strftime("%d/%m/%Y")

def formatar_data_hora(data: datetime):
    return data.strftime("%d/%m/%Y %H:%M:%S")

def formatar_valor(valor, isMoeda: bool=False) -> str:
    valor_formatado = ""
    try:
        if not isinstance(valor, float):
            valor_formatado = f"{valor:,.0f}".replace(",", "X").replace(".", ",").replace("X", ".")
        else:
            valor_formatado = f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        return valor_formatado
    except Exception as error:
        exibir_mensagem(30, 3, error, wait_key=True)
        return valor_formatado

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

def datetime_to_iso(data: datetime):
    return data.strftime("%Y-%m-%d %H:%M:%S")

def date_to_iso(data: date):
    return data.strftime("%Y-%m-%d %H:%M:%S")

def date_brasilian_format(data: str):
    try:
        data_obj = datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
        return data_obj.strftime("%d/%m/%Y %H:%M:%S")
    except Exception as e:
        return f"Data inválida! {e}"
    
def datetime_brasilian_format(data: str):
    try:
        data_obj = datetime.strptime(data, "%Y-%m-%d")
        return data_obj.strftime("%d/%m/%Y")
    except Exception as e:
        return f"Data inválida! {e}"
