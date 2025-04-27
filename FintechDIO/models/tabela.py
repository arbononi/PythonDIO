from abc import ABC, abstractmethod
from database.banco import Banco

class Tabela(ABC):
    def __init__(self, banco: Banco):
        self.banco = banco
        
    @classmethod
    @abstractmethod
    def create_table(cls):
        pass

    @classmethod
    @abstractmethod
    def insert(cls):
        pass

    @classmethod
    @abstractmethod
    def update(cls):
        pass
    
    @classmethod
    @abstractmethod
    def delete(cls):
        pass
