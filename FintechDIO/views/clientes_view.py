from datetime import date
from dataclasses import fields
from enum import Enum
from models.cliente import Cliente
from models.versao import Versao
from models.tiposenum import TipoPessoa, StatusCliente
from utils.userfunctions import validar_cpf_cnpj, formatar_cpf_cnpj, formatar_cep, formatar_data
from utils.userfunctions import exibir_mensagem, esperar_tecla, limpar_linha, limpar_tela, exibir_conteudo, desenhar_tela, posicionar_cursor
from utils import userfunctions
from layouts.layouts import layout_cadastro_clientes, layout_consulta_cliente, titulo_telas, layout_opcoes_consultas, opcoes_disponiveis, operacoes_disponiveis
from layouts.layouts import restaurar_linha_29
from utils.helper import ClienteInputvalidator

campos_cliente = {
    "id" : { "lin": 7, "col": 15, "size": 10, "mensagem": "Informe o código do cliente ou 0 (zero) para encerrar" },
    "tipo_pessoa": { "lin": 7, "fisica": 41, "juridica": 54, "size": 1, "mensagem" : "Selecione o tipo de pessoa pressionando a letra F ou J. S para cancelar" },
    "cpf_cnpj" : { "lin": 7, "col": 80, "size": 18, "mensagem" : "Informe o {doc} ou SAIR para cancelar" },
    "nome" : { "lin": 9, "col": 15, "size": 83, "mensagem" : "Digite no nome do cliente ou SAIR para cancelar" },
    "endereco" : { "lin": 11, "col": 15, "size": 83, "mensagem" : "Informe o endereço do cliente ou SAIR para cancelar" },
    "numero" : { "lin": 13, "col": 15, "size": 10, "mensagem" : "Informe o número do endereço ou SAIR para cancelar" },
    "complemento" : { "lin": 13, "col": 47, "size": 51, "mensagem" : "Informe o complemento, se houver, do endereço ou SAIR para cancelar" },
    "bairro" : { "lin" : 15, "col": 15, "size": 83, "mensagem" : "Informe o bairro ou SAIR para cancelar" },
    "cidade" : { "lin": 17, "col": 15, "size": 73, "mensagem" : "Informe o nome da Cidade ou SAIR para cancelar" },
    "uf" : { "lin": 17, "col": 96, "size": 2, "mensagem" : "Informe a sigla do Estado da cidade ou XX para cancelar" },
    "cep" : { "lin": 19, "col" : 15, "size": 10, "mensagem" : "Informe o CEP ou 99999999 para cancelar" },
    "telefone" : { "lin": 19, "col": 47, "size": 13, "mensagem" : "Informe o número do telefone ou SAIR para cancelar" },
    "data_nascimento" : { "lin": 19, "col": 88, "size": 10, "mensagem" : "Informe a data de nascimento ou SAIR para cancelar" },
    "status" : { "lin": 21, "ativo": 15, "restrito": 27, "bloqueado": 42, "inativo": 58, "size": 1, "mensagem" : "Selecione o Status do cliente ou S para cancelar" },
    "data_cadastro" : { "lin": 21, "col": 88, "size": 10 }
}

campos_consulta = {
    "nome" : 4,
    "cpf_cnpj" : 14,
    "cidade" : 27,
    "data_nascimento" : 38,
    "argumento": 71
}

letra_para_tipo_pessoa = {
    "F" : TipoPessoa.FISICA,
    "J" : TipoPessoa.JURIDICA
}

letra_para_status_cliente = {
    "A" : StatusCliente.ATIVO,
    "R" : StatusCliente.RESTRITO,
    "B" : StatusCliente.BLOQUEADO,
    "I" : StatusCliente.INATIVO
}

