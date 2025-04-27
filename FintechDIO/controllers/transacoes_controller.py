from database.banco import Banco
from views.transacoes_view import TransacoesView

class TransacoesController:
    def __init__(self, banco: Banco):
        self.banco = banco
    
    def iniciar(self):
        app = TransacoesView(self.banco)
        app.iniciar()