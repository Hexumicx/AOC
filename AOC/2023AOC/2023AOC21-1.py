from queue import Queue
s = input()
m = []
while s != '':
    m.append(list(s))
    s = input()

v = [[-1 for i in range(len(m[0]))] for j in range(len(m))]
for i in m:
    for j in i:
        if j=='S':
            sx = i.index(j)
            sy = m.index(i)

q = Queue()
q.put((sx,sy, 0))
while not q.empty():
    x,y,step = q.get()
    if step>64:
        break
    if x<0 or x>=len(m) or y<0 or y>=len(m[0]):
        continue
    if v[x][y] != -1:
        continue
    v[x][y] = step%2
    if x-1>=0 and m[x-1][y]=='.':
        q.put((x-1,y,step+1))
    if x+1<len(m) and  m[x+1][y]=='.':
        q.put((x+1,y,step+1))
    if y-1>=0 and m[x][y-1]=='.':
        q.put((x,y-1,step+1))
    if y+1<len(m[0]) and m[x][y+1]=='.':
        q.put((x,y+1,step+1))

count = 0
for i in v:
    for j in i:
        if j==0:
            count += 1

print(count)