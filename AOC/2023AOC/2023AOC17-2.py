from queue import Queue, PriorityQueue
s = input()
arr = []
while s!='':
    arr.append(list(s))
    s = input()

for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = int(arr[i][j])

v = [[{} for i in range(len(arr[0]))] for j in range(len(arr))]
q = PriorityQueue()
q.put((0, 0, 0, (1,'D')))
q.put((0, 0, 0, (1,'R')))
while not q.empty():
    cur = q.get()
    cur = list(cur)
    if(cur[1]>=len(arr) or cur[2]>=len(arr[0]) or cur[1]<0 or cur[2]<0):
        continue
    if(v[cur[1]][cur[2]].get(cur[3],-1)!=-1):
        continue
    else:
        v[cur[1]][cur[2]][cur[3]] = cur[0]
    if(cur[3][0]==10):
        if(cur[3][1]=='R'):
            if(cur[1]+1<len(arr)):
                q.put((cur[0]+arr[cur[1]+1][cur[2]], cur[1]+1, cur[2], (1,'D')))
            if(cur[1]-1>=0):
                q.put((cur[0]+arr[cur[1]-1][cur[2]], cur[1]-1, cur[2], (1,'U')))
        elif(cur[3][1]=='L'):
            if(cur[1]+1<len(arr)):
                q.put((cur[0]+arr[cur[1]+1][cur[2]], cur[1]+1, cur[2], (1,'D')))
            if(cur[1]-1>=0):
                q.put((cur[0]+arr[cur[1]-1][cur[2]], cur[1]-1, cur[2], (1,'U')))
        elif(cur[3][1]=='U'):
            if(cur[2]-1>=0):
                q.put((cur[0]+arr[cur[1]][cur[2]-1], cur[1], cur[2]-1, (1,'L')))
            if(cur[2]+1<len(arr[0])):
                q.put((cur[0]+arr[cur[1]][cur[2]+1], cur[1], cur[2]+1, (1,'R')))
        elif(cur[3][1]=='D'):
            if(cur[2]-1>=0):
                q.put((cur[0]+arr[cur[1]][cur[2]-1], cur[1], cur[2]-1, (1,'L')))
            if(cur[2]+1<len(arr[0])):
                q.put((cur[0]+arr[cur[1]][cur[2]+1], cur[1], cur[2]+1, (1,'R')))
    elif(cur[3][0]>=4):
        if(cur[3][1]=='R'):
            if(cur[1]+1<len(arr)):
                q.put((cur[0]+arr[cur[1]+1][cur[2]], cur[1]+1, cur[2], (1,'D')))
            if(cur[1]-1>=0):
                q.put((cur[0]+arr[cur[1]-1][cur[2]], cur[1]-1, cur[2], (1,'U')))
            if(cur[2]+1<len(arr[0])):
                q.put((cur[0]+arr[cur[1]][cur[2]+1], cur[1], cur[2]+1, (cur[3][0]+1,'R')))
        elif(cur[3][1]=='L'):
            if(cur[1]+1<len(arr)):
                q.put((cur[0]+arr[cur[1]+1][cur[2]], cur[1]+1, cur[2], (1,'D')))
            if(cur[1]-1>=0):
                q.put((cur[0]+arr[cur[1]-1][cur[2]], cur[1]-1, cur[2], (1,'U')))
            if(cur[2]-1>=0):
                q.put((cur[0]+arr[cur[1]][cur[2]-1], cur[1], cur[2]-1, (cur[3][0]+1,'L')))
        elif(cur[3][1]=='U'):
            if(cur[2]-1>=0):
                q.put((cur[0]+arr[cur[1]][cur[2]-1], cur[1], cur[2]-1, (1,'L')))
            if(cur[2]+1<len(arr[0])):
                q.put((cur[0]+arr[cur[1]][cur[2]+1], cur[1], cur[2]+1, (1,'R')))
            if(cur[1]-1>=0):
                q.put((cur[0]+arr[cur[1]-1][cur[2]], cur[1]-1, cur[2], (cur[3][0]+1,'U')))
        elif(cur[3][1]=='D'):
            if(cur[2]-1>=0):
                q.put((cur[0]+arr[cur[1]][cur[2]-1], cur[1], cur[2]-1, (1,'L')))
            if(cur[2]+1<len(arr[0])):
                q.put((cur[0]+arr[cur[1]][cur[2]+1], cur[1], cur[2]+1, (1,'R')))
            if(cur[1]+1<len(arr)):
                q.put((cur[0]+arr[cur[1]+1][cur[2]], cur[1]+1, cur[2], (cur[3][0]+1,'D')))
    else:
        if(cur[3][1]=='R'):
            if(cur[2]+1<len(arr[0])):
                q.put((cur[0]+arr[cur[1]][cur[2]+1], cur[1], cur[2]+1, (cur[3][0]+1,'R')))
        elif(cur[3][1]=='L'):
            if(cur[2]-1>=0):
                q.put((cur[0]+arr[cur[1]][cur[2]-1], cur[1], cur[2]-1, (cur[3][0]+1,'L')))
        elif(cur[3][1]=='U'):
            if(cur[1]-1>=0):
                q.put((cur[0]+arr[cur[1]-1][cur[2]], cur[1]-1, cur[2], (cur[3][0]+1,'U')))
        elif(cur[3][1]=='D'):
            if(cur[1]+1<len(arr)):
                q.put((cur[0]+arr[cur[1]+1][cur[2]], cur[1]+1, cur[2], (cur[3][0]+1,'D')))

print(min(v[len(arr)-1][len(arr[0])-1].values()))