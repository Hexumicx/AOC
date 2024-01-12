s=input()
instructions=[]
while s!='':
    d, l, hex = s.split(" ")
    instructions.append((d, int(l)))
    s=input()

m = [["." for i in range(10000)] for j in range(10000)]
start = (0,0)
points = []
points.append(start)
for i in instructions:
    if(i[0]=='U'):
        for j in range(i[1]):
            m[start[0]][start[1]]="#"
            start=(start[0]-1, start[1])
            points.append(start)
    elif(i[0]=='D'):
        for j in range(i[1]):
            m[start[0]][start[1]]="#"
            start=(start[0]+1, start[1])
            points.append(start)
    elif(i[0]=='L'):
        for j in range(i[1]):
            m[start[0]][start[1]]="#"
            start=(start[0], start[1]-1)
            points.append(start)
    elif(i[0]=='R'):
        for j in range(i[1]):
            m[start[0]][start[1]]="#"
            start=(start[0], start[1]+1)
            points.append(start)

count = 0
for i in range(len(m)):
    for j in range(len(m[0])):
      if(m[i][j]=="#"):
          count+=1

area = 0
for i in range(len(points)-1):
    area+=(points[i][0]+points[i+1][0])*(points[i][1]-points[i+1][1])
area+= (points[-1][0]+points[0][0])*(points[-1][1]-points[0][1])
area = abs(area)/2

interior = area - count/2 + 1
print(interior+count)

# for i in m:
#     print(''.join(i))