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

for _ in range(1000):
    for m in jupiter_moons:
        m.update_vel(jupiter_moons)
    for m in jupiter_moons:
        m.move()

print(sum([m.get_energy() for m in jupiter_moons]))