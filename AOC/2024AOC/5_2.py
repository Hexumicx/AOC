mp = {}
rmp = {}
while True:
    x = input()
    if x == "":
        break
    f,b = x.split("|")
    if f not in mp.keys():
        mp[f] = [b]
    else:
        mp[f].append(b)
    if b not in rmp.keys():
        rmp[b] = [f]
    else:  
        rmp[b].append(f)

ls = []
cnt = 0

while True:
    x = input()
    if x == "":
        break
    x = x.split(",")
    printed = {}
    fail = False
    for val in x:
        if val not in rmp.keys():
            printed[val] = True
            continue
        for i in rmp[val]:
            if i not in x:
                continue
            if printed.get(i,False) == False:
                fail = True
                break
        if not fail:
            printed[val] = True
        else:
            break
    xx = []
    if fail == True:
        printed = {}
        idx = 0
        while idx<=len(x)-1:
            fail = False
            ll = rmp.get(x[idx],[])
            for j in ll:
                if j not in x:
                    continue
                if printed.get(j,False) == False:
                    fail = True
                    break
            if not fail:
                printed[x[idx]] = True
                xx.append(x[idx])
                x.remove(x[idx])
                idx = -1
            idx += 1
        cnt += int(xx[len(xx)//2])
print(cnt)
