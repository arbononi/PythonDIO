from datetime import datetime
from Database import banco_dados
from Models.TiposEnum import TipoTransacao
from Models.Transacao import Transacao
from Utils.user_functions import posicionarCursor

class Transacao:
    def __init__(self, id: int, data_movto : datetime, idconta: int, tipo_transacao: TipoTransacao,
                 saldo_anterior: float, valor_transacao: float, saldo_atual: float, flag_conciliada : bool):
        self.id = id
        self.data_movto = data_movto
        self.idconta = idconta
        self.tipo_transacao = tipo_transacao
        self.saldo_anterior = saldo_anterior
        self.valor_transacao = valor_transacao
        self.saldo_atual = saldo_atual
        self.flag_conciliada = flag_conciliada

    def to_dict(self):
        return {
            "id": self.id,
            "data_movto": self.data_movto.isoformat(),
            "idconta": self.idconta,
            "tipo_transacao": self.tipo_transacao.name,
            "saldo_anterior": self.saldo_anterior,
            "valor_transacao": self.valor_transacao,
            "saldo_atual": self.saldo_atual,
            "flag_conciliada": self.flag_conciliada
        }
    
    def add_transacao(self):
        banco_dados.Lista_Transacoes[self.id] = self
        banco_dados.salvar_transacoes()

    def remove_transacao(self):
        transacao = banco_dados.Lista_Transacoes.pop(self.id, None)
        banco_dados.salvar_transacoes()

    def get_transacao_by_id(id: int):
        return banco_dados.Lista_Transacoes.get(id, None)
    
    def exibir_dados(self: Transacao, config_tela):
        for campo, valor in vars(self).items():
            layout = config_tela.get(campo)
            if not layout:
                continue
            if campo == "tipo_transacao":
                name = valor.name.lower()
                posicionarCursor(layout["lin"], layout[name])
                print("•")
            elif isinstance(valor, datetime):
                posicionarCursor(layout["lin"], layout["col"])
                print(valor.strftime("%d/%m/%Y %H:%M"))
            elif isinstance(valor, float):
                posicionarCursor(layout["lin"], layout["col"])
                print(f"{valor:,.2f}".replace(".", ","))
            elif campo == "idconta":
                posicionarCursor(layout["lin"], layout["col"])
                print(str(valor).rjust(10, " "))
                conta_corrente = banco_dados.Lista_ContasCorrentes.get(valor, None)
                if conta_corrente:
                    posicionarCursor(config_tela["nome_correntista"]["lin"], config_tela["nome_correntista"]["col"])
                    correntista = banco_dados.Lista_Correntistas.get(conta_corrente.idcorrentista, None)
                    if correntista:
                        print(conta_corrente.nome_conta)
                    else:
                        print("Correntista não encontrado")
            else:
                posicionarCursor(layout["lin"], layout["col"])
                print(str(valor).rjust(10, " "))