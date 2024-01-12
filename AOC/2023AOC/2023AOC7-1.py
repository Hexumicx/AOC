hand = []
s = input()
while(s!="end"):
    h, p = s.strip().split(" ")
    hand.append((h,int(p)))
    s = input()

preproc = []
point = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
point = point[::-1]
def sortkey(x):
    totalpoint = 0
    totalpoint += x[2]
    for i in x[0]:
        totalpoint *= 100
        totalpoint += point.index(i)
    return totalpoint

for h, p in hand:
    d = {}
    for c in h:
        d[c] = d.get(c,0)+1
    if len(d) == 1:
        preproc.append((h,p,7))
    elif len(d) == 2:
        for key, value in d.items():
            if value == 4:
                preproc.append((h,p,6))
                break
            elif value == 2:
                preproc.append((h,p,5))
                break
    elif len(d) == 3:
        for key, value in d.items():
            if value == 3:
                preproc.append((h,p,4))
                break
            elif value == 2:
                preproc.append((h,p,3))
                break
    elif len(d) == 4:
        preproc.append((h,p,2))
    else:
        preproc.append((h,p,1))
preproc = sorted(preproc, key=sortkey)
print(preproc)
total = 0
idx = 1
for h, p, _ in preproc:
    total += p*idx
    idx += 1
print(total)





