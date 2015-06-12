i=0
nota=0
while True:
    try:
        a = int (raw_input("Digite a nota do Aluno "))
        while a > 0:
            i += 1
            nota = a + nota
            print "Nota total e: ", nota
            a = int (raw_input("Digite a nota do Aluno "))
        else:
            media = nota/i
            print " O valor da media e: ", media
    except:
        print "Nao foi um numero valido"

media = nota/i
print " O valor da media e: ", media
     
    

# Nota: 0.9
# Comentario: tome cuidado com as mensagens ao usuario. A Mensagem de total de
# nota confundiiu e nao dava pra saber que era para digitar as proximas notas
# enquanto eu nao li o codigo
