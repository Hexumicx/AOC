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
        for j in range(i + 1, len(value)):
            diff = value[j][0] - value[i][0], value[j][1] - value[i][1]
            loc1 = value[i]
            loc2 = value[j]
            if 0<=loc1[0]-diff[0]<len(ls) and 0<=loc1[1]-diff[1]<len(ls[0]) and ls[loc1[0]-diff[0]][loc1[1]-diff[1]] != key:
                ls[loc1[0]-diff[0]] = ls[loc1[0]-diff[0]][:loc1[1]-diff[1]] + '#' + ls[loc1[0]-diff[0]][loc1[1]-diff[1]+1:]
            if 0<=loc2[0]+diff[0]<len(ls) and 0<=loc2[1]+diff[1]<len(ls[0]) and ls[loc2[0]+diff[0]][loc2[1]+diff[1]] != key:
                ls[loc2[0]+diff[0]] = ls[loc2[0]+diff[0]][:loc2[1]+diff[1]] + '#' + ls[loc2[0]+diff[0]][loc2[1]+diff[1]+1:]
            if 0<=loc1[0]+diff[0]<len(ls) and 0<=loc1[1]+diff[1]<len(ls[0]) and ls[loc1[0]+diff[0]][loc1[1]+diff[1]] != key:
                ls[loc1[0]+diff[0]] = ls[loc1[0]+diff[0]][:loc1[1]+diff[1]] + '#' + ls[loc1[0]+diff[0]][loc1[1]+diff[1]+1:]
            if 0<=loc2[0]-diff[0]<len(ls) and 0<=loc2[1]-diff[1]<len(ls[0]) and ls[loc2[0]-diff[0]][loc2[1]-diff[1]] != key:
                ls[loc2[0]-diff[0]] = ls[loc2[0]-diff[0]][:loc2[1]-diff[1]] + '#' + ls[loc2[0]-diff[0]][loc2[1]-diff[1]+1:]

cnt = 0
for i in range(len(ls)):
    for j in range(len(ls[i])):
        if ls[i][j] == '#':
            cnt += 1


print(cnt)