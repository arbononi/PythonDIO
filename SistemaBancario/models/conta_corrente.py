from datetime import datetime
from tiposenum import TipoContaCorrente, StatusContaCorrente

class ContaCorrente:
    def __init__(self, num_conta: int, idcorrentista: int, data_abertura: datetime, limite_especial: float,
                 tipo_conta : TipoContaCorrente, status : StatusContaCorrente, data_encerramento: datetime=None):
        self.num_conta = num_conta
        self.idcorrentista = idcorrentista
        self.data_abertura = data_abertura
        self.limite_especial = limite_especial
        self.tipo_conta = tipo_conta
        self.status = status
        self.data_encerramento = data_encerramento