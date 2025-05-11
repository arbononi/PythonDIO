from database.versao_repository import VersaoRepository
from models.versao import Versao

class VersaoController:
    _repo = None

    def __init__(self):
        self._repo = VersaoRepository()

    def checar_versao_atual(self):
        fl_ok = True
        mensagem = ""
        versao_sistema = Versao.get_init_version()
        versao_banco, _ = self._repo.get_by_id(versao_sistema.versao)
        if versao_banco:
            if versao_banco.versao != versao_sistema.versao:
                # TODO Criar verificação de diferenças entre as versões
                fl_ok = False
                mensagem = "Versão do banco difere do sistema. Verificar necessidade de atualização"
            elif versao_banco.release != versao_sistema.release or versao_banco.build != versao_sistema.build or versao_banco.compile != versao_sistema.compile:
                versao_banco.release = versao_sistema.release
                versao_banco.build = versao_sistema.build
                versao_banco.compile = versao_sistema.compile
                fl_ok, mensagem = self._repo.update(versao_banco)
        else:
            versao_banco = versao_sistema
            fl_ok, _, mensagem = self._repo.add(versao_sistema)

        return fl_ok, mensagem, versao_banco
                
                    