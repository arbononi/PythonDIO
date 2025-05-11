from dataclasses import dataclass
from datetime import datetime
from models.tiposenum import TipoOperacao, TipoTransacao, TipoChavePix
from models.conta import ContaDTO

@dataclass
class Transacao:
    id: int
    data_movto: datetime
    id_conta_origem: int
    id_conta_destino: int
    tipo_operacao: TipoOperacao
    tipo_transacao: TipoTransacao
    tipo_chave_pix: TipoChavePix
    chave_pix: str
    linha_digitavel: str
    saldo_anterior: float
    valor_movto: float
    saldo_final: float
    nome_autor: str
    mensagem: str

    def as_tuple(self):
        return(
            self.id,
            self.data_movto,
            self.id_conta_origem,
            self.id_conta_destino,
            self.tipo_operacao,
            self.tipo_transacao,
            self.tipo_chave_pix,
            self.chave_pix,
            self.linha_digitavel,
            self.saldo_anterior,
            self.valor_movto,
            self.saldo_final,
            self.nome_autor,
            self.mensagem
        )
    
@dataclass
class TransacaoDTO:
    transacao: Transacao
    conta_origem: ContaDTO
    conta_destino: ContaDTO