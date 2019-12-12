from operator import add
import re
import numpy as np
moon_data=re.compile(r"<x=(-?\d+), y=(-?\d+), z=(-?\d+)>")
class Moon:
    def __init__(self, pos):
        self.pos=pos
        self.vel=(0,0,0)
    def move(self):
        self.pos=tuple(map(add,self.pos,self.vel))
    def update_vel(self,moons):
        for m in moons:
            dv=[0,0,0]
            for i in range(3):
                if self.pos[i]>m.pos[i]:
                    dv[i]=-1
                elif self.pos[i]<m.pos[i]:
                    dv[i]=1
            self.vel=tuple(map(add,self.vel,dv))
    def get_kinetic(self):
        return sum(map(abs,self.vel))
    def get_potential(self):
        return sum(map(abs,self.pos))
    def get_energy(self):
        return self.get_kinetic()*self.get_potential()
    def __str__(self):
        return str(self.pos)+str(self.vel)
                    
with open("test.txt","r") as f:
    jupiter_moons_data=[l.strip() for l in f.readlines()]
jupiter_moons=[]
for d in jupiter_moons_data:
    moon_match=moon_data.match(d)
    jupiter_moons.append(Moon((int(moon_match.group(1)),int(moon_match.group(2)),int(moon_match.group(3)))))
x_history=[]
y_history=[]
z_history=[]
found_period_x=False
found_period_y=False
found_period_z=False
period_x,period_y,period_z=0,0,0
i=0
while not found_period_x or not found_period_y or not found_period_z:
    x_state=set()
    y_state=set()
    z_state=set()
    for m in jupiter_moons:
        x_state.add((m.pos[0],m.vel[0]))
        y_state.add((m.pos[1],m.vel[1]))
        z_state.add((m.pos[2],m.vel[2]))
    x_state=tuple(x_state)
    y_state=tuple(y_state)
    z_state=tuple(z_state)
    if not found_period_x:
        if x_state in x_history:
            print("hola_x")
            found_period_x=True
            period_x=i
            #encontrado periodo de x
        else:
            x_history.append(x_state)
            #meter el estado de x en history
    if not found_period_y:
        if y_state in y_history:
            print("hola_y")
            found_period_y=True
            period_y=i
        else:
            y_history.append(y_state)
    if not found_period_z:    
        if z_state in z_history:
            print("hola_z")
            found_period_z=True
            period_z=i
        else:
            z_history.append(z_state)
        
    for m in jupiter_moons:
        m.update_vel(jupiter_moons)
    for m in jupiter_moons:
        m.move()
    i+=1
print(period_x)
print(period_y)
print(period_z)
print(np.lcm.reduce([period_x,period_y,period_z]))