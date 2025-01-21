map = []
while True:
    x = input()
    if x == "": 
        break
    s = [int(i) for i in x]
    map.append(s)

import queue
q = queue.Queue()
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == 0:
            q.put((i, j, 0))

q2 = queue.Queue()
total = 0

while not q.empty():
    i, j, d = q.get()
    q2.put((i, j, d))
    visited = set()
    while not q2.empty():
        i, j, d = q2.get()
        if (i, j) in visited:
            continue
        else:
            visited.add((i, j))
        if d==9:
            total += 1
            continue
        if i < 0 or i >= len(map) or j < 0 or j >= len(map[i]):
            continue
        if 0<=i-1<len(map) and map[i-1][j] == d+1:
            q2.put((i-1, j, d+1))
        if 0<=i+1<len(map) and map[i+1][j] == d+1:
            q2.put((i+1, j, d+1))
        if 0<=j-1<len(map[i]) and map[i][j-1] == d+1:
            q2.put((i, j-1, d+1))
        if 0<=j+1<len(map[i]) and map[i][j+1] == d+1:
            q2.put((i, j+1, d+1))
        
print(total)
