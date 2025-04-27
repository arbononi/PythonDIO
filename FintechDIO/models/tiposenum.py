from enum import Enum

class TipoOperacao(Enum):
    CREDITO = 1
    DEBITO = 2

class TipoTransacao(Enum):
    DEPOSITO = 1
    SAQUE = 2
    PIX = 3
    PAGAMENTO = 4
    TRANSFERENCIA = 5
    DOC = 6

class TipoPessoa(Enum):
    FISICA = 1
    JURIDICA = 2

class TipoConta(Enum):
    CONTA_CORRENTE = 1
    POUPANCA = 2
    APLICACAO = 3

class StatusCad(Enum):
    CONSULTA = 1
    INCLUSAO = 2
    ALTERACAO = 3
    EXCLUSAO = 4

class StatusCliente(Enum):
    ATIVO = 1
    RESTRITO = 2
    BLOQUEADO = 3
    INATIVO = 4

class StatusConta(Enum):
    ANALISE = 1
    ATIVA = 2
    SUSPENSA = 3
    BLOQUEADA = 4
    INATIVA = 5
    ENCERRADA = 6

class OperationResult(Enum):
    ERROR = 1
    SUCCESS = 0
    
estados = [ "AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO",
            "MA", "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR",
            "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO"]
