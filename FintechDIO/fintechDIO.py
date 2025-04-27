from database.banco import Banco
from database.migracao import create_tables
from models.versao import Versao

# from controllers.cliente_controller import ClienteController

def main():
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
            
    except Exception as e:
        print(f"Erro: {e}")

    finally:
        if banco.conn:
            banco.fechar()

if __name__ == "__main__":
    main()
