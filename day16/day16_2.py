with open("input.txt","r") as f:
    phase_elems=[int(e) for e in f.readline().strip()]*10000
offset=int("".join(list(map(str,phase_elems[:7]))))
base_pattern=[0,1,0,-1]
n_phase=100
phase_elems=phase_elems[offset:]
for n in range(n_phase):
    print("phase: %d"%n)
    quedan=len(phase_elems)
    for out_elem in reversed(range(len(phase_elems)-1)):#-1 porque el ultimo elemento nunca cambia
        #print(sum(phase_elems[out_elem:])%10)
        phase_elems[out_elem]=(phase_elems[out_elem+1]+phase_elems[out_elem])%10
print("".join(list(map(str,phase_elems[:8]))))