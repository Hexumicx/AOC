mapsize = 71
mp = [['.' for i in range(mapsize)] for j in range(mapsize)]
i = 0
ls = []
while True:
    i+=1
    x = input()
    if x=='':
        break
    x = x.split(',')
    x = [int(i) for i in x]
    ls.append(x)
    if i>2990:
        continue
    mp[x[1]][x[0]] = '#'

def findpath(mp):
    import queue
    pq = queue.PriorityQueue()
    pq.put([0,0,0])
    visited = [[False for i in range(mapsize)] for j in range(mapsize)]
    while not pq.empty():
        cur = pq.get()
        if cur[2] <0 or cur[2]>=mapsize or cur[1]<0 or cur[1]>=mapsize:
            continue
        if cur[2]==mapsize-1 and cur[1]==mapsize-1:
            return cur[0]
        if visited[cur[2]][cur[1]]:
            continue
        visited[cur[2]][cur[1]] = True
        if mp[cur[2]][cur[1]]=='#':
            continue
        for dir in [[0,1],[0,-1],[1,0],[-1,0]]:
            pq.put([cur[0]+1,cur[1]+dir[0],cur[2]+dir[1]])
    return -1

for i in range(1024, len(ls)):
    mp[ls[i][1]][ls[i][0]] = '#'
    if findpath(mp)==-1:
        print(ls[i])
        break

