lsl = []
lsr = []
while True:
    try:
        n = input()
        if n == "":
            break
        n1, n2 = n.split()[0], n.split()[-1]
        lsl.append(int(n1))
        lsr.append(int(n2))
    except:
        break

mp = {}
for i in lsr:
    if i in mp:
        mp[i] += 1
    else:
        mp[i] = 1
dist = 0
for i in lsl:
    dist += mp.get(i, 0)*i
print(dist)