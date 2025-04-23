from time import sleep
from os import system as limp

class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
        print("Ligando motor...")

    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado = False):
        super().__init__(cor, placa, numero_rodas) 
        self.carregado = carregado

    def esta_carregado(self):
        if self.carregado:
            print("Sim, está carregado")
        else:
            print("Não, está vazio")
            
limp("cls")            
moto = Motocicleta("branca", "ABC-1234", 2)
carro = Carro("Prata", "AYQ4F068", 4)
caminhao = Caminhao("Cinza", "ABC4F90", 8)
                    

print(moto)
print(carro)
print(caminhao)
caminhao.esta_carregado()
print("Carregando o caminhão", end="")
for i in range(6):
    sleep(1)
    print(".", end="")
print()
caminhao.carregado = True
caminhao.esta_carregado()
print(caminhao)