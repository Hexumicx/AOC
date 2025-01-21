mp = []
while True:
    x = input()
    if x =="": break
    x = list(x)
    mp.append(x)

for i in range(len(mp)):
    for j in range(len(mp[i])):
        if mp[i][j] == "S":
            sx, sy = i, j
            mp[i][j] = "."
        if mp[i][j] == "E":
            gx, gy = i, j
            mp[i][j] = "."
    
import queue
def findshortestpath(mp, sx, sy, gx, gy):
    pq = queue.PriorityQueue()
    pq.put((0, sx, sy))
    ogtime = 1e9
    visited = [[False for i in range(len(mp[0]))] for j in range(len(mp))]
    times = [[1e9 for i in range(len(mp[0]))] for j in range(len(mp))]
    while not pq.empty():
        cur = pq.get()
        time, x, y = cur
        if x == gx and y == gy:
            ogtime = min(ogtime, time)
        if mp[x][y] == "#":
            continue
        times[x][y] = min(times[x][y], time)
        if visited[x][y]:
            continue
        visited[x][y] = True
        for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = x + dir[0]
            ny = y + dir[1]
            if 0 <= nx < len(mp) and 0 <= ny < len(mp[0]):
                pq.put((time + 1, nx, ny))
    return ogtime, times

total = 0
ogtime,times = findshortestpath(mp, sx, sy, gx, gy)
for i in range(len(mp)):
    print(i)
    for j in range(len(mp[i])):
        if mp[i][j] == "#":
            if 0<=i-1<len(mp) and 0<=i+1<len(mp) and mp[i-1][j] != "#" and mp[i+1][j] != "#":
                if abs(times[i-1][j]-times[i+1][j])-2 >= 100:
                    total += 1
            if 0<=j-1<len(mp[i]) and 0<=j+1<len(mp[i]) and mp[i][j-1] != "#" and mp[i][j+1] != "#":
                if abs(times[i][j-1]-times[i][j+1])-2 >= 100:
                    total += 1


print(total)
