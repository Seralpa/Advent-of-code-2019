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
            memory[args[0]]=int(input(">"))
    def output(args):
        if output_l==None:
            #print(args[0])
            print(str(chr(args[0])),end='')
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
        if instruction!=None:
            i=instruction
        else:
            i+=inc_dict[opcode]

with open("input.txt","r") as f:
    code=Infinite_memory(map(int,f.readline().split(",")))
code[0]=2
out=[]
mapa=[[]]
run_intcode(code)
# for c in out:
#     if c==10:
#         mapa.append([])
#     else:
#         mapa[-1].append(str(chr(c)))
# mapa.pop()
# mapa.pop()
# for i in range(len(mapa)):
#     for j in range(len(mapa[i])):
#         if i>0 and j>0 and i<len(mapa)-1 and j<len(mapa[i])-1 and mapa[i][j]=='#' and mapa[i-1][j]=='#' and mapa[i+1][j]=='#' and mapa[i][j-1]=='#' and mapa[i][j+1]=='#':
#             count+=i*j