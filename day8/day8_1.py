with open("input1.txt","r") as f:
    lst=list(map(int,f.readline().strip()))
n=6*25  #size of layer
layers=[lst[i:i + n] for i in range(0, len(lst), n)]
l=min(layers,key=lambda x:x.count(0))
print(l.count(1)*l.count(2))