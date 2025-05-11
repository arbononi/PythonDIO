from dataclasses import dataclass

@dataclass
class Versao:
    versao: int
    release: int
    build: int
    compile: int

    def to_str(self):
        return f"Versão: {self.versao}.{self.release}.{self.build}.{self.compile}"
    
    def as_tuple(self):
        return (
            self.versao,
            self.release,
            self.build,
            self.compile
        )
    
    @staticmethod
    def get_init_version():
        return Versao(
            versao= 1,
            release= 2025,
            build= 5,
            compile=0
        )
