def run_intcode(memory,input_stream=None,output_l=None):
    def suma(args):
        memory[args[2]]=args[0]+args[1]
    def mult(args):
        memory[args[2]]=args[0]*args[1]
    def inpt(args):
        if input_stream:
            memory[args[0]]=input_stream.pop(0)
        else:
            memory[args[0]]=int(input("escribe un numero, puto:"))
    def output(args):
        if output:
            output_l.append(args[0])
        else:
            print(args[0])
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
    func_dict={1:suma,2:mult,3:inpt,4:output,5:j_if_t,6:j_if_f,7:less_than,8:equals}
    writes_to_mem=[1,2,3,7,8]#instructions that write to memory
    inc_dict={1:4,2:4,3:2,4:2,5:3,6:3,7:4,8:4}

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
        
        instruction=func_dict[opcode](params)
        if instruction:
            i=instruction
        else:
            i+=inc_dict[opcode]


import itertools
phase_states=list(itertools.permutations([0,1,2,3,4]))

with open("input1.txt","r") as f:
    code=list(map(int,f.readline().split(",")))

salidas=[]

for ps in phase_states:
    prev_output=[0]
    for i in ps:
        code_cpy=list(code)
        output=[]
        run_intcode(code_cpy,input_stream=[i,prev_output[0]],output_l=output)
        prev_output=output
    salidas.append((prev_output,ps))

print(max(salidas,key=lambda x:x[0]))