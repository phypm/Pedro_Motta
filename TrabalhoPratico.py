import math

def distancia(x1,x2,y1,y2):
    dx = x2 -x1
    dy = y2 - y1 
    dx = dx ** 2
    dy = dy ** 2
    dist = math.sqrt(dx+dy)
    return dist
#------------------------------------------------

def listpto():
    print "Digite o numero de pontos que deseja trabalhar"
    i = int(raw_input())
    listax = []
    while  len(listax) < i:
        valorx = float(raw_input())
        listax.append(valorx)
    listay = []
    while  len(listay) < i:
        valory = float(raw_input())
        listay.append(valory)
    j=1
    tamanho=0
    while j < i:
        d = distancia(listax[j-1],listax[j],listay[j-1],listay[j])
        print "Comparando", d
        if tamanho < d:
            tamanho=d      
        else:
            tamanho=tamanho
        j=j+1      
    print "Amaior distancia e",tamanho

#---------------------------------------------------

def polar (x1,x2,y1,y2):
    d = distancia(x1,x2,y1,y2)
    dx = x2 -x1
    dy = y2 - y1
    angulo = math.atan2(dy,dx)
    angulo = math.degrees(angulo)
    print "A distancia e %d" % d
    print "O angulo e", angulo

#---------------------------------------------------
'''
print "Digite x1"
x1= float(raw_input())
print "Digite x2"
x2= float(raw_input())
print "Digite y1"
y1= float(raw_input())    
print "Digite y1"
y2= float(raw_input())
polar (x1,x2,y1,y2)
'''
#----------------------------------------------------

def retangulo (a,b,c):
    if (a**2 + b**2) == c**2:
        area =(a*b)/2
        print "A area e",area
    else:
        print "Não e um triangulo rec. Os valores sao", a, b ,c

#--------------------------------------------------
'''print "Digite os valores do traingulo"
a= int (raw_input())
b= int (raw_input())
c=int (raw_input())
retangulo (a,b,c)'''

#------------------------------------------------------

def gps (x,y,z):
    lan = math.atan2 (y,x)
    lan = math.degrees(lan)
    x = x**2
    y = y**2
    P = math.sqrt(x + y)
    N = 1
    h = 0
    i = 1
    a = 6378160
    E = 0.00669454185
    while i <= 5 :
        fi = math.atan ((z/P)*(1/(1-((E*N)/(N+h)))))
        seno = math.sin(fi)
        c = 1- ((seno**2) * E)
        b = math.sqrt(c)
        N = a/b
        cose = math.cos (fi)
        h = (P/cose)-N
        i=i+1
    fi = math.degrees(fi)
    h = h *1000
    print "Os valores sao", fi, lan, h

gps (4010210.546, -4260166.288, -2533008.133)
        
        
        
    











    
