ls = {}
while True:
    x = input()
    if x == '': break
    x = x.split("-")
    if x[0] not in ls:
        ls[x[0]] = set()
        ls[x[0]].add(x[1])
    else:
        ls[x[0]].add(x[1])
    if x[1] not in ls:
        ls[x[1]] = set()
        ls[x[1]].add(x[0])
    else:  
        ls[x[1]].add(x[0])

from functools import cache
lans = set()
mxset = set()
@cache
def is_clique(nodes):
    global ls
    checkset = set(nodes)
    for node in nodes:
        neighbors = ls[node].copy()
        neighbors.add(node)
        checkset = checkset.intersection(neighbors)
    if len(checkset) == len(nodes):    
        return True
    else:
        return False

@cache
def find_largest_clique(cur, nodes):
    global ls
    if len(nodes) == 0:
        return cur
    nodels1 = []
    if is_clique(cur+(nodes[0],)):
        nodels1 = find_largest_clique(cur+(nodes[0],), nodes[1:])
    nodels2 =  find_largest_clique(cur, nodes[1:])
    if len(nodels1) > len(nodels2):
        return nodels1
    else:
        return nodels2

mxset = set()
for key, value in ls.items():
    s = find_largest_clique((key,), tuple(value))
    if len(s) > len(mxset):
        mxset = s
print(','.join(sorted(mxset)))
