r=(168630,718098)
count=0
for p in range(r[0],r[1]):
    password=str(p)
    ascendent=True
    consecutive=False
    for i in range(len(password)):
        if int(password[i])<int(password[i-1]) and i!=0:
            ascendent=False
            break
        if int(password[i])==int(password[i-1]) and i!=0:
            consecutive=True
    if ascendent and consecutive:
        count+=1
print(count)
    