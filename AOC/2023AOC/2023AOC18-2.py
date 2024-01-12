s=input()
instructions=[]
while s!='':
    d, l, hex = s.split(" ")
    if(hex[-2]=="0"):
        d = "R"
    elif(hex[-2]=="1"):
        d = "D"
    elif(hex[-2]=="2"):
        d = "L"
    elif(hex[-2]=="3"):
        d = "U"
    hex = int(hex[2:-2],16)
    instructions.append((d, hex))
    s=input()

start = (0,0)
count = 0
points = []
points.append(start)
for i in instructions:
    if(i[0]=='U'):
        start = (start[0]-i[1], start[1])
        count+=i[1]
    elif(i[0]=='D'):
        start = (start[0]+i[1], start[1])
        count+=i[1]
    elif(i[0]=='L'):
        start = (start[0], start[1]-i[1])
        count+=i[1]
    elif(i[0]=='R'):
        start = (start[0], start[1]+i[1])
        count+=i[1]
    points.append(start)
area = 0
for i in range(len(points)-1):
    area+=(points[i][0]+points[i+1][0])*(points[i][1]-points[i+1][1])
area+= (points[-1][0]+points[0][0])*(points[-1][1]-points[0][1])
area = abs(area)/2

interior = area - count/2 + 1
print(int(interior+count))

# for i in m:
#     print(''.join(i))