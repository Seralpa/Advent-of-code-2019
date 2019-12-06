import networkx as nx
with open("input1.txt","r") as f:
    lines=[l.strip().split(")") for l in f.readlines()]

g=nx.Graph()
for l in lines:
    g.add_edge(l[0],l[1])
print(nx.shortest_path_length(g,"YOU","SAN")-2)
