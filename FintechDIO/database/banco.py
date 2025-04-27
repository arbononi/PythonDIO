import sqlite3
import logging
import os

CAMINHO_BANCO = os.path.join(os.path.dirname(__file__), "dados", "fintechDIO.db")

logging.basicConfig(
    filename="fintech.log",
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
class Banco:
    _instance = None # atributo de classe para guardar instancia única

    def __init__(self):
        if Banco._instance is not None:
            raise Exception("Esta classe é um Singleton! Use get_instance() para acessar!")
        self.caminho_banco = CAMINHO_BANCO
        self.conn = None
        Banco._instance = self

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Banco()
        return cls._instance
    
    def create_database():
        try:
            banco = Banco()
            fl_ok, mensagem = banco.conectar()
            if not fl_ok:
                return fl_ok, mensagem
            banco.fechar()
            return fl_ok, logging.info("Banco de dados criado com sucesso!")
        except sqlite3.Error as e:
            logging.error(f"Erro ao criar banco de dados: {e}")
            return logging.error
        
    def conectar(self):
        try:
            if self.conn is None:
                self.conn = sqlite3.connect(CAMINHO_BANCO)
                self.cursor = self.conn.cursor()
                self.mensagens = []
                logging.info("Conexão com banco iniciada.")
            return True, None
        except sqlite3.Error as e:
            logging.error(f"Erro ao conectar ao banco de dados: {e}")
            return False, logging.error

    def executar(self, query, params=()):
        if not self.conn:
            return False, logging.error("Tentativa de executar operação sem conexão com o banco")
        try:
            if self.cursor is None:
                self.cursor = self.conn.cursor()
                
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
            if params:
                logging.info(f"Executou query: {query} | Params: {params}")
            else:
                logging.info(f"Executou query: {query}")
            return self.cursor, None
        except sqlite3.IntegrityError as e:
            logging.error(f"Erro de integridade (IntegrityError) - Query: {query} : {e}")
            return None, logging.error
        except sqlite3.OperationalError as e:
            logging.error(f"Comando SQL inválido (OperationalError) - Query: {query} : {e}")
            return None, logging.error
        except sqlite3.DatabaseError as e:
            logging.error(f"Erro ao processar comando (DatabaseError) - Query: {query} : {e}")
            return None, logging.error
        except Exception as e:
            logging.exception(f"Exceção gerada (Exception) - Query: {query} : {e}")
            return None, logging.exception

    def fechar(self):
        if self.conn:
            self.conn.close()
            self.conn = None
        return True, logging.info("Conexão com banco de dados encerrada!")

    def check_exists_database():
        return os.path.exists(CAMINHO_BANCO)
    
    
    
    



