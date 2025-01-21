mp = {}
in_x = 0
in_y = 0
while True:
    x = input()
    if x=="": break
    x = x.split(":")
    mp[x[0]] = int(x[1].strip())
    if x[0][0] == "x":
        in_x += mp[x[0]] << int(x[0][1:])
    elif x[0][0] == "y":
        in_y += mp[x[0]] << int(x[0][1:])

target = in_x + in_y
targetbits = [0]*50
for i in range(50):
    targetbits[i] = (target >> i) & 1
print(targetbits)

import queue
q = queue.Queue()
ls = []
while True:
    x = input()
    if x=="": break
    ls.append((x,0))

def get_output(q, mp):
    last_clear = None
    failure = []
    while not q.empty():
        front = q.get()
        cur = front.split(" ")
        if front in failure:
            return 0
        if cur[0] not in mp or cur[2] not in mp:
            failure.append(front)
            q.put(front)
            continue
        failure = []
        if cur[1] == "AND":
            mp[cur[4]] = mp[cur[0]] & mp[cur[2]]
        elif cur[1] == "OR":
            mp[cur[4]] = mp[cur[0]] | mp[cur[2]]
        elif cur[1] == "XOR":
            mp[cur[4]] = mp[cur[0]] ^ mp[cur[2]]
    total = 0
    for key, value in mp.items():
        if key[0] == 'z':
            bit = int(key[1:])
            total += value << bit
    return total

target = [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0]
targetz= [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0]
for i in range(50):
    if target[i] != targetz[i]:
        print(i)

ans = ["hmt", "z18", "bfq", "z27", "z31", "hkh", "fjp", "bng"]
print(",".join(sorted(ans)))
