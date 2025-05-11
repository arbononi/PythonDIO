import locale
from os import system as limp
from time import sleep
from database.banco import Banco
from models.versao import Versao
from layouts.layouts import titulo_telas, opcoes_disponiveis, layout_menu_principal, operacoes_disponiveis
from utils import userfunctions
from controllers.versao_controller import VersaoController
from controllers.clientes_controller import ClientesController
from controllers.contas_controller import ContasController
from controllers.transacoes_controller import TransacaoController
from controllers.consultas_controller import ConsultasController

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def main():

    def redesenhar_tela(star_lin=3, stop_lin=30):
        for config in layout_menu_principal:
            if config["lin"] >= star_lin and config["lin"] <= stop_lin:
                userfunctions.posicionar_cursor(config["lin"], config["col"])
                print(config["value"])
        titulo_menu = titulo_telas["menu_principal"].strip() + " - " + Versao.get_init_version().to_str()
        userfunctions.exibir_conteudo(titulo_menu.center(75, " "), lin=2, col=2)
    
    fl_ok = True
    if not Banco.check_exists_database():
        fl_ok, mensagem = Banco.create_database()

    if not fl_ok:
        print(mensagem)
        input()
        return
    
    banco = Banco.get_instance()
    banco.conectar()

    try:
        versaocontroller = VersaoController()
        clientescontroller = ClientesController()
        contascontroller = ContasController()
        transacoescontroller = TransacaoController()
        consultacontroller = ConsultasController()
        
        fl_ok, mensagem, versao_atual = versaocontroller.checar_versao_atual()
        if not fl_ok:
            print(mensagem)
            userfunctions.esperar_tecla()
            return
        
        limp("cls")
        data_atual_str = userfunctions.formatar_data(userfunctions.get_data_atual(), exibir_dia_semana=True, antes=True)
        userfunctions.posicionar_cursor(1, 1)
        userfunctions.desenhar_tela(layout_menu_principal)
        titulo_menu = titulo_telas["menu_principal"].strip() + " - " + versao_atual.to_str()
        userfunctions.exibir_conteudo(titulo_menu.center(75, " "), lin=2, col=2)
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
            except Exception as e:
                userfunctions.exibir_mensagem(f"Erro processar opção: {e}.", wait_key=True)
                continue
        userfunctions.exibir_mensagem("Obrigado por usar nossa Fintech! Finalizando ")
        col = 48
        for i in range(2, 0, -1):
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
