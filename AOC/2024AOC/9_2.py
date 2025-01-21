import queue
with open('txt.txt') as f:
    ln = f.readlines()[0]
mxlen = 0
for idx, i in enumerate(ln):
    if idx%2==0:
        mxlen += int(i)

lastval = (len(ln))//2
q = queue.Queue()
for i in range(len(ln)-1, -1, -1):
    if i%2==1: continue
    q.put((int(ln[i]), i//2))


cur = 0
taken = 0
checksum = 0
ival = 0
visited = {}
for idx, val in enumerate(ln):
    if idx%2==0:
        if visited.get(idx//2, False) == True:
            ival += int(val)
            continue
        visited[idx//2] = True
        checksum += (((ival+int(val))*(ival+int(val)-1))/2 - (ival*(ival-1))/2) * int(idx//2)
        ival += int(val)
    else:
        tempq = queue.Queue()
        while not q.empty():
            num, v = q.get()
            if num <= int(val):
                if v in visited:
                    continue
                checksum += (((ival+num)*(ival+num-1))/2 - ((ival)*(ival-1))/2) * v
                ival += num
                val = str(int(val) - num)
                visited[v] = True
            else:
                tempq.put((num, v))
        ival += int(val)
        q = tempq

print(int(checksum))
