from queue import Queue
s = input()
m = {}
states = {}
while s != '':
    inp, output = s.split(' -> ')
    output = output.split(', ')
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

on = 0
off = 0
for times in range(1000):
    q = Queue()
    for i in start:
        q.put((i, False))
    off += len(start)+1
    while not q.empty():
        cur, state = q.get()
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

print(on, off)
print(on*off)
    

