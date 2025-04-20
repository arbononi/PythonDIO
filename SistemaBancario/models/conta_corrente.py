from datetime import date
import models.correntista
from models.tiposenum import TipoContaCorrente, StatusContaCorrente
from models.correntista import Correntista
from database.tables import lista_contas
from utils.user_functions import posicionarCursor
from utils import user_functions
import models

class ContaCorrente:
    def __init__(self, num_conta: int, num_cpf: int, data_abertura: date, limite_especial: float,
                 tipo_conta : TipoContaCorrente, status : StatusContaCorrente, data_encerramento: date=None):
        self.num_conta = num_conta
        self.num_cpf = num_cpf
        self.data_abertura = data_abertura
        self.limite_especial = limite_especial
        self.tipo_conta = tipo_conta
        self.status = status
        self.data_encerramento = data_encerramento

    def get_conta_by_numero(num_conta: int):
        return lista_contas.get(num_conta)
    
    def salvar_conta(self):
        lista_contas[self.num_conta] = self
    
    def excluir_conta(num_conta: int):
        return lista_contas.pop(num_conta, None)

    def proximo_num_conta():
        if not lista_contas:
            return 1
        return max(int(k) for k in lista_contas) + 1

    def exibir_dados_conta(self, config_tela):
        for campo, valor in vars(self).items():
            layout = config_tela.get(campo)
            if not layout:
                continue
            if isinstance(valor, date):
                if campo == "data_encerramento" and self.status != StatusContaCorrente.ENCERRADA:
                    continue
                posicionarCursor(layout["lin"], layout["col"])
                print(user_functions.formatar_data(valor))
            elif campo == "num_cpf":
                posicionarCursor(layout["lin"], layout["col"])
                print(user_functions.formatar_cpf(valor))
                correntista = models.correntista.Correntista.get_correntista_por_cpf(valor)
                if correntista:
                    posicionarCursor(config_tela["nome_cliente"]["lin"], config_tela["nome_cliente"]["col"])
                    print(correntista.nome.ljust(40, " ")[:40])
                    posicionarCursor(config_tela["data_cadastro"]["lin"], config_tela["data_cadastro"]["col"])
                    print(user_functions.formatar_data(correntista.data_cadastro))
            elif campo == "tipo_conta":
                name = valor.name.lower()
                posicionarCursor(layout[name], layout["col"])
                print("•")
            elif campo == "status":
                name = valor.name.lower()
                posicionarCursor(layout[name], layout["col"])
                print("•")
            elif isinstance(valor, float):
                posicionarCursor(layout["lin"], layout["col"])
                print(user_functions.formatar_valor(valor).rjust(12, " "))

    def get_tipo_conta_by_name(name: str):
        if name == TipoContaCorrente.POUPANCA.name:
            return TipoContaCorrente.POUPANCA
        return TipoContaCorrente.CONTA_CORRENTE
    
    def get_status_conta_by_name(name: str):
        if name == StatusContaCorrente.ATIVA.name:
            return StatusContaCorrente.ATIVA
        elif name == StatusContaCorrente.BLOQUEADA.name:
            return StatusContaCorrente.BLOQUEADA
        elif name == StatusContaCorrente.INATIVA.name:
            return StatusContaCorrente.INATIVA
        elif name == StatusContaCorrente.ENCERRADA.name:
            return StatusContaCorrente.ENCERRADA
        else:
            return StatusContaCorrente.PENDENTE
        
    