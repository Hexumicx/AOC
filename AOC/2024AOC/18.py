mapsize = 71
mp = [['.' for i in range(mapsize)] for j in range(mapsize)]
i = 0
while True:
    i+=1
    x = input()
    if x=='':
        break
    if i>1024:
        continue
    x = x.split(',')
    x = [int(i) for i in x]
    mp[x[1]][x[0]] = '#'


import queue
pq = queue.PriorityQueue()
pq.put([0,0,0])
visited = [[False for i in range(mapsize)] for j in range(mapsize)]
while not pq.empty():
    cur = pq.get()
    print(cur)
    if cur[2] <0 or cur[2]>=mapsize or cur[1]<0 or cur[1]>=mapsize:
        continue
    if cur[2]==mapsize-1 and cur[1]==mapsize-1:
        print(cur[0])
        break
    if visited[cur[2]][cur[1]]:
        continue
    visited[cur[2]][cur[1]] = True
    if mp[cur[2]][cur[1]]=='#':
        continue
    for dir in [[0,1],[0,-1],[1,0],[-1,0]]:
        pq.put([cur[0]+1,cur[1]+dir[0],cur[2]+dir[1]])


# for i in mp:
#     print(i)


