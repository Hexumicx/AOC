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
pq.put((0, x, y, 'E', [(x, y)]))    
minval = 1000000000

while not pq.empty():
    cur = pq.get()
    if cur[1] == ex and cur[2] == ey:
        if minval == 1000000000:
            minval = cur[0]
        
        if cur[0] == minval:
            for i in cur[4]:
                mp[i[0]][i[1]] = 'O'

    if (cur[1], cur[2], cur[3]) in m:
        if m[(cur[1], cur[2], cur[3])] == cur[0]:
            pass
        else:
            continue
    m[(cur[1], cur[2], cur[3])] = cur[0]
    if mp[cur[1]][cur[2]] == '#':
        continue    
    if cur[3] == 'E':
        pq.put((cur[0]+1000, cur[1], cur[2], 'S', cur[4]))
        pq.put((cur[0]+1000, cur[1], cur[2], 'N', cur[4]))
        pq.put((cur[0]+1, cur[1], cur[2]+1, 'E', cur[4]+[(cur[1], cur[2])]))
    elif cur[3] == 'N':
        pq.put((cur[0]+1000, cur[1], cur[2], 'E', cur[4]))
        pq.put((cur[0]+1000, cur[1], cur[2], 'W', cur[4]))
        pq.put((cur[0]+1, cur[1]-1, cur[2], 'N', cur[4]+[(cur[1], cur[2])]))
    elif cur[3] == 'W':
        pq.put((cur[0]+1000, cur[1], cur[2], 'N', cur[4]))
        pq.put((cur[0]+1000, cur[1], cur[2], 'S', cur[4]))
        pq.put((cur[0]+1, cur[1], cur[2]-1, 'W', cur[4]+[(cur[1], cur[2])]))
    elif cur[3] == 'S':
        pq.put((cur[0]+1000, cur[1], cur[2], 'W', cur[4]))
        pq.put((cur[0]+1000, cur[1], cur[2], 'E', cur[4]))
        pq.put((cur[0]+1, cur[1]+1, cur[2], 'S', cur[4]+[(cur[1], cur[2])]))

num = 0
for i in range(0, len(mp)):
    for j in range(0, len(mp[i])):
        print(mp[i][j], end='')
        if mp[i][j] == 'O':
            num += 1
    print()

print(num+1)
