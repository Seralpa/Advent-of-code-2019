def count_bugs(pos,mapa):
    count=0
    if pos[0]>0:
        count+=mapa[pos[0]-1][pos[1]]
    if pos[0]<len(mapa)-1:
        count+=mapa[pos[0]+1][pos[1]]
    if pos[1]>0:
        count+=mapa[pos[0]][pos[1]-1]
    if pos[1]<len(mapa[pos[0]])-1:
        count+=mapa[pos[0]][pos[1]+1]
    return count

def bio_rating(mapa):
    count=0
    value=1
    for l in mapa:
        for c in l:
            count+=c*value
            value*=2
    return count

with open("input.txt") as f:
    bug_map=[[1 if c=='#' else 0 for c in l.strip()] for l in f]
s=set()
while tuple(tuple(a) for a in bug_map) not in s:
    s.add(tuple(tuple(a) for a in bug_map))
    updates=[]
    for i in range(len(bug_map)):
        for j in range(len(bug_map[i])):
            bugs=count_bugs((i,j),bug_map)
            if bug_map[i][j] and bugs!=1:
                updates.append((i,j))
            elif not bug_map[i][j] and (bugs==1 or bugs==2):
                updates.append((i,j))
    for u in updates:
        bug_map[u[0]][u[1]]=int(not bug_map[u[0]][u[1]])
print(bio_rating(bug_map))