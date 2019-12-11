class Infinite_memory(list):
    def __init__(self,*args):
        list.__init__(self,*args)
    def __getitem__(self, index):
        if index>=len(self):
            for _ in range((index-len(self))+1):
                self.append(0)
        return super().__getitem__(index)
    def __setitem__(self, key, value):
        if key>=len(self):
            for _ in range((key-len(self))+1):
                self.append(0)
        return super().__setitem__(key, value)

def run_intcode(memory,input_stream=None,output_l=None):
    global relative_base
    relative_base=0
    def suma(args):
        memory[args[2]]=args[0]+args[1]
    def mult(args):
        memory[args[2]]=args[0]*args[1]
    def inpt(args):
        if input_stream:
            memory[args[0]]=input_stream.pop(0)
        else:
            memory[args[0]]=int(input("escribe un numero, puto (1 para parte 1 2 para parte 2):"))
    def output(args):
        if output_l==None:
            print(args[0])
        else:
            output_l.append(args[0])
    def j_if_t(args):
        if args[0]!=0:
            return args[1]
    def j_if_f(args):
        if args[0]==0:
            return args[1]
    def less_than(args):
        memory[args[2]]=int(args[0]<args[1])
    def equals(args):
        memory[args[2]]=int(args[0]==args[1])
    def inc_rel_base(args):
        global relative_base
        relative_base+=args[0]
    func_dict={1:suma,2:mult,3:inpt,4:output,5:j_if_t,6:j_if_f,7:less_than,8:equals,9:inc_rel_base}
    writes_to_mem=[1,2,3,7,8]#instructions that write to memory
    inc_dict={1:4,2:4,3:2,4:2,5:3,6:3,7:4,8:4,9:2}
    i=0
    while True:
        opcode=str(memory[i])
        param_bits=list(opcode[:-2])
        opcode=int(opcode[-2:])
        if opcode==99:
            break
        params=[]
        for p in range(1,inc_dict[opcode]):
            bit=0
            if len(param_bits)>0:
                bit=int(param_bits.pop())

            if bit==2:
                if (p==inc_dict[opcode]-1 and opcode in writes_to_mem):             #write relative
                    params.append(relative_base+memory[i+p])
                else:                                                               #read relative
                    params.append(memory[relative_base+memory[i+p]])
            elif (p==inc_dict[opcode]-1 and opcode in writes_to_mem) or (bit==1):   #read immediate or write positional
                params.append(memory[i+p])
            
            else:                                                                   #default read positional
                params.append(memory[memory[i+p]])
        
        instruction=func_dict[opcode](params)
        if instruction:
            i=instruction
        else:
            i+=inc_dict[opcode]
        if len(output_l)>0:
            yield output_l.pop()
from operator import add
from collections import defaultdict
class Hull_robot:
    def __init__(self):
        self.direction=(-1,0)
        self.pos=(0,0)
        self.mapa=defaultdict(int)
        self.mapa[(0,0)]=1  #starting position white
    def move(self):
        self.pos=tuple(map(add,self.pos,self.direction))
    def turn(self,lado):
        if abs(self.direction[1])==lado:
            self.direction=(self.direction[1],self.direction[0])
        else:
            self.direction=(-self.direction[1],-self.direction[0])
    def paint(self,color):
        self.mapa[self.pos]=color
    def get_color(self):
        return self.mapa[self.pos]

with open("input1.txt","r") as f:
    code=Infinite_memory(map(int,f.readline().split(",")))

_exhausted = object()
entrada,salida=[],[]
g=run_intcode(code,input_stream=entrada,output_l=salida)
robot=Hull_robot()
while True:
    entrada.append(robot.get_color())
    color=next(g,_exhausted)
    if color==_exhausted:
        break
    robot.paint(color)
    lado=next(g)
    robot.turn(lado)
    robot.move()
matrix=[]
for i in range(min(robot.mapa.keys(),key=lambda x: x[0])[0],max(robot.mapa.keys(),key=lambda x: x[0])[0]+1):
    matrix.append([])
    for j in range(min(robot.mapa.keys(),key=lambda x: x[1])[1],max(robot.mapa.keys(),key=lambda x: x[1])[1]+1):
        if robot.mapa[(i,j)]==1:
            matrix[i].append('#')
        else:
            matrix[i].append(' ')
for l in matrix:
    print()
    for p in l:
        print(p,end='')