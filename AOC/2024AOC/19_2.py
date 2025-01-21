ls = []
x = input()
x = x.split(",")
for i in range(len(x)):
    x[i] = x[i].strip()
ls = x
ls = tuple(ls)
input()
print(ls)

mp = {}
cnt = 0
def possible(ls, x):
    global mp
    global cnt
    if x == '':
        return 1
    p = False
    temp = 0
    for colour in ls:
        if len(x) < len(colour):
            continue
        if x[:len(colour)] == colour:
            if (ls, x[len(colour):]) in mp:
                temp += mp[(ls, x[len(colour):])]
            else:
                t = possible(ls, x[len(colour):])
                mp[(ls, x[len(colour):])] = t
                temp += t
    return temp

cnt = 0
while True:
    x = input()
    if x == '':
        break
    cnt += possible(ls, x)
    # print(cnt)


print(cnt)