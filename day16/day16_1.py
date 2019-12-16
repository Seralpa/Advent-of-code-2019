with open("input.txt","r") as f:
    phase_in=[int(e) for e in f.readline().strip()]
base_pattern=[0,1,0,-1]
n_phase=100
for _ in range(n_phase):
    phase_out=[]
    for out_elem in range(1,len(phase_in)+1):#va a empezar en 1 para evitar division por 0
        aux=[]
        for i in range(len(phase_in)):
            aux.append(phase_in[i]*base_pattern[((i+1)//out_elem)%4])
        phase_out.append(abs(sum(aux))%10)
    phase_in=phase_out
phase_out="".join(list(map(str,phase_out)))
print(phase_out[:8])