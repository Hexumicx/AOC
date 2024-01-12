import queue
m = []
s = input()
while s != "":
    if '#' not in s:
        m.append(s)
    m.append(s)
    s = input()
m2 = m.copy()
added = 0
for i in range(len(m[0])):
    add = True
    for j in range(len(m)):
        if m[j][i] == '#':
            add = False
            break
    if add:
        for j in range(len(m)):
            m2[j] = m2[j][:i+added] + '.' + m2[j][i+added:]
        added += 1

gloc = []
for i in range(len(m2)):
    for j in range(len(m2[0])):
        if m2[i][j] == '#':
            gloc.append((i, j))

distance = 0
for i in range(len(gloc)):
    for j in range(len(gloc)):
        if(i != j):
            distance += abs(gloc[i][0] - gloc[j][0]) + abs(gloc[i][1] - gloc[j][1])
print(distance/2)
