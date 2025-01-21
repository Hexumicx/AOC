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
    for j in range(int(ln[i])):
        q.put(i//2)


cur = 0
taken = 0
checksum = 0
ival = 0
for idx, val in enumerate(ln):
    if idx%2==0:
        for j in range(int(val)):
            checksum += int(idx//2)*ival
            ival += 1
            if ival == mxlen:
                break
    else:
        for j in range(int(val)):
            v = q.get()
            checksum += v*ival
            ival += 1
            if ival == mxlen:
                break
    if ival == mxlen:
        break

print(checksum)
