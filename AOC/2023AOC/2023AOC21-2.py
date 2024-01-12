from queue import Queue
import numpy as np
s = input()
m2 = []
while s != '':
    m2.append(list(s)*11)
    s = input()

m = []
for i in range(11):
    for row in m2:
        m.append(row)
v = [[-1 for i in range(len(m[0]))] for j in range(len(m))]
for i in m:
    for j in i:
        if j=='S':
            sx = i.index(j)
            sy = m.index(i)
            m[sy][sx] = '.'

q = Queue()
q.put((720,720, 0))
ss = 0
steps = [66, 197,328,459, 590, 721]
data = []
while not q.empty():
    x,y,step = q.get()
    ss = step
    if step in steps:
        count = 0
        for i in v:
            for j in i:
                if j==(step-1)%2:
                    count += 1
        data.append(count)
        steps.remove(step)
    # if x==0 or x==len(m)-1 or y==0 or y==len(m[0])-1:
    #     continue
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
        if j==1:
            count += 1
fitting = np.polyfit([66, 197,328,459], data[:4], 2)
fitted = np.poly1d(fitting)
print(fitted(26501366))
print(fitting)
print(' '.join([str(i) for i in data]))



