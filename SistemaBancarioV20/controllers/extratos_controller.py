from utils import user_functions
from views.extratos_view import iniciar

class ExtratoController:
    def __init__(self):
        pass

    def iniciar(self):
        opcao = iniciar()
        if opcao == "R":
            return