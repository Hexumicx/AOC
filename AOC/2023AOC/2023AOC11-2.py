import queue
m = []
s = input()
erow = []
ecol = []
row = 0
while s != "":
    if '#' not in s:
        erow.append(row)
    m.append(s)
    s = input()
    row += 1
for i in range(len(m[0])):
    add = True
    for j in range(len(m)):
        if m[j][i] == '#':
            add = False
            break
    if add:
        ecol.append(i)
gloc = []
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == '#':
            gloc.append((i, j))
for i in range(len(gloc)):
    distance = 0
    for row in erow:
        if gloc[i][0] > row:
            distance += 1
    if(distance>0):
        gloc[i] = ((gloc[i][0] + distance * 999999), gloc[i][1])
    distance = 0
    for col in ecol:
        if gloc[i][1] > col:
            distance += 1
    if(distance>0):
        gloc[i] = (gloc[i][0], (gloc[i][1] + distance * 999999))

distance = 0
for i in range(len(gloc)):
    for j in range(len(gloc)):
        if(i != j):
            distance += abs(gloc[i][0] - gloc[j][0]) + abs(gloc[i][1] - gloc[j][1])
print(distance/2)