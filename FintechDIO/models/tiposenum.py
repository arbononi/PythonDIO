from enum import Enum

class TipoOperacao(Enum):
    CREDITO = 1
    DEBITO = 2

    @property   
    def descricao(self):
        match self:
            case TipoOperacao.CREDITO:
                return "credito"
            case TipoOperacao.DEBITO:
                return "debito"

class TipoTransacao(Enum):
    DEPOSITO = 1
    SAQUE = 2
    PIX = 3
    PAGAMENTO = 4
    TRANSFERENCIA = 5
    DOC = 6

    @property
    def descricao(self):
        match self:
            case TipoTransacao.DEPOSITO:
                return "deposito"
            case TipoTransacao.SAQUE:
                return "saque"
            case TipoTransacao.PIX:
                return "pix"
            case TipoTransacao.PAGAMENTO:
                return "pagamento"
            case TipoTransacao.TRANSFERENCIA:
                return "transferencia"
            case TipoTransacao.DOC:
                return "doc"

class TipoPessoa(Enum):
    FISICA = 1
    JURIDICA = 2

    @property
    def descricao(self):
        match self:
            case TipoPessoa.FISICA:
                return "fisica"
            case TipoPessoa.JURIDICA:
                return "juridica"

class TipoConta(Enum):
    CONTA_CORRENTE = 1
    POUPANCA = 2
    APLICACAO = 3

    @property
    def descricao(self):
        match self:
            case TipoConta.CONTA_CORRENTE:
                return "conta_corrente"
            case TipoConta.POUPANCA:
                return "poupanca"
            case TipoConta.APLICACAO:
                return "aplicacao"

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

    @property
    def descricao(self):
        match self:
            case StatusConta.ANALISE:
                return "analise"
            case StatusCliente.ATIVO:
                return "ativo"
            case StatusCliente.RESTRITO:
                return "restrito"
            case StatusCliente.BLOQUEADO:
                return "bloqueado"
            case StatusCliente.INATIVO:
                return "inativo"

class StatusConta(Enum):
    ANALISE = 1
    ATIVA = 2
    SUSPENSA = 3
    BLOQUEADA = 4
    INATIVA = 5
    ENCERRADA = 6

    @property
    def descricao(self):
        match self:
            case StatusConta.ANALISE:
                return "analise"
            case StatusConta.ATIVA:
                return "ativa"
            case StatusConta.SUSPENSA:
                return "suspensa"
            case StatusConta.BLOQUEADA:
                return "bloqueada"
            case StatusConta.INATIVA:
                return "inativa"
            case StatusConta.ENCERRADA:
                return "encerrada"

# class OperationResult(Enum):
#     ERROR = 1
#     SUCCESS = 0

class TipoChavePix(Enum):
    NENHUMA = 0
    CPF = 1
    CNPJ = 2
    TELEFONE = 3
    EMAIL = 4
    CHAVE_ALEATORIA = 5

    @property
    def descricao(self):
        match self:
            case TipoChavePix.CPF:
                return "cpf"
            case TipoChavePix.CNPJ:
                return "cnpj"
            case TipoChavePix.TELEFONE:
                return "telefone"
            case TipoChavePix.EMAIL:
                return "email"
            case TipoChavePix.CHAVE_ALEATORIA:
                return "chave_aleatoria"
            case None:
                return "indefinida"
            
estados = [ "AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO",
            "MA", "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR",
            "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO"]
