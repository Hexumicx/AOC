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

sum = 0
while not q1.empty():
    tp = q1.get()
    if visited[tp[0]][tp[1]]: continue
    q.put(tp)
    area = 0
    perimeter = 0
    while not q.empty():
        cur = q.get()
        if visited[cur[0]][cur[1]]: continue
        visited[cur[0]][cur[1]] = True
        area += 1
        if 0<=cur[0]-1<len(map) and map[cur[0]-1][cur[1]] == map[cur[0]][cur[1]]:
            q.put((cur[0]-1, cur[1]))
        else:
            perimeter += 1
        if 0<=cur[0]+1<len(map) and map[cur[0]+1][cur[1]] == map[cur[0]][cur[1]]:
            q.put((cur[0]+1, cur[1]))
        else:
            perimeter += 1
        if 0<=cur[1]-1<len(map[0]) and map[cur[0]][cur[1]-1] == map[cur[0]][cur[1]]:
            q.put((cur[0], cur[1]-1))
        else:
            perimeter += 1
        if 0<=cur[1]+1<len(map[0]) and map[cur[0]][cur[1]+1] == map[cur[0]][cur[1]]:
            q.put((cur[0], cur[1]+1))
        else:
            perimeter += 1
    sum += area * perimeter

print(sum) 
