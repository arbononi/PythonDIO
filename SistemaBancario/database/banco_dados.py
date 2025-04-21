import json
import os
from datetime import date
from Models.Correntista import Correntista
from Models.ContaCorrente import ContaCorrente
from Models.SaldoContas import SaldoConta
from Models.Transacao import Transacao

from Models.TiposEnum import StatusCorrentista

CAMINHO_CORRENTISTAS = os.path.join(os.path.dirname(__file__), "dados", "correntistas.json")
CAMINHO_CONTAS = os.path.join(os.path.dirname(__file__), "dados", "contas.json")
CAMINHO_SALDOS = os.path.join(os.path.dirname(__file__), "dados", "saldos.json")
CAMINHO_TRANSACOES = os.path.join(os.path.dirname(__file__), "dados", "transacoes.json")

Lista_Correntistas = {}
Lista_ContaCorrente = {}
Lista_SaldoContas = {}
Lista_Transacoes = {}

# Função para carregar os correntistas do JSON
def carregar_correntistas():
    global Lista_Correntistas
    try:
        with open(CAMINHO_CORRENTISTAS, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            Lista_Correntistas = {
                int(cpf): Correntista(
                    num_cpf=int(d["num_cpf"]),
                    nome=d["nome"],
                    endereco=d["endereco"],
                    numero=d["numero"],
                    complemento=d["complemento"],
                    bairro=d["bairro"],
                    cidade=d["cidade"],
                    uf=d["uf"],
                    cep=int(d["cep"]),
                    data_nasc=date.fromisoformat(d["data_nasc"]),
                    telefone=d["telefone"],
                    status=StatusCorrentista[d["status"]],
                    data_cadastro=date.fromisoformat(d["data_cadastro"])
                )
                for cpf, d in dados.items()
            }
    except FileNotFoundError:
        Lista_Correntistas = {}

# Função para salvar os correntistas no JSON
def salvar_correntistas():
    with open(CAMINHO_CORRENTISTAS, 'w', encoding='utf-8') as f:
        json.dump({cpf: c.to_dict() for cpf, c in Lista_Correntistas.items()}, f, indent=4, ensure_ascii=False)

# Mesmo esquema para ContaCorrente
def carregar_contas():
    global Lista_ContaCorrente
    try:
        with open(CAMINHO_CONTAS, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            Lista_ContaCorrente = {
                int(num_conta): ContaCorrente(
                    num_conta=int(d["num_conta"]),
                    num_cpf=int(d["num_cpf"]),
                    data_abertura=date.fromisoformat(d["data_abertura"]),
                    limite_especial=float(d["limite_especial"]),
                    tipo_conta=ContaCorrente.get_tipo_conta_by_name(d["tipo_conta"]),
                    status=ContaCorrente.get_status_conta_by_name(d["status"]),
                    data_encerramento=date.fromisoformat(d["data_encerramento"]) if d["data_encerramento"] else None
                )
                for num_conta, d in dados.items()
            }
    except FileNotFoundError:
        Lista_ContaCorrente = {}

def salvar_contas():
    with open(CAMINHO_CONTAS, 'w', encoding='utf-8') as f:
        json.dump({num: c.to_dict() for num, c in Lista_ContaCorrente.items()}, f, indent=4, ensure_ascii=False)

# Função carregar saldo de contas
def carregar_saldo_contas():
    global Lista_SaldoContas
    try:
        with open(CAMINHO_SALDOS, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            Lista_SaldoContas = {
                int(num_conta): SaldoConta(
                    num_conta=int(d["num_conta"]),
                    data_saldo=date.fromisoformat(d["data_saldo"]),
                    saldo_atual=float(d["saldo_atual"])
                )
                for num_conta, d in dados.items()
            }
    except FileNotFoundError:
        Lista_SaldoContas ={}

def salvar_saldo_contas():
    with open(CAMINHO_SALDOS, 'w', encoding='utf-8') as f:
        json.dump({num: c.to_dict() for num, c in Lista_SaldoContas.items()}, f, indent=4, ensure_ascii=False)

# Função carregar transações
def carregar_transacoes():
    global Lista_Transacoes
    try:
        with open(CAMINHO_TRANSACOES, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            Lista_Transacoes = {
                int(num_transacao): Transacao(
                    num_transacao=int(d["num_transacao"]),
                    num_conta=int(d["num_conta"]),
                    data_transacao=date.fromisoformat(d["data_transacao"]),
                    valor=float(d["valor"]),
                    tipo=d["tipo"]
                )
                for num_transacao, d in dados.items()
            }
    except FileNotFoundError:
        Lista_Transacoes = {}

def salvar_transacoes():
    with open(CAMINHO_TRANSACOES, 'w', encoding='utf-8') as f:
        json.dump({num: t.to_dict() for num, t in Lista_Transacoes.items()}, f, indent=4, ensure_ascii=False)

# Chamada automática ao importar
carregar_correntistas()
carregar_contas()
carregar_saldo_contas()
carregar_transacoes()