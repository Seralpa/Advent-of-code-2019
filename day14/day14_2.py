import math
from collections import defaultdict
reactions=dict()
with open("input.txt","r") as f:
    for l in f:
        reactives,product=l.split(' => ')
        reactives=[r.split(' ') for r in reactives.split(', ')]
        reactives=list(map(lambda x:(int(x[0]),x[1]),reactives))
        reactives=(int(product.strip().split(' ')[0]),reactives)
        product=product.strip().split(' ')[1]
        reactions[product]=reactives

ore_resource=1000000000000
l=[(1,'FUEL')]
residues=defaultdict(int)
ore_count=0
fuel_count=0
out_of_ore=False
residues['ORE']=ore_resource
print("this may take a while...")
while True:
    l=[(1,'FUEL')]
    while l:
        p=l.pop()
        if p[1]=='ORE':
            residues[p[1]]-=p[0]
            if residues[p[1]]<0:
                out_of_ore=True
                break
            continue
        if residues[p[1]]>=p[0]:
            residues[p[1]]-=p[0]
            continue
        p=(p[0]-residues[p[1]],p[1])
        residues[p[1]]=0

        reaction=reactions[p[1]]
        n_of_reactions=math.ceil(p[0]/reaction[0])
        if p[0]%reaction[0]!=0:
            residues[p[1]]+=reaction[0]-(p[0]%reaction[0])
        for c in reaction[1]:
            l.append((c[0]*n_of_reactions,c[1]))
    if fuel_count%100000==0: #progres counter
        print(fuel_count)
    if not out_of_ore:
        fuel_count+=1
    else:
        break
print("done")
print(fuel_count)
