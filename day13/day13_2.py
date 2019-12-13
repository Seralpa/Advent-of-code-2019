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
        if input_stream==None:
            memory[args[0]]=int(input(">"))
        else:
            memory[args[0]]=input_stream.pop(0)
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
            yield output_l
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

        if opcode==3 and len(input_stream)==0:
            yield output_l
            output_l=[]
        instruction=func_dict[opcode](params)
        if instruction:
            i=instruction
        else:
            i+=inc_dict[opcode]
    
with open("input1.txt","r") as f:
    code=Infinite_memory(map(int,f.readline().split(",")))
code[0]=2
out,inp=[],[]
for data in run_intcode(code,input_stream=inp,output_l=out):
    useful_data=[(data[i-2],data[i-1],data[i]) for i in range(2,len(data),3) if data[i]==3 or data[i]==4 or data[i-2]==-1]
    score_l=[d for d in useful_data if d[0]==-1]
    paddle_l=[d for d in useful_data if d[2]==3]
    ball_l=[d for d in useful_data if d[2]==4]
    if score_l:
        score=score_l[0][2]
    if paddle_l:
        paddle=paddle_l[0]
    if ball_l:
        ball=ball_l[0]
    if ball[0]>paddle[0]:
        inp.append(1)
    elif ball[0]<paddle[0]:
        inp.append(-1)
    else:
        inp.append(0)
print(score)