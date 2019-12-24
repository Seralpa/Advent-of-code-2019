from copy import deepcopy
def count_bugs(pos,mapa):
    count=0
    if pos[1]==0:
        if pos[0]<len(mapa)-1:
            count+=mapa[pos[0]+1][1][2]
    elif (pos[1],pos[2])==(3,2) and pos[0]>0:
        count+=sum(mapa[pos[0]-1][-1])
    else:
        count+=mapa[pos[0]][pos[1]-1][pos[2]]

    if pos[1]==len(mapa[pos[0]])-1:
        if pos[0]<len(mapa)-1:
            count+=mapa[pos[0]+1][3][2]
    elif (pos[1],pos[2])==(1,2) and pos[0]>0:
        count+=sum(mapa[pos[0]-1][0])
    else:
        count+=mapa[pos[0]][pos[1]+1][pos[2]]

    if pos[2]==0:
        if pos[0]<len(mapa)-1:
            count+=mapa[pos[0]+1][2][1]
    elif (pos[1],pos[2])==(2,3) and pos[0]>0:
        count+=sum([l[-1] for l in mapa[pos[0]-1]])
    else:
        count+=mapa[pos[0]][pos[1]][pos[2]-1]
        
    if pos[2]==len(mapa[pos[0]][pos[1]])-1:
        if pos[0]<len(mapa)-1:
            count+=mapa[pos[0]+1][2][3]
    elif (pos[1],pos[2])==(2,1) and pos[0]>0:
        count+=sum([l[0] for l in mapa[pos[0]-1]])
    else:
        count+=mapa[pos[0]][pos[1]][pos[2]+1]

    return count

with open("input.txt") as f:
    bug_map=[[[1 if c=='#' else 0 for c in l.strip()] for l in f]]
clean_map=[[0 for _ in range(5)] for _ in range(5)]
niter=200
for _ in range(niter):
    bug_map.insert(0,deepcopy(clean_map))
    bug_map.append(deepcopy(clean_map))
    updates=[]
    for l in range(len(bug_map)):
        for i in range(len(bug_map[l])):
            for j in range(len(bug_map[l][i])):
                if (i,j)==(2,2):
                    continue
                bugs=count_bugs((l,i,j),bug_map)
                if bug_map[l][i][j] and bugs!=1:
                    updates.append((l,i,j))
                elif not bug_map[l][i][j] and (bugs==1 or bugs==2):
                    updates.append((l,i,j))
    for u in updates:
        bug_map[u[0]][u[1]][u[2]]=int(not bug_map[u[0]][u[1]][u[2]])
print(sum([sum([sum(l) for l in m]) for m in bug_map]))