from copy import deepcopy
s=input()
m = []
while s != "end":
    m.append(list(s))
    s = input()
first = False
for i in range(1000):
    for i in range(len(m[0])): #N
        val = len(m)
        for j in range(len(m)):
            if m[j][i] == "O":
                m[j][i] = '.'
                m[len(m)-val][i] = 'O'
                val -= 1
            if m[j][i] == "#":
                val = len(m)-j-1
    for i in range(len(m)): #W
        val = len(m[0])
        for j in range(len(m[0])):
            if m[i][j] == "O":
                m[i][j] = '.'
                m[i][len(m[0])-val] = 'O'
                val -= 1
            if m[i][j] == "#":
                val = len(m[0])-j-1
    for i in range(len(m[0])): #S
        val = 1
        for j in range(len(m)-1,-1,-1):
            if m[j][i] == "O":
                m[j][i] = '.'
                m[len(m[0])-val][i] = 'O'
                val += 1
            if m[j][i] == "#":
                val = len(m)-j+1
    for i in range(len(m)): #E
        val = 1
        for j in range(len(m[0])-1,-1,-1):
            if m[i][j] == "O":
                m[i][j] = '.'
                m[i][len(m[0])-val] = 'O'
                val += 1
            if m[i][j] == "#":
                val = len(m[0])-j+1

total = 0
val = len(m[0])
for i in range(len(m)):
    for j in range(len(m[0])):
        if(m[i][j] == "O"):
            total += val
    val -= 1

print(total)