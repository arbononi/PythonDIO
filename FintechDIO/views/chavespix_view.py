from dataclasses import fields
from enum import Enum
from models.conta import Conta, ContaConsulta, ContaDTO
from models.tiposenum import TipoConta, StatusConta
from models.versao import Versao
from utils.userfunctions import exibir_mensagem, esperar_tecla, limpar_linha, limpar_tela, exibir_conteudo, desenhar_tela
from utils.userfunctions import formatar_data, formatar_cpf_cnpj, formatar_valor
from layouts.layouts import layout_gerencia_chavespix, opcoes_disponiveis, operacoes_disponiveis, titulo_telas

class ChavesPixView:
    _cancelar = False
    _conta_dto = None
    _lista_chavesPix = None

    campos_chave_pix = {
        "id_conta": { "lin": 4, "col": 14, "size": 10 },
        "cpf_cnpj": { "lin": 4, "col": 26, "size": 18 },
        "nome_cliente": { "lin": 4, "col": 46, "size": 52 },
        "tipo_chave" : { "lin": 5, "size": 1, "cpf": 19, "cnpj": 32, "telefone": 46, "email": 64, "chave_aleatoria": 79 },
        "chave_pix" : { "lin": 6, "col": 19, "size": 44, "mensagem": "Digite a chave ou FIM para sair" },
        "linha_dados": { "lin_ini": 11, "seq": 3, "size_seq": 3, "tipo_chave": 9, "size_tipo": 15, "chave_pix": 27, "size_chave": 72 }
    }

    def __init__(self):
        pass
    
    def limpar_lista_chaves(self):
        lin_ini = self.campos_chave_pix["linha_dados"]["lin_ini"]
        col_seq = self.campos_chaves_pix["linha_dados"]["seq"]
        size_seq = self.campos_chave_pix["linha_dados"]["size_seq"]
        col_tipo_chave = self.campos_chave_pix["linha_dados"]["tipo_chave"]
        size_tipo = self.campos_chave_pix["linha_dados"]["size_tipo"]
        col_chave_pix = self.campos_chave_pix["linha_dados"]["chave_pix"]
        size_chave = self.campos_chave_pix["linha_dados"]["size_chave"]

        for lin in range(lin_ini, 29):
            exibir_conteudo(" " * size_seq, lin, col_seq)
            exibir_conteudo(" " * size_tipo, lin, col_tipo_chave)
            exibir_conteudo(" " * size_chave, lin, col_chave_pix)
        
    def listar_chavespix(self):
        self.limpar_lista_chaves()
        lin = self.campos_chave_pix["linha_dados"]["lin_ini"]
        col_seq = self.campos_chaves_pix["linha_dados"]["seq"]
        size_seq = self.campos_chave_pix["linha_dados"]["size_seq"]
        col_tipo_chave = self.campos_chave_pix["linha_dados"]["tipo_chave"]
        col_chave_pix = self.campos_chave_pix["linha_dados"]["chave_pix"]
        size_chave = self.campos_chave_pix["linha_dados"]["size_chave"]
        seq = 0
        for chave_pix in self._lista_chavesPix:
            seq += 1
            exibir_conteudo(str(seq).rjust(size_seq, " "), lin, col_seq)
            exibir_conteudo(chave_pix.tipo_chave.descricao.upper(), lin, col_tipo_chave)
            exibir_conteudo(chave_pix.chave_pix.ljust(size_chave, " "), lin, col_chave_pix)
            lin += 1
        return esperar_tecla()

    def exibir_dados_conta(self):
        info_conta = self.campos_chave_pix["id_conta"]
        info_cpf_cnpj = self.campos_chave_pix["cpf_cnpj"]
        info_nome_cliente = self.campos_chave_pix["nome_cliente"]
        exibir_conteudo(str(self._conta_dto.conta.id).rjust(10, " "), info_conta["lin"], info_conta["col"])
        _, doc_formatado = formatar_cpf_cnpj(self._conta_dto.cpf_cnpj)
        exibir_conteudo(doc_formatado.rjust(18, " "), info_cpf_cnpj["lin"], info_cpf_cnpj["col"])
        exibir_conteudo(self._conta_dto.nome_cliente[:info_nome_cliente["size"]].ljust(info_nome_cliente["size"], " "), 
                        info_nome_cliente["lin"], info_nome_cliente["col"])
        if self._lista_chavesPix:
            return self.listar_chavespix()
        return esperar_tecla()
        
    def iniciar(self):
        limpar_tela()
        limpar_linha()
        desenhar_tela(layout_gerencia_chavespix, line_loop=11, stop_loop=28)
        exibir_conteudo(titulo_telas["gerencia_chavespix"], col=2)
        exibir_mensagem(opcoes_disponiveis["gerencia_chavespix"], col=2)
