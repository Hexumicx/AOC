ls = {}
while True:
    x = input()
    if x == '': break
    x = x.split("-")
    if x[0] not in ls:
        ls[x[0]] = set()
        ls[x[0]].add(x[1])
    else:
        ls[x[0]].add(x[1])
    if x[1] not in ls:
        ls[x[1]] = set()
        ls[x[1]].add(x[0])
    else:  
        ls[x[1]].add(x[0])

lans = set()
for key in ls.keys():
    neighbors = ls[key]
    for neighbor in neighbors:
        neighbors2 = ls[neighbor]
        for neighbor2 in neighbors2:
            if neighbor2 in neighbors:
                lans.add(tuple(sorted([key, neighbor, neighbor2])))

res = 0
for lan in lans:
    if lan[0][0] =="t" or lan[1][0] =="t" or lan[2][0] =="t":
        res += 1
print(res)