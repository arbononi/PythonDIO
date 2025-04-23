from time import sleep
from os import system as limp

# class Animal:
#     def __init__(self, nro_patas):
#         self.nro_patas = nro_patas

#     def __str__(self):
#         return f"{self.__class__.__name__}: {", ".join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}"

# class Mamifero(Animal):
#     def __init__(self, cor_pelo, **kw):
#         super().__init__(**kw)
#         self.cor_pelo = cor_pelo 

# class Ave(Animal):
#     def __init__(self, cor_bico, **kw):
#         super().__init__(**kw)
#         self.cor_bico = cor_bico

# class Cachorro(Mamifero):
#     pass

# class Gato(Mamifero):
#     pass

# class Leao(Mamifero):
#     pass

# class Ornitorrinco(Mamifero, Ave):
#     def __init__(self, cor_pelo, cor_bico, nro_patas):
#        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)


# limp("cls")
# gato = Gato(nro_patas=4, cor_pelo="preto")
# ornitorrinco = Ornitorrinco(nro_patas=4, cor_pelo="cinza", cor_bico="laranja")

# print(gato)
# print()
# print(ornitorrinco)
# print()

limp("cls")

class Foo:
    def hello(self):
        print(self.__class__.__name__.lower)

class Bar(Foo):
    def hello(self):
        return super().hello()

bar = Bar()
bar.hello()            