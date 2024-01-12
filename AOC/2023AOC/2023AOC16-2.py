import queue
from copy import deepcopy
s = input()
maxi = -1
arr = []
while s!='':
    arr.append(s)
    s = input()

arr2 = [['.' for i in range(len(arr[0]))] for j in range(len(arr))]
q = queue.Queue()
q1 = queue.Queue()
for i in range(len(arr)):
    q1.put((i,0,'R'))
    q1.put((i,len(arr[0])-1,'L'))
for i in range(len(arr[0])):
    q1.put((0,i,'D'))
    q1.put((len(arr)-1,i,'U'))
while not q1.empty():
    q.put(q1.get())
    arr2 = [['.' for i in range(len(arr[0]))] for j in range(len(arr))]
    m = {}
    while not q.empty():
        cur = q.get()
        if(m.get((cur[0],cur[1],cur[2]))==None):
            m[(cur[0],cur[1],cur[2])] = 1
        else:
            continue
        if(cur[0]>=len(arr) or cur[1]>=len(arr[0]) or cur[0]<0 or cur[1]<0):
            continue
        arr2[cur[0]][cur[1]] = '#'
        if arr[cur[0]][cur[1]] == '.':
            if cur[2]=='R':
                q.put((cur[0],cur[1]+1,'R'))
            elif cur[2]=='L':
                q.put((cur[0],cur[1]-1,'L'))
            elif cur[2]=='U':
                q.put((cur[0]-1,cur[1],'U'))
            elif cur[2]=='D':
                q.put((cur[0]+1,cur[1],'D'))
        if arr[cur[0]][cur[1]] == '\\':
            if cur[2]=='R':
                q.put((cur[0]+1,cur[1],'D'))
            elif cur[2]=='L':
                q.put((cur[0]-1,cur[1],'U'))
            elif cur[2]=='U':
                q.put((cur[0],cur[1]-1,'L'))
            elif cur[2]=='D':
                q.put((cur[0],cur[1]+1,'R'))
        if arr[cur[0]][cur[1]] == '/':
            if cur[2]=='R':
                q.put((cur[0]-1,cur[1],'U'))
            elif cur[2]=='L':
                q.put((cur[0]+1,cur[1],'D'))
            elif cur[2]=='U':
                q.put((cur[0],cur[1]+1,'R'))
            elif cur[2]=='D':
                q.put((cur[0],cur[1]-1,'L'))
        if arr[cur[0]][cur[1]] == '-':
            if cur[2]=='R':
                q.put((cur[0],cur[1]+1,'R'))
            elif cur[2]=='L':
                q.put((cur[0],cur[1]-1,'L'))
            elif cur[2]=='U':
                q.put((cur[0],cur[1]-1,'L'))
                q.put((cur[0],cur[1]+1,'R'))
            elif cur[2]=='D':
                q.put((cur[0],cur[1]-1,'L'))
                q.put((cur[0],cur[1]+1,'R'))
        if arr[cur[0]][cur[1]] == '|':
            if cur[2]=='R':
                q.put((cur[0]+1,cur[1],'D'))
                q.put((cur[0]-1,cur[1],'U'))
            elif cur[2]=='L':
                q.put((cur[0]+1,cur[1],'D'))
                q.put((cur[0]-1,cur[1],'U'))
            elif cur[2]=='U':
                q.put((cur[0]-1,cur[1],'U'))
            elif cur[2]=='D':
                q.put((cur[0]+1,cur[1],'D'))

    count=0
    for i in arr2:
        for j in i:
            if j=='#':
                count += 1
    maxi = max(maxi,count)
print(maxi)
