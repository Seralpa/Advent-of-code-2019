import re
ins_format=re.compile(r"((?:[a-z]+_?)*)(-?\d*)")

def cut(deck, n):
    return deck[int(n):]+deck[:int(n)]

def deal_with_increment(deck, n):
    aux=[0 for _ in deck]
    for i,c in enumerate(deck):
        aux[(i*int(n))%len(deck)]=c
    return aux

def deal_into_new_stack(deck, useless):
    return list(reversed(deck))

deck=list(range(10007))
shuffles={"cut":cut,"deal_with_increment":deal_with_increment,"deal_into_new_stac":deal_into_new_stack}

with open("input.txt") as f:
    instructions=[(ins_format.match(i.strip().replace(' ','_')).group(1)[:-1],ins_format.match(i.strip().replace(' ','_')).group(2)) for i in f.readlines()]
for i in instructions:
    deck=shuffles[i[0]](deck,i[1])
print(deck.index(2019))