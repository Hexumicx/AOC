s = input()
ss = ""
while s!="end":
    ss += s
    s = input()

instructions = ss.split(",")

box = [[] for i in range(256)]
for i in instructions:
    label = 0
    if('-' in i):
        pre, post = i.split("-")
    elif('=' in i):
        pre, post = i.split("=")
    else:
        print(i)
    for c in pre:
        label += ord(c)
        label *= 17
        label %= 256
    if('=' in i):
        found = False
        for idx in range(len(box[label])):
            if(box[label][idx][0] == pre):
                box[label][idx] = (pre, i[i.find('=') + 1])
                found = True
                break
        if(not found):
            box[label].append((pre, i[i.find('=') + 1]))
    elif('-' in i):
        for idx in range(len(box[label])):
            if(box[label][idx][0] == pre):
                box[label].pop(idx)
                break

total = 0
bbox = 1
for b in box:
    val = 1
    for item in b:
        total += val * int(item[1]) * bbox
        val += 1
    bbox += 1

for i in box:
    print(i)
print(total)

