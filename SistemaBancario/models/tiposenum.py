from enum import Enum

class TipoTransacao(Enum):
    DEPOSITO = 1
    SAQUE = 2

class TipoContaCorrente(Enum):
    POUPANCA = 1
    CONTACORRENTE = 2

class StatusCorrentista(Enum):
    ATIVO = 1
    RESTRITO = 2
    INATIVO = 2

class StatusContaCorrente(Enum):
    PENDENTE = 0
    ATIVA = 1
    BLOQUEADA = 2
    INATIVA = 3
    ENCERRADA = 4

class Estados(Enum):
    "AC" "AL" "AM" "AP" "BA" "CE" "DF" "ES" "GO"
    "MA" "MG" "MS" "MT" "PA" "PB" "PE" "PI" "PR"
    "RJ" "RN" "RO" "RR" "RS" "SC" "SE" "SP" "TO"

class TipoOperacao(Enum):
    CONSULTA = 0
    INCLUSAO = 1
    ALTERACAO = 2
    EXCLUSAO = 3

OCULTAR_CURSOR = '\033[?25l'
MOSTRAR_CURSOR = '\033[?25h'
PRETO_NO_BRANCO = "\033[47;30m"
RESET = "\033[0m"
