target=19690720
for noun in range(99):
    for verb in range(99):
        with open("input1.txt","r") as f:
            code=list(map(int,f.readline().split(",")))
        code[1]=noun
        code[2]=verb
        for i in range(0,len(code),4):
            if code[i]==99:
                break
            elif code[i]==1:
                code[code[i+3]]=code[code[i+1]]+code[code[i+2]]
            elif code[i]==2:
                code[code[i+3]]=code[code[i+1]]*code[code[i+2]]
            else:
                print("error code %d on position %d" %(code[i],i))
                break
        if code[0]==target:
            print("resultado: %d" %(100 * noun + verb))