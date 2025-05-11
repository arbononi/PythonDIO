from datetime import date
from database.contas_repository import ContasRepository
from database.clientes_repository import ClientesRepository
from database.chavespix_repository import ChavesPixRepository
from views.chavespix_view import ChavesPixView
from utils import userfunctions
from utils.userfunctions import exibir_mensagem, limpar_tela, limpar_linha, exibir_conteudo, exibir_mensagem, posicionar_cursor, esperar_tecla
from models.conta import ContaDTO, ChavesPix
from models.tiposenum import TipoConta, TipoChavePix
from layouts.layouts import opcoes_disponiveis, operacoes_disponiveis

letra_para_tipo_chave = {
    "F" : TipoChavePix.CPF,
    "J" : TipoChavePix.CNPJ,
    "T" : TipoChavePix.TELEFONE,
    "E" : TipoChavePix.EMAIL,
    "A" : TipoChavePix.CHAVE_ALEATORIA
}

class ChavesPixController:
    _repo_conta = None
    _repo_chavepix = None
    _app = None
    _cancelar = False

    def __init__(self):
        self._repo_conta = ContasRepository(cliente_repository=ClientesRepository())
        self._repo_chavepix = ChavesPixRepository(self._repo_conta)
        self._app = ChavesPixView()

    def obter_conta(self):
        info = self._app.campos_chave_pix["id_conta"]
        exibir_conteudo("→", info["lin"], info["col"] - 2)
        while True:
            try:
                exibir_mensagem(info["mensagem"])
                id_conta = int(input())
                if id_conta == 0:
                    self._cancelar = True
                    break
                self._app._conta_dto, mensagem = self._repo_conta.get_by_id(id_conta)
                if not self._app._conta_dto:
                    exibir_mensagem(mensagem, wait_key=True)
                    continue
                break
            except ValueError as ex:
                exibir_mensagem(ex, wait_key=True)
        if self._app._conta_dto:
            self._app._lista_chavesPix, mensagem  = self._repo_chavepix.get_chaves_by_id_conta(id_conta)

    def setar_tipo_chave(tipo_chave: TipoChavePix, info: dict):
        match tipo_chave:
            case TipoChavePix.CPF:
                exibir_conteudo("•", info["lin"], info["cpf"])
            case TipoChavePix.CNPJ:
                exibir_conteudo("•", info["lin"], info["cnpj"])
            case TipoChavePix.TELEFONE:
                exibir_conteudo("•", info["lin"], info["telefone"])
            case TipoChavePix.EMAIL:
                exibir_conteudo("•", info["lin"], info["email"])
            case TipoChavePix.CHAVE_ALEATORIA:
                exibir_conteudo("•", info["lin"], info["chave_aleatoria"])

    def get_tipo_chave_pix(self):
        info = self._app.campos_chave_pix["tipo_chave"]
        while True:
            limpar_linha()
            exibir_mensagem("Escolha o tipo de chave que deseja cadastrar: [F], [J], [T], [E] ou [A]: ")
            opcao = esperar_tecla()
            if opcao not in ["F", "J", "T", "E", "A"]:
                exibir_mensagem("Opção inválida! Tente novamente!", wait_key=True)
                continue
            tipo_chave_pix = letra_para_tipo_chave[opcao]
            self.setar_tipo_chave(tipo_chave_pix, info)
            break
        return tipo_chave_pix

    def cadastrar_chave(self):
        tipo_chave = self.get_tipo_chave_pix()
        if self._cancelar:
            return
        
        

    def excluir_chave(self):
        pass

    def iniciar(self, conta: ContaDTO=None):
        self._app.iniciar()
        if not conta:
            self.obter_conta()
        else:
            self._app._conta_dto = conta
        if self._cancelar:
            return
        
        while True:
            opcao = self._app.exibir_dados_conta()
            if opcao == "R":
                break
            if opcao not in operacoes_disponiveis["gerencia_chavespix"]:
                exibir_mensagem("Opção inválida! Tente novamente!", wait_key=True)
                continue
            if opcao == "C":
                self.cadastrar_chave()
            elif opcao == "E":
                self.excluir_chave()
