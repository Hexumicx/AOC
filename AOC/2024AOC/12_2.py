map = []
while True:
    x = input()
    if x == '': break
    map.append(x)

import queue
visited = [[False for i in range(len(map[0]))] for j in range(len(map))]
q = queue.Queue()
q1 = queue.Queue()
for i in range(len(map)):
    for j in range(len(map[i])):
        q1.put((i, j))
perim = [[True for i in range(len(map[0]))] for j in range(len(map))]
for i in range(len(map)):
    for j in range(len(map[i])):
        if 0<=i-1<len(map) and map[i-1][j] == map[i][j]:
            if 0<=i+1<len(map) and map[i+1][j] == map[i][j]:
                if 0<=j-1<len(map[0]) and map[i][j-1] == map[i][j]:
                    if 0<=j+1<len(map[0]) and map[i][j+1] == map[i][j]:
                        perim[i][j] = False

def isperimeter(point, map):
    i, j = point
    for dir in [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]:
        if 0<=i+dir[0]<len(map) and 0<=j+dir[1]<len(map[0]) and map[i+dir[0]][j+dir[1]] != map[i][j]:
            return True
    return False

sum = 0
while not q1.empty():
    tp = q1.get()
    if visited[tp[0]][tp[1]]: continue
    q.put(tp)
    area = 0
    sides = 0
    debug = []
    while not q.empty():
        cur = q.get()
        if visited[cur[0]][cur[1]]: continue
        visited[cur[0]][cur[1]] = True
        area += 1
        iside = sides
        #concave corners
        if 0<=cur[0]-1<len(map) and map[cur[0]-1][cur[1]] == map[cur[0]][cur[1]]:
            if 0<=cur[1]-1<len(map[0]) and map[cur[0]][cur[1]-1] == map[cur[0]][cur[1]]:
                if map[cur[0]-1][cur[1]-1] != map[cur[0]][cur[1]]:
                    sides += 1
        if 0<=cur[1]-1<len(map[0]) and map[cur[0]][cur[1]-1] == map[cur[0]][cur[1]]:
            if 0<=cur[0]+1<len(map) and map[cur[0]+1][cur[1]] == map[cur[0]][cur[1]]:
                if map[cur[0]+1][cur[1]-1] != map[cur[0]][cur[1]]:
                    sides += 1
        if 0<=cur[0]+1<len(map) and map[cur[0]+1][cur[1]] == map[cur[0]][cur[1]]:
            if 0<=cur[1]+1<len(map[0]) and map[cur[0]][cur[1]+1] == map[cur[0]][cur[1]]:
                if map[cur[0]+1][cur[1]+1] != map[cur[0]][cur[1]]:
                    sides += 1
        if 0<=cur[1]+1<len(map[0]) and map[cur[0]][cur[1]+1] == map[cur[0]][cur[1]]:
            if 0<=cur[0]-1<len(map) and map[cur[0]-1][cur[1]] == map[cur[0]][cur[1]]:
                if map[cur[0]-1][cur[1]+1] != map[cur[0]][cur[1]]:
                    sides += 1
        #convex corners
        if cur[0]-1<0 or cur[0]-1>=len(map) or (0<=cur[0]-1<len(map) and map[cur[0]-1][cur[1]] != map[cur[0]][cur[1]]):
            if cur[1]-1<0 or cur[1]-1>=len(map[0]) or (0<=cur[1]-1<len(map[0]) and map[cur[0]][cur[1]-1] != map[cur[0]][cur[1]]):
                sides += 1
        if cur[1]-1<0 or cur[1]-1>=len(map[0]) or (0<=cur[1]-1<len(map[0]) and map[cur[0]][cur[1]-1] != map[cur[0]][cur[1]]):
            if cur[0]+1<0 or cur[0]+1>=len(map) or (0<=cur[0]+1<len(map) and map[cur[0]+1][cur[1]] != map[cur[0]][cur[1]]):
                sides += 1
        if cur[0]+1<0 or cur[0]+1>=len(map) or (0<=cur[0]+1<len(map) and map[cur[0]+1][cur[1]] != map[cur[0]][cur[1]]):
            if cur[1]+1<0 or cur[1]+1>=len(map[0]) or (0<=cur[1]+1<len(map[0]) and map[cur[0]][cur[1]+1] != map[cur[0]][cur[1]]):
                sides += 1
        if cur[1]+1<0 or cur[1]+1>=len(map[0]) or (0<=cur[1]+1<len(map[0]) and map[cur[0]][cur[1]+1] != map[cur[0]][cur[1]]):
            if cur[0]-1<0 or cur[0]-1>=len(map) or (0<=cur[0]-1<len(map) and map[cur[0]-1][cur[1]] != map[cur[0]][cur[1]]):
                sides += 1

        if iside != sides:
            debug.append(cur)

        if 0<=cur[0]-1<len(map) and map[cur[0]-1][cur[1]] == map[cur[0]][cur[1]]:
            q.put((cur[0]-1, cur[1]))
        if 0<=cur[0]+1<len(map) and map[cur[0]+1][cur[1]] == map[cur[0]][cur[1]]:
            q.put((cur[0]+1, cur[1]))
        if 0<=cur[1]-1<len(map[0]) and map[cur[0]][cur[1]-1] == map[cur[0]][cur[1]]:
            q.put((cur[0], cur[1]-1))
        if 0<=cur[1]+1<len(map[0]) and map[cur[0]][cur[1]+1] == map[cur[0]][cur[1]]:
            q.put((cur[0], cur[1]+1))
    sum += area * sides

print(sum) 
