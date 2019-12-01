with open("input1.txt","r") as f:
    l=[(int(line)//3)-2 for line in f.readlines()]
print(sum(l))
