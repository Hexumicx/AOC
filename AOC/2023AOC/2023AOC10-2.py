import queue
m = []
coords = []
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
coords.append((x,y))
coords.append((x-1,y))
q.put((x-1,y))
while not q.empty():
    cur = q.get()
    m2[cur[0]][cur[1]] = 0
    if(m[cur[0]][cur[1]]=="|"):
        if(m2[cur[0]-1][cur[1]]==-1):
            coords.append((cur[0]-1,cur[1]))
            q.put((cur[0]-1,cur[1]))
        elif(m2[cur[0]+1][cur[1]]==-1):
            coords.append((cur[0]+1,cur[1]))
            q.put((cur[0]+1,cur[1]))
    if(m[cur[0]][cur[1]]=="-"):
        if(m2[cur[0]][cur[1]-1]==-1):
            coords.append((cur[0],cur[1]-1))
            q.put((cur[0],cur[1]-1))
        elif(m2[cur[0]][cur[1]+1]==-1):
            coords.append((cur[0],cur[1]+1))
            q.put((cur[0],cur[1]+1))
    if(m[cur[0]][cur[1]]=="J"):
        if(m2[cur[0]-1][cur[1]]==-1): 
            coords.append((cur[0]-1,cur[1]))
            q.put((cur[0]-1,cur[1]))
        elif(m2[cur[0]][cur[1]-1]==-1):
            coords.append((cur[0],cur[1]-1))
            q.put((cur[0],cur[1]-1))
    if(m[cur[0]][cur[1]]=="F"):
        if(m2[cur[0]+1][cur[1]]==-1):
            coords.append((cur[0]+1,cur[1]))
            q.put((cur[0]+1,cur[1]))
        elif(m2[cur[0]][cur[1]+1]==-1):
            coords.append((cur[0],cur[1]+1))
            q.put((cur[0],cur[1]+1))
    if(m[cur[0]][cur[1]]=="L"):
        if(m2[cur[0]-1][cur[1]]==-1):
            coords.append((cur[0]-1,cur[1]))
            q.put((cur[0]-1,cur[1]))
        elif(m2[cur[0]][cur[1]+1]==-1):
            coords.append((cur[0],cur[1]+1))
            q.put((cur[0],cur[1]+1))
    if(m[cur[0]][cur[1]]=="7"):
        if(m2[cur[0]+1][cur[1]]==-1):
            coords.append((cur[0]+1,cur[1]))
            q.put((cur[0]+1,cur[1]))
        elif(m2[cur[0]][cur[1]-1]==-1):
            coords.append((cur[0],cur[1]-1))
            q.put((cur[0],cur[1]-1))

print(len(coords))

Area = 0
for i in range(len(coords)-1):
    Area += (coords[i][1]+coords[i+1][1])*(coords[i][0]-coords[i+1][0])
Area += (coords[len(coords)-1][1]+coords[0][1])*(coords[len(coords)-1][0]-coords[0][0])
Area /= 2
Area = abs(Area)
print(Area)

res = Area - len(coords)/2 + 1
print(res)
for i in range(len(m2)):
    for j in range(len(m2[i])):
        if(i==x and j==y):
            print("S",end="")
            continue
        if m2[i][j] == -1:
            print("*",end="")
        else:
            print(m2[i][j],end="")
    print()
