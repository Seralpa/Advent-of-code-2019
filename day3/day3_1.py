import re
regex=re.compile(r"([UDRL])(\d+)")

def folLow_wire_path(instructions):
    path=set()
    current_pos=(0,0)#x,y
    for i in instructions:
        match_i=regex.match(i)
        dire=match_i.group(1)
        cant=int(match_i.group(2))
        if dire=='R':
            for _ in range(cant):
                current_pos=(current_pos[0]+1,current_pos[1])
                path.add(current_pos)
        elif dire=='L':
            for _ in range(cant):
                current_pos=(current_pos[0]-1,current_pos[1])
                path.add(current_pos)
        elif dire=='U':
            for _ in range(cant):
                current_pos=(current_pos[0],current_pos[1]+1)
                path.add(current_pos)
        elif dire=='D':
            for _ in range(cant):
                current_pos=(current_pos[0],current_pos[1]-1)
                path.add(current_pos)
    return path


with open("input1.txt","r") as f:
    wire1=f.readline().split(",")
    wire2=f.readline().split(",")
w1_path=folLow_wire_path(wire1)
w2_path=folLow_wire_path(wire2)
intersections=sorted(list(w1_path.intersection(w2_path)),key=lambda x:abs(x[0])+abs(x[1]))
print(abs(intersections[0][0])+abs(intersections[0][1]))
