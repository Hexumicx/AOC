res = 0
import numpy as np
import re
while True:
    a = input()
    if a == '':
        break
    a = re.findall(r"\d+", a)
    b = input()
    b = re.findall(r"\d+", b)
    prize = input()
    prize = re.findall(r"\d+", prize)
    out = False
    a = [int(x) for x in a]
    b = [int(x) for x in b]
    prize = [int(x) for x in prize]
    prize = [int(prize[0]+10**13), int(prize[1]+10**13)]
    e1 = [a[0], b[0], prize[0]]
    e2 = [a[1], b[1], prize[1]]
    mult1 = [e1[1], e2[1]]
    e1 = [e1[0]*mult1[1], e1[1]*mult1[1], e1[2]*mult1[1]]
    e2 = [e2[0]*mult1[0], e2[1]*mult1[0], e2[2]*mult1[0]]
    out = [e1[0]-e2[0], e1[1]-e2[1], e1[2]-e2[2]]
    if out[2] % out[0] == 0:
        i = out[2] // out[0]
        if (prize[0]-a[0]*i) % b[0] == 0: 
            j = (prize[0] - a[0]*i) // b[0]
            if i<0 or j<0:
                continue
            res += 3*i + j

    dump = input()
print(res)