from operator import sub
from fractions import Fraction
def se_ven(p1,p2,asteroids):
    dif=map(sub,p1,p2)
    if dif[1]==0:
        #tratar este caso especial
        pass
    direction=Fraction(dif[0],dif[1])#ojo con los signos
    
    


with open("test.txt","r") as f:
    asteroids=[list(l.strip()) for l in f.readlines()]

asteroid_locations=[]
for i in range(len(asteroids)):
    for j in range(len(asteroids[i])):
        if asteroids[i][j]=='#':
            asteroid_locations.append((i,j))

for loc in asteroid_locations:
    for ast in asteroid_locations:
        if loc==ast:
            continue
        pass