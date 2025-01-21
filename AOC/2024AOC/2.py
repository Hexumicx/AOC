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
    inc = False
    safe = True
    if l[1] > l[0]:
        inc = True
    for i in range(1,len(l)):
        if inc:
            if 1<=l[i]-l[i-1]<=3:
                continue
            else:
                safe = False
                break
        else:
            if 1<=l[i-1]-l[i]<=3:
                continue
            else:
                safe = False
                break
    if safe:
        count += 1
print(count)