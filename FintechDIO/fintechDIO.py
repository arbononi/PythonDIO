import locale
from os import system as limp
from time import sleep
from database.banco import Banco
from database.migracao import create_tables
from models.versao import Versao
from layouts.layouts import titulo_telas, opcoes_disponiveis, layout_menu_principal, operacoes_disponiveis
from utils import userfunctions
from controllers.clientes_controller import ClientesController
from controllers.contas_controller import ContasController
from controllers.transacoes_controller import TransacoesController
from controllers.consultas_controller import ConsultasController

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def main():

    def redesenhar_tela(star_lin=3, stop_lin=30):
        for config in layout_menu_principal:
            if config["lin"] >= star_lin and config["lin"] <= stop_lin:
                userfunctions.posicionar_cursor(config["lin"], config["col"])
                print(config["value"])
    
    fl_ok = True
    fl_create_tables = False
    if not Banco.check_exists_database():
        fl_ok, mensagem = Banco.create_database()
        fl_create_tables = True

    if not fl_ok:
        print(mensagem)
        input()
        return
    
    banco = Banco.get_instance()
    banco.conectar()

    try:
        if fl_create_tables:
            create_tables(banco)
        
        versao = Versao.get_by_id(banco, Versao._versao)
        if versao:
            if versao.versao != Versao._versao or versao.release != Versao._release or versao.build != Versao._build:
                # TODO Criar verificação de diferenças entre as versões
                return
            elif versao.compile != Versao._compile:
                versao.compile = Versao._compile
                versao.banco.mensagens = []
                versao.update()
                if len(versao.banco.mensagens) > 0:
                    print(versao.banco.mensagens[0])
        else:
            versao = Versao(banco, versao=Versao._versao, release=Versao._release, build=Versao._build, compile=Versao._compile)
            versao.insert()

        clientescontroller = ClientesController(banco)
        contascontroller = ContasController(banco)
        transacoescontroller = TransacoesController(banco)
        consultacontroller = ConsultasController(banco)

        limp("cls")
        data_atual_str = userfunctions.formatar_data(userfunctions.get_data_atual(), exibir_dia_semana=True, antes=True)
        userfunctions.posicionar_cursor(1, 1)
        userfunctions.desenhar_tela(layout_menu_principal)
        userfunctions.exibir_conteudo(titulo_telas["menu_principal"], lin=2, col=2)
        userfunctions.exibir_conteudo(data_atual_str, lin=2, col=85)

        while True:
            try:
                userfunctions.exibir_conteudo(opcoes_disponiveis["menu_principal"], lin=30, col=2)
                opcao = int(userfunctions.esperar_tecla())
                fl_redesenhar_tela = False
                if opcao == 9:
                    break
                if opcao not in operacoes_disponiveis["menu_principal"]:
                    userfunctions.exibir_mensagem("Opção inválida! Tente novamente.", wait_key=True)
                    continue
                if opcao == 1:
                   clientescontroller.iniciar()
                   fl_redesenhar_tela = True
                elif opcao == 2:
                    contascontroller.iniciar()
                    fl_redesenhar_tela = True
                elif opcao == 3:
                    transacoescontroller.iniciar()
                    fl_redesenhar_tela = True
                else:
                    consultacontroller.iniciar()
                    fl_redesenhar_tela = True

                if fl_redesenhar_tela:
                    redesenhar_tela()
            except ValueError:
                userfunctions.exibir_mensagem("Opção inválida! Tente novamente.", wait_key=True)
                continue
        userfunctions.exibir_mensagem("Obrigado por usar nossa Fintech! Finalizando ")
        col = 48
        for i in range(3, 0, -1):
            userfunctions.exibir_conteudo(".", lin=30, col=col)
            col += 1
            sleep(1)
    except Exception as e:
        print(f"Erro: {e}")

    finally:
        if banco.conn:
            banco.fechar()
        limp("cls")

if __name__ == "__main__":
    main()
