with open("input1.txt","r") as f:
    memory=list(map(int,f.readline().split(",")))

def suma(args):
    memory[args[2]]=args[0]+args[1]
def mult(args):
    memory[args[2]]=args[0]*args[1]
def inpt(args):
    memory[args[0]]=int(input("escribe un numero, puto:"))
def output(args):
    print(args[0])
func_dict={1:suma,2:mult,3:inpt,4:output}
writes_to_mem=[1,2,3]#instructions that write to memory
inc_dict={1:4,2:4,3:2,4:2}

i=0
while True:
    opcode=str(memory[i])
    param_bits=list(opcode[:-2])
    opcode=int(opcode[-2:])
    if opcode==99:
        break
    params=[]
    for p in range(1,inc_dict[opcode]):
        if (p==inc_dict[opcode]-1 and opcode in writes_to_mem) or (len(param_bits)>0 and int(param_bits.pop())==1):
            params.append(memory[i+p])
        else:
            params.append(memory[memory[i+p]])
     
    func_dict[opcode](params)
    i+=inc_dict[opcode]