class ClientesView:
    _tipo_consulta = 1
    _cancelar = False
    _cliente = None

    def __init__(self):
        pass

    def limpar_opcoes(self):
        info = layout_opcoes_consultas["consulta_cliente"]
        for key, value in info.__dict__.items():
            if key == "lin":
                lin = value
                continue
            exibir_conteudo(" ", lin, value)

    def limpar_campos(self):
        for key, info in campos_cliente.items():
            if key == "tipo_pessoa":
                exibir_conteudo("_" * info["size"], info["lin"], info["fisica"])
                exibir_conteudo("_" * info["size"], info["lin"], info["juridica"])
            elif key == "status":
                exibir_conteudo("_" * info["size"],info["lin"], info["ativo"])
                exibir_conteudo("_" * info["size"],info["lin"], info["restrito"])
                exibir_conteudo("_" * info["size"],info["lin"], info["bloqueado"])
                exibir_conteudo("_" * info["size"],info["lin"], info["inativo"])
            else:
                exibir_conteudo("_" * info["size"],info["lin"], info["col"])

    def setar_status(self, status: StatusCliente):
        info = campos_cliente["status"]
        match status:
            case StatusCliente.ATIVO:
                exibir_conteudo(" ", info["lin"], info["restrito"])
                exibir_conteudo(" ", info["lin"], info["bloqueado"])
                exibir_conteudo(" ", info["lin"], info["inativo"])
            case StatusCliente.RESTRITO:
                exibir_conteudo(" ", info["lin"], info["ativo"])
                exibir_conteudo(" ", info["lin"], info["bloqueado"])
                exibir_conteudo(" ", info["lin"], info["inativo"])
            case StatusCliente.BLOQUEADO:
                exibir_conteudo(" ", info["lin"], info["ativo"])
                exibir_conteudo(" ", info["lin"], info["restrito"])
                exibir_conteudo(" ", info["lin"], info["inativo"])
            case StatusCliente.INATIVO:
                exibir_conteudo(" ", info["lin"], info["ativo"])
                exibir_conteudo(" ", info["lin"], info["restrito"])
                exibir_conteudo(" ", info["lin"], info["bloqueado"])

    def get_tipo_pessoa(self):
        tipo_pessoa = None
        info = campos_cliente["tipo_pessoa"]
        campo = "fisica"
        indicador = info["lin"] - 1
        while True:
            exibir_mensagem(info["mensagem"])
            exibir_conteudo("↓", indicador, info[campo])
            posicionar_cursor(info["lin"], info[campo])
            letra = esperar_tecla()
            if letra == "S":
                self._cancelar = True
                break
            if letra == "" and self._cliente is not None:
                tipo_pessoa = self._cliente.tipo_pessoa
            else:
                tipo_pessoa = letra_para_tipo_pessoa.get(letra)
            if tipo_pessoa is None:
                exibir_mensagem("Opção inválida! Digite apenas F, J ou S", wait_key=True)
                continue
            exibir_conteudo("•", info["lin"], info[tipo_pessoa.descricao])
            break
        if not self._cancelar:
            if tipo_pessoa == TipoPessoa.FISICA:
                exibir_conteudo(" ", info["lin"], info["juridica"])
            else:
                exibir_conteudo(" ", info["lin"], info["fisica"])
            exibir_conteudo(" ", indicador, info[campo])
            exibir_conteudo(" ", indicador, info[tipo_pessoa.descricao])
        return tipo_pessoa

    def get_cpf_cnpj(self, tipo_pessoa: TipoPessoa):
        info = campos_cliente["cpf_cnpj"]
        while True:
            mensagem =info["mensagem"]
            exibir_mensagem(mensagem.format(doc="CPF" if tipo_pessoa == TipoPessoa.FISICA else "CNPJ"))
            exibir_conteudo("↓", info["lin"] - 1, info["col"])
            posicionar_cursor(info["lin"], info["col"])
            cpf_cnpj = input().upper()
            if cpf_cnpj == "SAIR":
                self._cancelar = True
                doc_formatado=""
                break
            if cpf_cnpj == "" and self._cliente is not None:
                cpf_cnpj= self._cliente.cpf_cnpj
            fl_ok, mensagem = validar_cpf_cnpj(cpf_cnpj, tipo_pessoa)
            if not fl_ok:
                exibir_mensagem(mensagem, wait_key=True)
                continue
            fl_ok, doc_formatado = formatar_cpf_cnpj(cpf_cnpj)
            if not fl_ok:
                exibir_mensagem(doc_formatado, wait_key=True)
                continue
            break
        exibir_conteudo(" ", info["lin"] - 1, info["col"])
        exibir_conteudo(doc_formatado.rjust(18, " "), info["lin"], info["col"])
        return cpf_cnpj

    def get_nome(self):
        info = campos_cliente["nome"]
        while True:
            exibir_mensagem(info["mensagem"])
            exibir_conteudo("↓", info["lin"] - 1, info["col"])
            posicionar_cursor(info["lin"], info["col"])
            nome = input().title().strip()
            if nome.upper() == "SAIR":
                self._cancelar = True
                break
            if nome == "" and self._cliente is not None:
                nome = self._cliente.nome
            fl_ok, mensagem = ClienteInputvalidator.name_validation(nome)
            if not fl_ok:
                exibir_mensagem(mensagem, wait_key=True)
                continue
            break
        exibir_conteudo(" ", info["lin"] - 1, info["col"])
        exibir_conteudo(nome, info["lin"], info["col"])
        return nome

    def get_endereco(self):
        info = campos_cliente["endereco"]
        while True:
            exibir_mensagem(info["mensagem"])
            exibir_conteudo("↓", info["lin"] - 1, info["col"])
            posicionar_cursor(info["lin"], info["col"])
            endereco = input().title().strip()
            if endereco.upper() == "SAIR":
                self._cancelar = True
                break
            if endereco == "" and self._cliente is not None:
                endereco = self._cliente.endereco
            fl_ok, mensagem = ClienteInputvalidator.address_validation(endereco)
            if not fl_ok:
                exibir_mensagem(mensagem, wait_key=True)
                continue
            break
        exibir_conteudo(" ", info["lin"] - 1, info["col"])
        exibir_conteudo(endereco, info["lin"], info["col"])
        return endereco

    def get_number_address(self):
        info = campos_cliente["numero"]
        while True:
            exibir_mensagem(info["mensagem"])
            exibir_conteudo("↓", info["lin"] - 1, info["col"])
            posicionar_cursor(info["lin"], info["col"])
            numero = input().title().strip()
            if numero.upper() == "SAIR":
                self._cancelar = True
                break
            if numero == "" and self._cliente is not None:
                numero = self._cliente.numero
            fl_ok, mensagem = ClienteInputvalidator.number_validation(numero)
            if not fl_ok:
                exibir_mensagem(mensagem, wait_key=True)
                continue
            break
        exibir_conteudo(" ", info["lin"] - 1, info["col"])
        exibir_conteudo(numero, info["lin"], info["col"])
        return numero
    
    def get_complement_address(self):
        info = campos_cliente["complemento"]
        exibir_mensagem(info["mensagem"])
        exibir_conteudo("↓", info["lin"] - 1, info["col"])
        posicionar_cursor(info["lin"], info["col"])
        complemento = input().title().strip()
        if complemento.upper() == "SAIR":
            self._cancelar = True
        if complemento == "" and self._cliente is not None:
            complemento = self._cliente.complemento
        exibir_conteudo(complemento, info["lin"], info["col"])
        exibir_conteudo(" ", info["lin"] - 1, info["col"])
        return complemento

    def get_neighborhood_address(self):
        info = campos_cliente["bairro"]
        while True:
            exibir_mensagem(info["mensagem"])
            exibir_conteudo("↓", info["lin"] - 1, info["col"])
            posicionar_cursor(info["lin"], info["col"])
            bairro = input().title().strip()
            if bairro.upper() == "SAIR":
                self._cancelar = True
                break
            if bairro == "" and self._cliente is not None:
                bairro = self._cliente.bairro
            fl_ok, mensagem = ClienteInputvalidator.neighborhood_validation(bairro)
            if not fl_ok:
                exibir_mensagem(mensagem, wait_key=True)
                continue
            break
        exibir_conteudo(" ", info["lin"] - 1, info["col"])
        exibir_conteudo(bairro, info["lin"], info["col"])
        return bairro
    
    def get_city(self):
        info = campos_cliente["cidade"]
        while True:
            exibir_mensagem(info["mensagem"])
            exibir_conteudo("↓", info["lin"] - 1, info["col"])
            posicionar_cursor(info["lin"], info["col"])
            cidade = input().title().strip()
            if cidade.upper() == "SAIR":
                self._cancelar = True
                break
            if cidade == "" and self._cliente is not None:
                cidade = self._cliente.cidade
            fl_ok, mensagem = ClienteInputvalidator.city_validation(cidade)
            if not fl_ok:
                exibir_mensagem(mensagem, wait_key=True)
                continue
            break
        exibir_conteudo(" ", info["lin"] - 1, info["col"])
        exibir_conteudo(cidade, info["lin"], info["col"])
        return cidade

    def get_state(self):
        info = campos_cliente["uf"]
        while True:
            exibir_mensagem(info["mensagem"])
            exibir_conteudo("↓", info["lin"] - 1, info["col"])
            posicionar_cursor(info["lin"], info["col"])
            uf = input().upper().strip()
            if uf == "XX":
                self._cancelar = True
                break
            if uf == "" and self._cliente is not None:
                uf = self._cliente.uf
            fl_ok, mensagem = userfunctions.validar_estado(uf)
            if not fl_ok:
                exibir_mensagem(mensagem, wait_key=True)
                continue
            break
        exibir_conteudo(" ", info["lin"] - 1, info["col"])
        exibir_conteudo(uf, info["lin"], info["col"])
        return uf
    
    def get_cep(self):
        info = campos_cliente["cep"]
        while True:
            try:
                exibir_mensagem(info["mensagem"])
                exibir_conteudo("↓", info["lin"] - 1, info["col"])
                posicionar_cursor(info["lin"], info["col"])
                str_cep = input().strip()
                if str_cep == "99999999":
                    self._cancelar = True
                    break
                if str_cep == "" and self._cliente is not None:
                    str_cep = str(self._cliente.cep)
                fl_ok, num_cep, mensagem = userfunctions.validar_cep(str_cep)
                if not fl_ok:
                    exibir_mensagem(mensagem, wait_key=True)
                    continue
                break
            except ValueError as e:
                exibir_mensagem(f"Erro ao informar CEP: {e}", wait_key=True)
                continue
        exibir_conteudo(" ", info["lin"] - 1, info["col"])
        if not self._cancelar:
            cep_formatado = formatar_cep(num_cep)
            exibir_conteudo(cep_formatado, info["lin"], info["col"])
        return num_cep

    def get_phone(self):
        info = campos_cliente["telefone"]
        exibir_conteudo("↓", info["lin"] - 1, info["col"])
        exibir_mensagem(info["mensagem"])
        posicionar_cursor(info["lin"], info["col"])
        telefone = input().strip()
        if telefone.upper() == "SAIR":
            self._cancelar = True
        if telefone == "" and self._cliente is not None:
            telefone = self._cliente.telefone
        exibir_conteudo(" ", info["lin"] - 1, info["col"])
        return telefone
    
    def get_birthday(self):
        info = campos_cliente["data_nascimento"]
        while True:
            exibir_conteudo("↓", info["lin"] - 1, info["col"])
            exibir_mensagem(info["mensagem"])
            posicionar_cursor(info["lin"], info["col"])
            str_data_nascto = input().strip()
            if str_data_nascto.upper() == "SAIR":
                self._cancelar = True
                break
            if str_data_nascto == "" and self._cliente is not None:
                str_data_nascto = self._cliente.data_nascimento.strftime("%d/%m/%Y")
            fl_ok, data_nascto, mensagem = userfunctions.validar_data(str_data_nascto)
            if not fl_ok:
                exibir_mensagem(mensagem, wait_key=True)
                continue
            break
        exibir_conteudo(" ", info["lin"] - 1, info["col"])
        exibir_conteudo(userfunctions.formatar_data(data_nascto), info["lin"], info["col"])
        return data_nascto
    
    def get_status(self):
        info = campos_cliente["status"]
        campo = "ativo"
        status = None
        while True:
            exibir_mensagem(info["mensagem"])
            exibir_conteudo("↓", info["lin"] - 1, info[campo])
            posicionar_cursor(info["lin"], info[campo])
            letra = esperar_tecla()
            if letra == "S":
                self._cancelar = True
                break
            if letra == "" and self._cliente is not None:
                status = self._cliente.status
            else:
                status = letra_para_status_cliente.get(letra)
            if status is None:
                exibir_mensagem("Opção inválida! Tente novamente", wait_key=True)
                continue
            break
        exibir_conteudo(" ", info["lin"] - 1, info[campo])
        if not self._cancelar:
            exibir_conteudo("•", info["lin"], info[status.descricao])
            self.setar_status(status)
        return status

    def exibir_dados_cliente(self, cliente: Cliente, wait_key: bool=False):
        for campo in fields(cliente):
            info = campos_cliente[campo.name]
            tipo = campo.type
            valor = getattr(cliente, campo.name)
            if campo.type.__name__ == "date":
                valor_formatado = formatar_data(valor)
            elif campo.name == "cpf_cnpj":
                _, valor_formatado = formatar_cpf_cnpj(valor)
                if valor_formatado is not None:
                    valor_formatado = valor_formatado.rjust(18, " ")
            elif campo.name == "cep":
                valor_formatado = formatar_cep(valor)
            elif isinstance(valor, Enum):
                exibir_conteudo("•", info["lin"], info[valor.descricao])
                continue
            elif tipo.__name__ == "int":
                valor_formatado = str(valor).rjust(10, " ")
            else:
                valor_formatado = valor
            exibir_conteudo(" " * info["size"], info["lin"], info["col"])
            exibir_conteudo(valor_formatado, info["lin"], info["col"])
        if cliente.tipo_pessoa == TipoPessoa.FISICA:
            exibir_conteudo(" ", campos_cliente["tipo_pessoa"]["lin"], campos_cliente["tipo_pessoa"]["juridica"])
        else:
            exibir_conteudo(" ", campos_cliente["tipo_pessoa"]["lin"], campos_cliente["tipo_pessoa"]["fisica"])
        self.setar_status(cliente.status)
        if wait_key:
            exibir_mensagem("Pressione qualquer tecla para continuar", wait_key=wait_key)

    def get_cliente_id(self):
        limpar_linha(lin=28)        
        exibir_conteudo("Consultando cliente", lin=28)
        while True:
            try:
                self.limpar_campos()
                info = campos_cliente["id"]
                exibir_mensagem(info["mensagem"])
                exibir_conteudo("↓", info["lin"] - 1, info["col"])
                posicionar_cursor(info["lin"], info["col"])
                cliente_id = int(input())
                break
            except ValueError as error:
                exibir_conteudo(f"Código inválido para o cliente: {error}", lin=29)
                continue
            except Exception as error:
                exibir_conteudo(f"Erro ao processar operação: {error}", lin=29)
                break
        return cliente_id

    def obter_tipo_consulta(self):
        info = layout_opcoes_consultas["consulta_cliente"]
        fl_cancelar = False
        while True:
            exibir_mensagem("Selecione o tipo de pesquisa pressionanado N, F, C, D or R para cancelar a consulta")
            escolha = esperar_tecla()
            if escolha == "R":
                fl_cancelar = True
                break
            if escolha not in ["N", "F", "C", "D" ]:
                exibir_mensagem("Opção inválida! Tente novamente!", wait_key=True)
                continue
            match escolha:
                case "N":
                    self._tipo_consulta = 1
                    exibir_conteudo("•", info["lin"], info["nome"])
                case "F":
                    self._tipo_consulta = 2
                    exibir_conteudo("•", info["lin"], info["cpf_cnpj"])
                case "C":
                    self._tipo_consulta = 3
                    exibir_conteudo("•", info["lin"], info["cidade"])
                case "D":
                    self._tipo_consulta = 4
                    exibir_conteudo("•", info["lin"], info["data_nascimento"])
            break
        
        return fl_cancelar

    def digitar_argumento(self):
        match self._tipo_consulta:
            case 1:
                help = "Digite o nome ou parte do nome do cliente"
            case 2:
                help = "Digite o CPF ou CNPJ para consulta"
            case 3:
                help = "Digite o nome da cidade para consulta"
            case 4:
                help = "Digite a data de nascimento/fundação"
        help += "  ou FIM para cancelar"

        while True:
            exibir_mensagem(help)
            posicionar_cursor(4, 71)
            argumento = input().upper()
            if argumento == "FIM":
                fl_ok = False
                break
            fl_ok = True
            if self._tipo_consulta == 2:
                fl_ok, mensagem = userfunctions.validar_cpf_cnpj(argumento)
            elif self._tipo_consulta == 4:
                fl_ok, data_valida, mensagem = userfunctions.validar_data(argumento)
            if not fl_ok:
                exibir_mensagem(mensagem, wait_key=True)
                limpar_linha()
                continue
            break
        if fl_ok:
            if self._tipo_consulta == 2:
                _, doc_formatado = userfunctions.formatar_cpf_cnpj(argumento)
                exibir_conteudo(doc_formatado, 4, 71)
            elif self._tipo_consulta == 4:
                exibir_conteudo(userfunctions.formatar_data(data_valida), 4, 71)
                argumento = data_valida
            else:
                argumento = argumento.title()
        return fl_ok, argumento

    def processar_dados_tela(self):
        try:
            data_cadastro = date.today()
            info = campos_cliente["data_cadastro"]
            exibir_conteudo(formatar_data(data_cadastro), info["lin"], info["col"])
            cliente_temp = {}
            if self._cliente is not None:
                cliente_temp["id"] = self._cliente.id
            else:
                cliente_temp["id"] = 0
            cliente_temp["tipo_pessoa"] = self.get_tipo_pessoa()
            if self._cancelar:
                return
            cliente_temp["cpf_cnpj"] = self.get_cpf_cnpj(cliente_temp["tipo_pessoa"])
            if self._cancelar:
                return
            cliente_temp["nome"] = self.get_nome()
            if self._cancelar:
                return
            cliente_temp["endereco"] = self.get_endereco()
            if self._cancelar:
                return
            cliente_temp["numero"] = self.get_number_address()
            if self._cancelar:
                return
            cliente_temp["complemento"] = self.get_complement_address()
            if self._cancelar:
                return
            cliente_temp["bairro"] = self.get_neighborhood_address()
            if self._cancelar:
                return
            cliente_temp["cidade"] = self.get_city()
            if self._cancelar:
                return
            cliente_temp["uf"] = self.get_state()
            if self._cancelar:
                return
            cliente_temp["cep"] = self.get_cep()
            if self._cancelar:
                return
            cliente_temp["telefone"] = self.get_phone()
            if self._cancelar:
                return
            cliente_temp["data_nascimento"] = self.get_birthday()
            if self._cancelar:
                return
            cliente_temp["status"] = self.get_status()
            if self._cancelar:
                return
            cliente_temp["data_cadastro"] = data_cadastro

            while True:
                exibir_mensagem("Confirma os dados (S/N): ")
                confirmar = esperar_tecla(False)
                if confirmar not in [ "S", "N"]:
                    exibir_mensagem("Informe apenas S ou N!", wait_key=True)
                    continue
                break
            if confirmar == "N":
                return None
            cliente = Cliente(**cliente_temp)
            return cliente            
        except Exception as e:
            exibir_mensagem(f"Ocorreu um erro inesperado: {e}", wait_key=True)
            return None

    def incluir_cliente(self):
        self.limpar_campos()
        limpar_linha(lin=28)
        exibir_conteudo("Incluindo cliente", lin=28, col=3)
        return self.processar_dados_tela()
        
    def alterar_cliente(self, cliente: Cliente):
        limpar_linha(lin=28)
        exibir_conteudo("Alterando cliente", lin=28)
        self._cancelar = False
        self._cliente = cliente
        return self.processar_dados_tela()

    def excluir_cliente(self):
        limpar_linha(lin=28)
        exibir_conteudo("Excluindo cliente", lin=28)
        while True:
            exibir_mensagem("Confirma exclusão desse registro (S/N)? ")
            confirma_exclusao = esperar_tecla()
            if confirma_exclusao.upper() not in ["S", "N"]:
                exibir_mensagem("Opção inválida. Tente novamente!", wait_key=True)
                continue
            break
        return confirma_exclusao == "S"

    def exibir_lista_clientes(self, clientes: list[Cliente]):
        limpar_tela()
        desenhar_tela(layout_consulta_cliente, 8, 28)
        exibir_conteudo(titulo_telas["consulta_cliente"], 2, 2)
        # exibir_conteudo(opcoes_disponiveis["opcoes_consultas"], col=2)
        lin = 7
        for cliente in clientes:
            lin += 1
            _, doc_formatado = formatar_cpf_cnpj(cliente.cpf_cnpj)
            data_formatada = formatar_data(cliente.data_nascimento) if cliente.data_nascimento else " " * 10
            exibir_conteudo(doc_formatado, lin, 3)
            exibir_conteudo(cliente.nome[:34].ljust(34, " "), lin, 24)
            exibir_conteudo(cliente.telefone.ljust(13, " "), lin, 61)
            exibir_conteudo(data_formatada, lin, 77)
            exibir_conteudo(cliente.status.name, lin, 90)

        while True:
            exibir_conteudo(opcoes_disponiveis["opcoes_consultas"], col=2)
            opcao = esperar_tecla()
            if opcao == "R":
                exibir_conteudo(restaurar_linha_29, lin=29, col=1)
                break
            if opcao not in operacoes_disponiveis["opcoes_consultas"]:
                exibir_mensagem("Opção inválida! Tente novamente!", wait_key=True)
                continue
            break
        return opcao

    def nova_consulta(self):
        fl_cancelar = self.obter_tipo_consulta()
        if fl_cancelar:
            return
        fl_ok, argumento = self.digitar_argumento()
        if not fl_ok:
            return None, None
        return self._tipo_consulta, argumento

    def mostar_erro(self, err: str):
        exibir_mensagem(err, wait_key=True)

    def iniciar(self):
        limpar_tela()
        desenhar_tela(layout_cadastro_clientes)
        titulo_tela = titulo_telas["menu_principal"].replace(" - MENU PRINCIPAL", "").strip() + " - " + Versao.get_init_version().to_str()
        exibir_conteudo(titulo_tela.center(75, " "), 2, 2)
        exibir_conteudo(titulo_telas["cadastro_clientes"], lin=4, col=2)
        self.limpar_campos()

        while True:
            limpar_linha()
            exibir_conteudo(opcoes_disponiveis["opcoes_cadastro"], lin=30, col=2)
            opcao = esperar_tecla()
            if opcao not in operacoes_disponiveis["operacoes_cadastro"]:
                exibir_mensagem("Opção inválida! Pressione qualquer tecla para continuar.", col=2, wait_key=True)
                continue
            break
        return opcao
