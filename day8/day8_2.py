with open("input1.txt","r") as f:
    lst=list(map(int,f.readline().strip()))
n=6*25  #size of layer
layers=[lst[i:i + n] for i in range(0, len(lst), n)]
decoded=[2 for _ in range(n)]   #start with a transparent image
for l in layers:
    for i in range(n):
        if l[i]!=2 and decoded[i]==2:
            decoded[i]=l[i]
for i in range(6):
    print()
    for j in range(25):
        if decoded[i*25+j]==0:
            print(" ",end='')
        else:
            print("#",end='')