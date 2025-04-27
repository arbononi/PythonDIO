from models.cliente import Cliente
from models.conta import Conta
from models.transacao import Transacao
from models.versao import Versao

def create_tables(banco):
    fl_clientes, mensagem_clientes = Cliente.create_table(banco)
    fl_contas, mensagem_contas = Conta.create_table(banco)
    fl_transacoes, mensagem_transacoes = Transacao.create_table(banco)
    fl_versao, mensagem_versao = Versao.create_table(banco)

    mensagens = []
    if not fl_clientes:
        mensagens.append(mensagem_clientes)
    if not fl_contas:
        mensagens.append(mensagem_contas)
    if not fl_transacoes:
        mensagens.append(mensagem_transacoes)
    if not fl_versao:
        mensagens.append(mensagem_versao)
    
    return len(mensagens) == 0, mensagens