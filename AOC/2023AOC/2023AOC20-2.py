from queue import Queue
import math
s = input()
m = {}
states = {}
rx = []
while s != '':
    inp, output = s.split(' -> ')
    output = output.split(', ')
    if 'rx' in output:
        rx.append(inp[1:])
    if inp == 'broadcaster':
        start = output
    else:
        m[inp[1:]] = (inp[0], output, False)
        if inp[0] == '&':
            states[inp[1:]] = {}
    s = input()
for j, i in m.items():
    for v in i[1]:
        if(m.get(v)!=None and m[v][0] == '&'):
            states[v][j] = False

q = Queue()
rxset = set()
for i in rx:
    q.put(i)
while not q.empty():
    cur = q.get()
    if cur in rxset:
        continue
    rxset.add(cur)
    for key, value in m.items():
        if cur in value[1]:
            q.put(key)

rxdict = {'gt': -1, 'vr': -1, 'nl': -1, 'lr':-1}

on = 0
off = 0
for times in range(1,100000):
    q = Queue()
    for i in start:
        q.put((i, False))
    off += len(start)+1
    while not q.empty():
        cur, state = q.get()
        if rxdict.get(cur) == -1 and state==False:
            rxdict[cur] = times
        if m.get(cur) == None:
            continue
        if m[cur][0] == "%":
            if not state:
                m[cur] = (m[cur][0], m[cur][1], not m[cur][2])
                for i in m[cur][1]:
                    q.put((i, m[cur][2]))
                    if(states.get(i)!=None):
                        states[i][cur] = m[cur][2]
                    if m[cur][2]:
                        on += 1
                    else:
                        off += 1
            else:
                continue
        elif m[cur][0] == "&":
            for i in states[cur].values():
                if i==False:
                    m[cur] = (m[cur][0], m[cur][1], True)
                    break
                else:
                    m[cur] = (m[cur][0], m[cur][1], False)
            for i in m[cur][1]:
                q.put((i, m[cur][2]))
                if(states.get(i)!=None):
                    states[i][cur] = m[cur][2]
                if m[cur][2]:
                    on += 1
                else:
                    off += 1

res = 1
for i in rxdict.values():
    res = math.lcm(res, i)

print(rxdict)
print(res)
    

