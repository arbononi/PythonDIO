from database.banco import Banco
from views.clientes_view import ClientesView

class ClientesController:
    def __init__(self, banco: Banco):
        self.banco = banco

    def iniciar(self):
        app = ClientesView(self.banco)
        app.iniciar()
