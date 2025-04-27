from database.banco import Banco
from views.contas_view import ContasView

class ContasController:
    def __init__(self, banco: Banco):
        self.banco = banco

    def iniciar(self):
        app = ContasView(self.banco)
        app.iniciar()