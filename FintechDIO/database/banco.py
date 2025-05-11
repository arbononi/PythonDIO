import sqlite3, os, logging

CAMINHO_BANCO = os.path.join(os.path.dirname(__file__), "dados", "fintechDIO.db")

logging.basicConfig(filename="fintech.log", level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s')

class Banco:
    _instance = None

    def __init__(self):
        if Banco._instance:
            raise Exception("Use Banco.get_instance()")
        self.conn = None
        Banco._instance = self

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = Banco()
        return cls._instance

    @classmethod
    def check_exists_database(cls) -> bool:
        return os.path.exists(CAMINHO_BANCO)
    
    @classmethod
    def create_database(cls):
        """
        Cria o arquivo do banco (se não existir), conecta, 
        e chama create_table() de cada repositório.
        """
        # Assegura diretório
        pasta = os.path.dirname(CAMINHO_BANCO)
        os.makedirs(pasta, exist_ok=True)

        # Instancia e conecta
        banco = cls.get_instance()
        ok, msg = banco.conectar()
        if not ok:
            return ok, msg

        # Cria tabelas via repositórios
        from database.clientes_repository import ClienteRepository
        repo_cliente = ClienteRepository()
        cursor, msg_tab = repo_cliente.create_table()
        if cursor is None:
            return False, msg_tab

        logging.info("Banco de dados e tabelas criados com sucesso.")
        banco.fechar()
        return True, None
    
    def conectar(self):
        if not self.conn:
            self.conn = sqlite3.connect(CAMINHO_BANCO)
            self.conn.row_factory = sqlite3.Row
        return True, None

    def executar(self, sql, params=()):
        try:
            cur = self.conn.execute(sql, params)
            self.conn.commit()
            logging.info(f"Comando executado com sucesso: {sql}, {params}")
            return cur, None
        except Exception as e:
            logging.error(f"{e} — SQL: {sql} | {params}")
            return None, str(e)

    def fechar(self):
        if self.conn:
            self.conn.close()
            self.conn = None
        return True, None
