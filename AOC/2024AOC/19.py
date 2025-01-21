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
def possible(ls, x):
    global mp
    if x == '':
        return True
    p = False
    for colour in ls:
        if len(x) < len(colour):
            continue
        if x[:len(colour)] == colour:
            if (ls, x[len(colour):]) in mp:
                p = p or mp[(ls, x[len(colour):])]
            else:
                temp = possible(ls, x[len(colour):])
                mp[(ls, x[len(colour):])] = temp
                p = p or temp
        else:
            p = p or False
    return p

cnt = 0
while True:
    x = input()
    if x == '':
        break
    if possible(ls, x):
        cnt += 1

print(cnt)