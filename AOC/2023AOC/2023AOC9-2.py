s = input()
total = 0
while s != "end":
    stepsls = []
    ls = s.strip().split(' ')
    for i in range(len(ls)):
        ls[i] = int(ls[i])
    ls.reverse()
    stepsls.append(ls)
    found = False
    while not found:
        nxtls = []
        for i in range(len(stepsls[-1])-1):
            nxtls.append(stepsls[-1][i+1]-stepsls[-1][i])
        stepsls.append(nxtls)
        if stepsls[-1] == [0]*len(stepsls[-1]):
            found = True
    stepsls[-1].append(0)
    for i in range(len(stepsls)-2,-1,-1):
        stepsls[i].append(stepsls[i+1][-1]+stepsls[i][-1])
    total += stepsls[0][-1]
    s = input()
print(total)
