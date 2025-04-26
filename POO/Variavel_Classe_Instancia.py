class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def exibir_alunos(*objs):
    for obj in objs:
        print(obj)

print()    
aluno_1 = Estudante("André", 1)
aluno_2 = Estudante("Rogerio", 2)

exibir_alunos(aluno_1, aluno_2)