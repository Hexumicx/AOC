keys = []
locks = []
while True:
    ls = []
    while True:
        x = input()
        if x == "": break
        ls.append(x)
    if ls == []: break
    if ls[0] == "#####":
        lock = [0,0,0,0,0]
        for i in range(len(ls)):
            for j in range(len(ls[i])):
                if i==0 or i==len(ls)-1:
                    continue
                if ls[i][j] == '#':
                    lock[j] += 1
        locks.append(lock)
    elif ls[0] == ".....":
        key = [0,0,0,0,0]
        for i in range(len(ls)):
            for j in range(len(ls[i])):
                if i==0 or i==len(ls)-1:
                    continue
                if ls[i][j] == '#':
                    key[j] += 1
        keys.append(key)


cnt = 0
for key in keys:
    for lock in locks: 
        fail = False
        for i in range(5):
            if key[i] + lock[i] >= 6:
                fail = True
        if not fail:
            cnt += 1

print(cnt)