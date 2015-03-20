

print "Digite a nota do Aluno"
a = int (raw_input())
i=0
b=0
nota=0
while a >= 0:
    b = a
    i = 1 + i
    nota = b + nota
    print "Nota total eh", nota
    a = int (raw_input())
else:
    media = nota/i
    print " O valor da media eh", media     
    
