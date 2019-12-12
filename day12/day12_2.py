from operator import add
import re
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
                    
with open("input1.txt","r") as f:
    jupiter_moons_data=[l.strip() for l in f.readlines()]
jupiter_moons=[]
for d in jupiter_moons_data:
    moon_match=moon_data.match(d)
    jupiter_moons.append(Moon((int(moon_match.group(1)),int(moon_match.group(2)),int(moon_match.group(3)))))

found_period_x=False
found_period_y=False
found_period_z=False
period_x,period_y,period_z=0,0,0
i=0
while not found_period_x or not found_period_y or not found_period_z:
    x_state=[]
    y_state=[]
    z_state=[]
    for m in jupiter_moons:
        x_state.append((m.pos[0],m.vel[0]))
        y_state.append((m.pos[1],m.vel[1]))
        z_state.append((m.pos[2],m.vel[2]))
    x_state=tuple(x_state)
    y_state=tuple(y_state)
    z_state=tuple(z_state)
    if i==0:
        x_initial=x_state
        y_initial=y_state
        z_initial=z_state
    else:
        if not found_period_x:
            if x_state ==x_initial:
                found_period_x=True
                period_x=i
        if not found_period_y:
            if y_state ==y_initial:
                found_period_y=True
                period_y=i
        if not found_period_z:    
            if z_state ==z_initial:
                found_period_z=True
                period_z=i
        
    for m in jupiter_moons:
        m.update_vel(jupiter_moons)
    for m in jupiter_moons:
        m.move()
    i+=1

def lcm(x, y):
    a, b = x, y
    while a:
        a, b = b % a, a
    return x // b * y
#se asume que el estado que se repite es el inicial
print(lcm(period_x,lcm(period_y,period_z)))