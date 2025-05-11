import re
from models.tiposenum import TipoChavePix
from utils.userfunctions import validar_cpf_cnpj

class ClienteInputvalidator:
    @staticmethod
    def name_validation(name: str):
        if name.strip() == "" or len(name.strip()) < 3:
            return False, "Nome do cliente não pode ficar em branco nem ser muito curto"
        return True, None
    
    def address_validation(address: str):
        if address.strip() == "" or len(address.strip()) < 3:
            return False, "Endereço não pode ficar em branco nem ser muito curto"
        return True, None
    
    def number_validation(number: str):
        if number.strip() == "":
            return False, "Número do endereço não pode ficar em branco!"
        return True, None
    
    def neighborhood_validation(neighborhodd: str):
        if neighborhodd.strip() == "" or len(neighborhodd.strip()) < 3:
            return False, "Bairro não pode ficar em branco nem ser muito curto"
        return True, None
    
    def city_validation(city: str):
        if city.strip() == "" or len(city.strip()) < 3:
            return False, "Nome da cidade não pode ficar em branco nem ser muito curto"
        return True, None

class TransacaoInputValidator:
    regex_telefone = re.compile(r"""
    ^\(?\d{2}\)?      # DDD com ou sem parênteses
    [\s-]?            # Espaço ou hífen opcional
    (                 # Início do grupo de tipo
        9\d{4}        # Celular: começa com 9 e tem 5 dígitos
        |             # ou
        [2-5]\d{3}    # Fixo: começa com 2-5 e tem 4 dígitos
    )
    -?\d{4}$          # Últimos 4 dígitos
""", re.VERBOSE)
    # regex_email = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$")
    # regex_email = re.compile(r'^[\w-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$')
    regex_email = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    
    @staticmethod
    def chave_pix_validate(chave_pix: str, tipo_chave: TipoChavePix) -> bool:
        fl_ok = True
        match tipo_chave:
            case TipoChavePix.CPF:
                fl_ok = validar_cpf_cnpj(chave_pix)
            case TipoChavePix.CNPJ:
                fl_ok = validar_cpf_cnpj(chave_pix)
            case TipoChavePix.TELEFONE:
                fl_ok = bool(TransacaoInputValidator.regex_telefone.mt(chave_pix.strip()))
            case TipoChavePix.EMAIL:
                fl_ok = bool(TransacaoInputValidator.regex_email.match(chave_pix.strip()))
            case TipoChavePix.CHAVE_ALEATORIA:
                pass
        return fl_ok
            