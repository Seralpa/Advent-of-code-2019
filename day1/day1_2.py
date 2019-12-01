def calculate_fuel(mass):
    return (mass//3)-2

with open("input1.txt","r") as f:
    masses=[int(line) for line in f.readlines()]

total=0
while(len(masses)>0):
    masses=[calculate_fuel(m) for m in masses if calculate_fuel(m)>0]
    total+=sum(masses)
print(total)