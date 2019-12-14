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

l=[(1,'FUEL')]
residues=defaultdict(int)
ore_count=0
while l:
    p=l.pop()
    if p[1]=='ORE':
        ore_count+=p[0]
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

print(ore_count)  