total = 0
sizex = 101
sizey = 103
ls = [0,0,0,0]
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
    iter = 100
    finalloc = (loc[0]+velo[0]*iter, loc[1]+velo[1]*iter)
    finalloc = [finalloc[0]%sizex, finalloc[1]%sizey]
    if finalloc[0] == sizex//2 or finalloc[1] == sizey//2:
        pass
    else:
        if finalloc[0] < sizex//2 and finalloc[1] < sizey//2:
            ls[0] += 1
        elif finalloc[0] < sizex//2 and finalloc[1] > sizey//2:
            ls[1] += 1
        elif finalloc[0] > sizex//2 and finalloc[1] < sizey//2:
            ls[2] += 1
        elif finalloc[0] > sizex//2 and finalloc[1] > sizey//2:
            ls[3] += 1

print(ls)
total = ls[0]*ls[3]*ls[1]*ls[2]
print(total)