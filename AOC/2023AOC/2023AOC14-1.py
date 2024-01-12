s=input()
m = []
while s != "end":
    m.append(list(s))
    s = input()

total = 0
for i in range(len(m[0])):
    val = len(m)
    for j in range(len(m)):
        if m[j][i] == "O":
            total += val
            val -= 1
        if m[j][i] == "#":
            val = len(m)-j-1
print(total)