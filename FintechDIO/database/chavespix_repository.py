from dataclasses import fields
from database.banco import Banco
from database.base_repository import BaseRepository
from database.contas_repository import ContasRepository
from models.conta import  ChavesPix
from models.tiposenum import TipoChavePix

class ChavesPixRepository(BaseRepository[ChavesPix]):
    def __init__(self, contas_repository: ContasRepository):
        super().__init__(Banco.get_instance(), ChavesPix, "chavespix")
        self.contas_repository = contas_repository

    def create_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS chavespix(
           id_conta INTEGER NOT NULL,
           tipo_chave INTEGER NOT NULL,
           chave_pix TEXT NOT NULL,
           PRIMARY KEY ("id_conta", "tipo_chave")
           )"""
        return self.banco.executar(sql)

    def get_chaves_by_id_conta(self, id_conta:int, limite: 18, offset=0):
        conta_dto = self.contas_repository.get_by_id(id_conta)
        query = "Select * from chavespix where id_conta = :id_conta order by tipo_chave limit :limite OFFSET :offset"
        params = [id_conta, limite, offset]
        cursor, mensagem = self.banco.executar(query, params)
        if not cursor:
            return None, mensagem
        rows = cursor.fetchall()
        lista_chaves = []
        for row in rows:
            kwargs = {}
            for f in fields(ChavesPix):
                if f.name == "conta":
                    kwargs[f.name] = conta_dto
                    continue
                v = row[f.name]
                kwargs[f.name] = v
            lista_chaves.append(ChavesPix(**kwargs))
        if len(lista_chaves) > 0:
            return lista_chaves, ""
        return None, "Nenhuma chave pix encontrada"
    
    def check_chave_pix_exists(self, id_conta: int, tipo_chave: TipoChavePix) -> ChavesPix:
        conta_dto = self.contas_repository.get_by_id(id_conta)
        query = "Select * from chavespix where id_conta = :id_conta and tipo_chave = :tipo_chave"
        params = [id_conta, tipo_chave]
        cursor, mensagem = self.banco.executar(query, params)
        if not cursor:
            return None, mensagem
        row = cursor.fetchone()
        return ChavesPix(conta=conta_dto, id_conta=conta_dto.conta.id, tipo_chave=row["tipo_chave"], chave_pix=row["chave_pix"]), ""
                
