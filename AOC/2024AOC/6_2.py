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
            mp[i] = mp[i][:j] + "." + mp[i][j+1:]
            break
mv = [(-1,0), (0,1), (1,0), (0,-1)]
mmp = {}
cnt = 0
visited = set()
while True:
    if start[0]<0 or start[0]>=len(mp) or start[1]<0 or start[1]>=len(mp[0]):
        break
    nxtpos = (start[0] + start[2][0], start[1] + start[2][1])
    turnpos = (start[0], start[1], mv[(mv.index(start[2])+1)%4])
    blockpos = nxtpos
    t1 = turnpos
    flag = True
    done = False
    if blockpos[0]>=len(mp) or blockpos[1]>=len(mp[0]) or blockpos[0]<0 or blockpos[1]<0:
        break
    if mp[blockpos[0]][blockpos[1]] == "#": 
        flag = False
    else:
        mp[blockpos[0]] = mp[blockpos[0]][:blockpos[1]] + "#" + mp[blockpos[0]][blockpos[1]+1:]
    while True:
        while 0<=t1[0]<len(mp) and 0<=t1[1]<len(mp[0]):
            tt = (t1[0]+t1[2][0], t1[1]+t1[2][1], t1[2])
            if t1 == start: # looped
                cnt += 1
                visited.add(blockpos)
                done = True
                break
            if 0<=tt[0]<len(mp) and 0<=tt[1]<len(mp[0]) and mp[tt[0]][tt[1]] == "#": # wall
                break
            t1 = tt
        if done: 
            break
        if t1[0]<0 or t1[0]>=len(mp) or t1[1]<0 or t1[1]>=len(mp[0]): 
            break
        t1 = (t1[0], t1[1], mv[(mv.index(t1[2])+1)%4])

    if flag: mp[blockpos[0]] = mp[blockpos[0]][:blockpos[1]] + "." + mp[blockpos[0]][blockpos[1]+1:]
    if 0<=nxtpos[0]<len(mp) and 0<=nxtpos[1]<len(mp[0]) and mp[nxtpos[0]][nxtpos[1]] == "#":
        start = (start[0], start[1], mv[(mv.index(start[2])+1)%4])
    else:
        start = (nxtpos[0], nxtpos[1], start[2])
    

print(cnt)