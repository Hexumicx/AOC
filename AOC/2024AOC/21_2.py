from functools import cache
from itertools import permutations

ls = []
mp = {}
val = {
    "0": (0,1),
    "1": (1,0),
    "2": (1,1),
    "3": (1,2),
    "4": (2,0),
    "5": (2,1),
    "6": (2,2),
    "7": (3,0),
    "8": (3,1),
    "9": (3,2),
    "A": (0,2)
}
keys = {"^":(1,1), "v":(0,1), "<":(0,0), ">":(0,2), "A":(1,2)}
res = 0
mp = {}
import sys
from functools import cache
from itertools import permutations

def pad2(ls):
    sln = []
    s1 = pad1(ls)
    for i in s1:
        s2 = pad1(i)
        sln += s2
    return sln

def pad1(ls):
    # return string by user to pad1 that would result in ls
    keys = {"^":(1,1), "v":(0,1), "<":(0,0), ">":(0,2), "A":(1,2)}
    cur = (1,2)
    allsln = [""]
    for i in ls:
        q = queue.Queue()
        q.put((cur,""))
        goal = keys[i]
        sln = []
        while not q.empty():
            cur, path = q.get()
            if cur == (1,0):
                continue
            if cur[0]<0 or cur[0]>3 or cur[1]<0 or cur[1]>2:
                continue
            if cur == goal:
                sln.append(path+"A")
                continue
            if goal[0]<cur[0]:
                q.put(((cur[0]-1, cur[1]), path+"v"))
            if goal[0]>cur[0]:
                q.put(((cur[0]+1, cur[1]), path+"^"))
            if goal[1]<cur[1]:
                q.put(((cur[0], cur[1]-1), path+"<"))
            if goal[1]>cur[1]:
                q.put(((cur[0], cur[1]+1), path+">"))
        temp = []
        for i in sln:
            for j in allsln:
                temp.append(j+i)
        allsln = temp
        cur = goal
    return allsln

@cache
def findminlen(s, depth=25, cur=(1,2)):
    global keys
    dirs = {'^': (1, 0), '>': (0, 1), 'v': (-1, 0), '<': (0, -1)}
    if not s: return 0
    cx, cy = cur
    px, py = keys[s[0]]
    dx, dy = px-cx, py-cy

    buttons = '>'*dy + '<'*-dy + 'v'*-dx + '^'*dx
    if depth:
        perms = []
        for perm in set(permutations(buttons)):
            cx, cy = cur
            for button in perm:
                dx, dy = dirs[button]
                cx += dx
                cy += dy
                if (cx, cy) not in keys.values():
                    break
            else:
                perms.append(findminlen(perm+('A',), depth-1))
        minlen = min(perms)
    else:
        minlen = len(buttons)+1
    return minlen+findminlen(s[1:], depth, keys[s[0]])


import queue
total = 0
while True:
    x = input()
    if x=="": break
    cur = (0,2)
    allsln = [""]
    for ch in x:
        q = queue.Queue()
        q.put((cur, ""))
        sln = []
        goal = val[ch]
        while not q.empty():
            cur, path = q.get()
            if cur == (0,0):
                continue
            if cur[0]<0 or cur[0]>3 or cur[1]<0 or cur[1]>2:
                continue
            if cur == goal:
                sln.append(path+"A")
                continue
            if goal[0]<cur[0]:
                q.put(((cur[0]-1, cur[1]), path+"v"))
            if goal[0]>cur[0]:
                q.put(((cur[0]+1, cur[1]), path+"^"))
            if goal[1]<cur[1]:
                q.put(((cur[0], cur[1]-1), path+"<"))
            if goal[1]>cur[1]:
                q.put(((cur[0], cur[1]+1), path+">"))
        cur = goal
        temp = []
        for i in sln:
            for j in allsln:
                temp.append(j+i)
        allsln = temp
    minlen = 1e20
    minlen = min([findminlen(x, 24) for x in allsln])
    
    total += minlen*int(x[:len(x)-1])

print(total)
    
