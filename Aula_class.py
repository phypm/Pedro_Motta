class Pessoa:
    nome = "Nome da pessoa"
    idade = 100
    profissao= "Eng"
    
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def set_profissao (self,profissao):
        self.profissao = profissao


class saladeaula():
    self.alunos =


class Aluno (Pessoa):

    def __init__(self,nome,idade):
        Pessoa.__init__(self,nome,idade)
        self.notas = []
        self.trab =[]

    def add_nota(self,titulo,valor):
        self.notas.append(valor)
        self.trab.append(titulo)

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
