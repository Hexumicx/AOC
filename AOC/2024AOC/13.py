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
    for i in range(100):
        for j in range(100):
            if int(b[0])*i + int(a[0])*j == int(prize[0]) and int(b[1])*i + int(a[1])*j == int(prize[1]):
                res += 3*j + i
                out = True
                break
        if out: break

    dump = input()
print(res)