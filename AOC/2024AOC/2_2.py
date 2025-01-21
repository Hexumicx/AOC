ls = []
while True:
    try:
        x = input()
        if x=='':
            break
        x = x.split()
        ls.append(x)
    except:
        break
for l in ls:
    for i in range(len(l)):
        l[i] = int(l[i])
count = 0
for l in ls:
    safe = False
    templ = l.copy()
    for i in range(len(l)):
        templ = l[0:i] + l[i+1:]
        cursafe = True
        inc = False
        if templ[1] > templ[0]:
            inc = True
        for i in range(1,len(templ)):
            if inc:
                if 1<=templ[i]-templ[i-1]<=3:
                    continue
                else:
                    cursafe = False
                    break
            else:
                if 1<=templ[i-1]-templ[i]<=3:
                    continue
                else:
                    cursafe = False
                    break
        if cursafe:
            safe = True
    inc = False
    cursafe = True
    if l[1] > l[0]:
        inc = True
    for i in range(1,len(l)):
        if inc:
            if 1<=l[i]-l[i-1]<=3:
                continue
            else:
                cursafe = False
                break
        else:
            if 1<=l[i-1]-l[i]<=3:
                continue
            else:
                cursafe = False
                break
    if cursafe:
        safe = True
    if safe:
        count += 1
print(count)