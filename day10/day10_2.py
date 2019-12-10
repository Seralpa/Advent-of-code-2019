from operator import sub
from operator import add
from fractions import Fraction
def se_ven(p1,p2,asteroids):
    dif=tuple(map(sub,p2,p1))
    if dif[1]==0:
        #tratar este caso especial
        d=(abs(dif[0])//dif[0],0)
    elif dif[0]==0:
        #otro caso especial...
        d=(0,abs(dif[1])//dif[1])
    else:
        direction=Fraction(dif[0],dif[1])#ojo con los signos
        d=(abs(direction.numerator),abs(direction.denominator))
        d=(d[0]*abs(dif[0])//dif[0],d[1]*abs(dif[1])//dif[1])
    while True:
        p1=tuple(map(add,p1,d))
        if p1==p2:
            return True
        elif asteroids[p1[0]][p1[1]]=="#":
            return False

with open("input1.txt","r") as f:
    asteroids=[list(l.strip()) for l in f.readlines()]

asteroid_locations=dict()
for i in range(len(asteroids)):
    for j in range(len(asteroids[i])):
        if asteroids[i][j]=='#':
            asteroid_locations[(i,j)]=[]

view_count=[0 for _ in asteroid_locations]
for loc in asteroid_locations.keys():
    for ast in asteroid_locations.keys():
        if loc==ast:
            continue
        if se_ven(loc,ast,asteroids):
            asteroid_locations[loc].append(ast)
laser=max(asteroid_locations.items(),key=lambda x:len(x[1]))[0]
print(len(asteroid_locations[laser]))
#solo funciona si se carga mas de 200 en la primera vuelta
#sino hay que eliminar todos los del diccionari y calcular de nuevo la parte anterior
j_mayor_0=[]#a la derecha de laser
j_menor_0=[]#a la izq de laser
en_vertical_arriba=[]
en_vertical_abajo=[]
for ast in asteroid_locations[laser]:
    if ast[1]>laser[1]:
        j_mayor_0.append(ast)
    elif ast[1]<laser[1]:
        j_menor_0.append(ast)
    else:
        if ast[0]>laser[0]:
            en_vertical_arriba.append(ast)
        else:
            en_vertical_abajo.append(ast)
j_mayor_0.sort(key=lambda x:(x[0]-laser[0])/(x[1]-laser[1]))
j_menor_0.sort(key=lambda x:(x[0]-laser[0])/(x[1]-laser[1]))
ordered_asteroids=en_vertical_arriba+j_mayor_0+en_vertical_abajo+j_menor_0
print(ordered_asteroids[199][0]+ordered_asteroids[199][1]*100)