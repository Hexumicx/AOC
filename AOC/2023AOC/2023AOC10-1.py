import queue
m = []
s = input()
while s != "":
    m.append(s)
    s = input()

x = -1
y = -1
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] == "S":
            x=i
            y=j

q = queue.Queue()
m2 = []
for i in range(len(m)):
    m2.append([])
    for j in range(len(m[i])):
        m2[i].append(-1)
m2[x][y] = 0
if(m[x-1][y]=="|" or m[x-1][y]=="7" or m[x-1][y]=="F"):
    q.put((x-1,y,1))
if(m[x+1][y]=="|" or m[x+1][y]=="J" or m[x+1][y]=="L"):
    q.put((x+1,y,1))
if(m[x][y-1]=="-" or m[x][y-1]=="L" or m[x][y-1]=="F"):
    q.put((x,y-1,1))
if(m[x][y+1]=="-" or m[x][y+1]=="J" or m[x][y+1]=="7"):
    q.put((x,y+1,1))
while not q.empty():
    cur = q.get()
    m2[cur[0]][cur[1]] = cur[2]
    if(m[cur[0]][cur[1]]=="|"):
        if(m2[cur[0]-1][cur[1]]==-1):
            q.put((cur[0]-1,cur[1],cur[2]+1))
        elif(m2[cur[0]+1][cur[1]]==-1):
            q.put((cur[0]+1,cur[1],cur[2]+1))
    if(m[cur[0]][cur[1]]=="-"):
        if(m2[cur[0]][cur[1]-1]==-1):
            q.put((cur[0],cur[1]-1,cur[2]+1))
        elif(m2[cur[0]][cur[1]+1]==-1):
            q.put((cur[0],cur[1]+1,cur[2]+1))
    if(m[cur[0]][cur[1]]=="7"):
        if(m2[cur[0]+1][cur[1]]==-1):
            q.put((cur[0]+1,cur[1],cur[2]+1))
        elif(m2[cur[0]][cur[1]-1]==-1):
            q.put((cur[0],cur[1]-1,cur[2]+1))
    if(m[cur[0]][cur[1]]=="J"):
        if(m2[cur[0]-1][cur[1]]==-1):
            q.put((cur[0]-1,cur[1],cur[2]+1))
        elif(m2[cur[0]][cur[1]-1]==-1):
            q.put((cur[0],cur[1]-1,cur[2]+1))
    if(m[cur[0]][cur[1]]=="L"):
        if(m2[cur[0]-1][cur[1]]==-1):
            q.put((cur[0]-1,cur[1],cur[2]+1))
        elif(m2[cur[0]][cur[1]+1]==-1):
            q.put((cur[0],cur[1]+1,cur[2]+1))
    if(m[cur[0]][cur[1]]=="F"):
        if(m2[cur[0]+1][cur[1]]==-1):
            q.put((cur[0]+1,cur[1],cur[2]+1))
        elif(m2[cur[0]][cur[1]+1]==-1):
            q.put((cur[0],cur[1]+1,cur[2]+1))

maxi = 0
for i in m2:
    for j in i:
        maxi = max(maxi,j)

print(maxi)
    
