"""class Pessoa:
    nome = "Nome da pessoa"
    idade = 100
    profissao= "Eng"

#double underscore
    
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def set_profissao (self,profissao):
        self.profissao = profissao

p=Pessoa("Pedro",24)

print p.nome
print p.idade
p.set_profissao("Engenheiro")
print p.profissao

class Engenheiro (Pessoa):
    profissao = "Engenheiro"
    salario = 0

    def set_salario (self, valor):
        self.salario = valor

p = Engenheiro ("Pedro",24)
print p.salario

p.set_salario (9000)
print p.salario

#-----------------------------------------------------------

class Aluno (Pessoa):

    def __init__(self,nome,idade):
        Pessoa.__init__(self,nome,idade)
        self.notas = []

    def add_nota(self,valor):
        self.notas.append(valor)

    def media(self):
        soma = 0
        for i in self.notas:
            soma = soma+i
        media = soma / len(self.notas)
        return media

    def status (self):
        if self.media() >=5.0:
            return True
        else:
            return False
"""

from Aula_class import Aluno


a= Aluno("Aluno1",18)
a.add_nota("T1",5.0)
a.add_nota("T2",6.0)
a.add_nota("T3",5.0)

b= Aluno("Aluno2",20)
b.add_nota("T1",8.0)
b.add_nota("T2",10.0)
b.add_nota("T3",7.0)

def mostrar_aluno (a):
    if a.status() == True:
        cond = "Aprovado"
    else:
        cond = "Reprovado"
    print "Media do aluno %s : %2.2f: %s " %(a.nome, a.media(),cond)
    for i in range(len(a.notas)):
        print a.trab[i], a.notas[i]

mostrar_aluno(a)
mostrar_aluno(b)












            
            







        
