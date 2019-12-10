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

asteroid_locations=[]
for i in range(len(asteroids)):
    for j in range(len(asteroids[i])):
        if asteroids[i][j]=='#':
            asteroid_locations.append((i,j))

view_count=[0 for _ in asteroid_locations]
for i,loc in enumerate(asteroid_locations):
    for ast in asteroid_locations:
        if loc==ast:
            continue
        if se_ven(loc,ast,asteroids):
            view_count[i]+=1
print(max(view_count))