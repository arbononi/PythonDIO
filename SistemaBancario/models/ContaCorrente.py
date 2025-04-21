from datetime import date
from Models.TiposEnum import TipoContaCorrente, StatusContaCorrente
from Utils.user_functions import posicionarCursor
from Utils import user_functions
from Database import banco_dados
from Models.SaldoContas import SaldoConta

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

    def to_dict(self):
        return {
            "num_conta": self.num_conta,
            "num_cpf": self.num_cpf,
            "data_abertura": self.data_abertura.isoformat(),
            "limite_especial": self.limite_especial,
            "tipo_conta": self.tipo_conta.name,
            "status": self.status.name,
            "data_encerramento": self.data_encerramento.isoformat() if self.data_encerramento else None
        }
    
    def add_conta(self):
        banco_dados.Lista_ContaCorrente[self.num_conta] = self
        banco_dados.salvar_contas()
        saldo_conta = banco_dados.Lista_SaldoContas.get(self.num_conta)
        if not saldo_conta:
            saldo = SaldoConta(self.num_conta, self.data_abertura, 0.0)
            SaldoConta.add_saldo(saldo)
            
    def get_conta_by_numero(num_conta: int):
        return banco_dados.Lista_ContaCorrente.get(num_conta)
        
    def excluir_conta(num_conta: int):
        saldo = SaldoConta.excluir_saldo(num_conta)        
        return banco_dados.Lista_ContaCorrente.pop(num_conta, None)

    def proximo_num_conta():
        if not banco_dados.Lista_ContaCorrente:
            return 1
        return max(int(k) for k in banco_dados.Lista_ContaCorrente) + 1

    def exibir_dados_conta(self, config_tela):
        for campo, valor in vars(self).items():
            layout = config_tela.get(campo)
            if not layout:
                continue
            if isinstance(valor, date):
                posicionarCursor(layout["lin"], layout["col"])
                if campo == "data_encerramento" and self.status != StatusContaCorrente.ENCERRADA:
                    print(" " * 10, end="")
                    continue
                print(user_functions.formatar_data(valor))
            elif campo == "num_cpf":
                posicionarCursor(layout["lin"], layout["col"])
                print(user_functions.formatar_cpf(valor))
                correntista = banco_dados.Lista_Correntistas.get(valor)
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
        
    