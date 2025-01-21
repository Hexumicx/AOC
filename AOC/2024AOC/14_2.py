total = 0
sizex = 101
sizey = 103
ls = [0,0,0,0]
mapp = [[0 for i in range(sizey)] for j in range(sizex)]
import queue
q  = queue.Queue()
while True:
    n = input()
    if n=="": break
    loc, velo = n.split(' ')
    loc = loc.split("=")[1]
    loc = loc.split(",")
    loc = [int(i) for i in loc]
    velo = velo.split("=")[1]
    velo = velo.split(",")
    velo = [int(i) for i in velo]
    mp = {}
    mapp[loc[0]][loc[1]] += 1
    q.put((loc[0],loc[1],velo[0],velo[1]))
step = 0
basefile = "14_2"
while True:
    mapp2 = [[0 for i in range(sizey)] for j in range(sizex)]
    q2 = queue.Queue()
    while(not q.empty()):
        locx, locy, velox, veloy = q.get()
        finalloc = (locx+velox, locy+veloy)
        finalloc = [finalloc[0]%sizex, finalloc[1]%sizey]
        mapp2[finalloc[0]][finalloc[1]] += 1
        q2.put((finalloc[0],finalloc[1],velox,veloy))
    q = q2
    mapp = mapp2
    step += 1
    toprint = False
    mxcnt = 0
    for i in range(sizey):
        cnt = 0
        for j in range(sizex-1):
            if mapp[j][i] == mapp[j+1][i] == 1:
                cnt += 1
                mxcnt = max(mxcnt, cnt)
        if mxcnt > 10:
            toprint = True
            break
    if toprint:
        with open(basefile+str(step)+".txt", "w") as f:
            for i in range(sizex):
                for j in range(sizey):
                    if mapp[i][j] > 0:
                        f.write("#")
                    else:
                        f.write(" ")
                f.write("\n")
