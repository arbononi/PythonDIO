from enum import Enum

class TipoOperacao(Enum):
    DEBITO = 1
    CREDITO = 2

class StatusCliente(Enum):
    INATIVO = 0
    ATIVO = 1
    RESTRITO = 2
    BLOQUEADO = 3

class StatusConta(Enum):
    PENDENTE = 0
    ATIVA = 1
    SUSPENSA = 2
    BLOQUEADA = 3
    INATIVA = 4
    ENCERRADA = 5

class TipoConta(Enum):
    POUPANCA = 1
    CONTA_CORRENTE = 2
    APLICACAO = 3

class TipoTransacao(Enum):
    DEPOSITO = 1
    SAQUE = 2
    TRANSFERENCIA = 3
    PIX = 4
    DOC = 5
    PAGAMENTOS = 6

class TipoPessoa(Enum):
    FISICA = "F"
    JURIDICA = "J"
    
estados = [ 
    "AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO",
    "MA", "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR",
    "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO"
]

OCULTAR_CURSOR = '\033[?25l'
MOSTRAR_CURSOR = '\033[?25h'