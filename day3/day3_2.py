import re
regex=re.compile(r"([UDRL])(\d+)")

def folLow_wire_path(wire):
    path=set()
    current_pos=(0,0)#x,y
    for i in wire:
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

def step_to_pos(pos, wire):
    steps=0
    current_pos=(0,0)
    for i in wire:
        match_i=regex.match(i)
        dire=match_i.group(1)
        cant=int(match_i.group(2))
        if dire=='R':
            for _ in range(cant):
                current_pos=(current_pos[0]+1,current_pos[1])
                steps+=1
                if current_pos==pos:
                    return steps
        elif dire=='L':
            for _ in range(cant):
                current_pos=(current_pos[0]-1,current_pos[1])
                steps+=1
                if current_pos==pos:
                    return steps
        elif dire=='U':
            for _ in range(cant):
                current_pos=(current_pos[0],current_pos[1]+1)
                steps+=1
                if current_pos==pos:
                    return steps
        elif dire=='D':
            for _ in range(cant):
                current_pos=(current_pos[0],current_pos[1]-1)
                steps+=1
                if current_pos==pos:
                    return steps
            
with open("input1.txt","r") as f:
    wire1=f.readline().split(",")
    wire2=f.readline().split(",")
w1_path=folLow_wire_path(wire1)
w2_path=folLow_wire_path(wire2)
intersections=list(w1_path.intersection(w2_path))
intersections_steps=[step_to_pos(i,wire1)+step_to_pos(i,wire2) for i in intersections]
intersections_steps.sort(key=lambda x:x)
print(intersections_steps[0])



