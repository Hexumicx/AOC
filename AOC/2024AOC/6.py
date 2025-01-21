mp = []
while True:
    x = input()
    if x == "":
        break
    mp.append(x)

for i in range(len(mp)):
    for j in range(len(mp[i])):
        if mp[i][j] == "^":
            start = (i,j, (-1, 0))
            break
mv = [(-1,0), (0,1), (1,0), (0,-1)]
while True:
    nxtpos = (start[0] + start[2][0], start[1] + start[2][1])
    if 0<=nxtpos[0]<len(mp) and 0<=nxtpos[1]<len(mp[0]) and mp[nxtpos[0]][nxtpos[1]] == "#":
        start = (start[0], start[1], mv[(mv.index(start[2])+1)%4])
    else:
        mp[start[0]] = mp[start[0]][:start[1]] + "X" + mp[start[0]][start[1]+1:]
        start = (nxtpos[0], nxtpos[1], start[2])
    if start[0]<0 or start[0]>=len(mp) or start[1]<0 or start[1]>=len(mp[0]):
        break
cnt = 0
for i in mp:
    for j in i:
        if j=="X":
            cnt += 1

print(cnt)