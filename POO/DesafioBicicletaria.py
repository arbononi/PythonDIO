class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro=18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro

    def buzinar(self):
        print("Biiiiiiiiiiiiii!!!")
    
    def parar(self):
        print("Parando bicicleta")
        print("Bicicleta parada")

    def correr(self):
        print("Vruuuuummmmm!!!!")

    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}"

print()
b1 = Bicicleta("Vermelha", "Caloi", 2025, 600.00)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)
print(b1)