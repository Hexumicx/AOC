mp = {}
while True:
    x = input()
    if x=="": break
    x = x.split(":")
    mp[x[0]] = int(x[1].strip())

import queue
q = queue.Queue()
while True:
    x = input()
    if x=="": break
    q.put(x)

while not q.empty():
    front = q.get()
    cur = front.split(" ")
    if cur[0] not in mp or cur[2] not in mp:
        q.put(front)
        continue
    if cur[1] == "AND":
        mp[cur[4]] = mp[cur[0]] & mp[cur[2]]
    elif cur[1] == "OR":
        mp[cur[4]] = mp[cur[0]] | mp[cur[2]]
    elif cur[1] == "XOR":
        mp[cur[4]] = mp[cur[0]] ^ mp[cur[2]]
    
total = 0
zbits = [0]*50
for key, value in mp.items():
    if key[0] == 'z':
        bit = int(key[1:])
        zbits[bit] = value
        total += value << bit
print(zbits)

target = [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0]
targetz= [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0]
for i in range(50):
    if target[i] != targetz[i]:
        print(i)