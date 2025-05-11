from database.banco import Banco
from database.base_repository import BaseRepository
from models.versao import Versao

class VersaoRepository(BaseRepository[Versao]):
    def __init__(self):
        super().__init__(Banco.get_instance(), Versao, "versoes")

    def create_table(self):
        command_text = """
        CREATE TABLE IF NOT EXISTS versoes(
          versao INTEGER NOT NULL PRIMARY KEY,
          release INTEGER NOT NULL,
          build INTEGER NOT NULL,
          compile INTEGER NOT NULL
        )"""
        return self.banco.executar(command_text)
