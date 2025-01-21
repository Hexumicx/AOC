mp = []
while True:
    x = input()
    if x == '': break
    x = list(x)
    mp.append(x)

for i in range(0, len(mp)):
    for j in range(0, len(mp[i])):
        if mp[i][j] == 'S':
            x, y = i, j
        if mp[i][j] == 'E':
            ex, ey = i, j

m = {}

import queue
pq = queue.PriorityQueue()
pq.put((0, x, y, 'E'))    
        
    
while not pq.empty():
    cur = pq.get()
    if cur[1] == ex and cur[2] == ey:
        print(cur[0])
        break
    if (cur[1], cur[2], cur[3]) in m:
        continue
    m[(cur[1], cur[2], cur[3])] = cur[0]
    if mp[cur[1]][cur[2]] == '#':
        continue    
    if cur[3] == 'E':
        pq.put((cur[0]+1000, cur[1], cur[2], 'S'))
        pq.put((cur[0]+1000, cur[1], cur[2], 'N'))
        pq.put((cur[0]+1, cur[1], cur[2]+1, 'E'))
    elif cur[3] == 'N':
        pq.put((cur[0]+1000, cur[1], cur[2], 'E'))
        pq.put((cur[0]+1000, cur[1], cur[2], 'W'))
        pq.put((cur[0]+1, cur[1]-1, cur[2], 'N'))
    elif cur[3] == 'W':
        pq.put((cur[0]+1000, cur[1], cur[2], 'N'))
        pq.put((cur[0]+1000, cur[1], cur[2], 'S'))
        pq.put((cur[0]+1, cur[1], cur[2]-1, 'W'))
    elif cur[3] == 'S':
        pq.put((cur[0]+1000, cur[1], cur[2], 'W'))
        pq.put((cur[0]+1000, cur[1], cur[2], 'E'))
        pq.put((cur[0]+1, cur[1]+1, cur[2], 'S'))

    
