ls = []
while True:
    x = input()
    if x == '':
        break
    ls.append(x)

mp = {}
for i in range(len(ls)):
    for j in range(len(ls[i])):
        if ls[i][j] != '.':
            if ls[i][j] not in mp:
               mp[ls[i][j]] = [(i, j)]
            else:
                mp[ls[i][j]].append((i, j))

cnt = 0
for key, value in mp.items():
    for i in range(len(value)):
        for j in range(len(value)):
            if i == j:
                continue
            diff = value[j][0] - value[i][0], value[j][1] - value[i][1]
            loc1 = value[i]
            loc2 = value[j]
            while 0<=loc1[0]-diff[0]<len(ls) and 0<=loc1[1]-diff[1]<len(ls[0]):
                loc1 = loc1[0]-diff[0], loc1[1]-diff[1]
                if loc1!= value[i] and loc1 != value[j]:
                    ls[loc1[0]] = ls[loc1[0]][:loc1[1]] + '#' + ls[loc1[0]][loc1[1]+1:]
            loc1 = value[i]
            while 0<=loc1[0]+diff[0]<len(ls) and 0<=loc1[1]+diff[1]<len(ls[0]):
                loc1 = loc1[0]+diff[0], loc1[1]+diff[1]
                if loc1!= value[i] and loc1 != value[j]:
                    ls[loc1[0]] = ls[loc1[0]][:loc1[1]] + '#' + ls[loc1[0]][loc1[1]+1:]


for i in range(len(ls)):
    for j in range(len(ls[i])):
        if ls[i][j] != '.':
            cnt += 1    
print(cnt)