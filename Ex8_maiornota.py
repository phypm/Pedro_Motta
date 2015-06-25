import sys
i=0
nota=0
boletim=[]
while True:
    try:
        a = int (raw_input("Digite a nota do Aluno "))
        while a >= 0:
            boletim.append(a)
            i += 1
            nota = a + nota
            print "Nota total e: ", nota
            a = int (raw_input("Digite a nota do Aluno "))
        else:
            media = nota/i
            maior=0
            j=0
            print "O boletim e: ",boletim
            for x in boletim:
                if x>j:
                    j=x
            print "A maior nota e :", j
            print
            print "O valor da media e: ", media
            break
    except:
        print "Nao foi um numero valido"


#Nota: 0.8
#Comentario: media eh um valor float e nao um inteiro. Para que serve a variavel "maior?"
     
