with open("input.txt","r") as f:
    inp=[int(e) for e in f.readline().strip()]
phase_in=[]
for _ in range(10000):
    phase_in.extend(inp)
base_pattern=[0,1,0,-1]
n_phase=100
for n in range(n_phase):
    print(n)
    phase_out=[]
    for out_elem in range(1,len(phase_in)+1):#va a empezar en 1 para evitar division por 0
        aux=[]
        if out_elem>len(phase_in)/2:
            phase_out.append(abs(sum(phase_in[out_elem-1:]))%10)
            continue
        for i in range(out_elem-1,len(phase_in)):
            aux.append(phase_in[i]*base_pattern[((i+1)//out_elem)%4])
        phase_out.append(abs(sum(aux))%10)
    phase_in=phase_out
phase_out="".join(list(map(str,phase_out)))
print("done")