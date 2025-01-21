ls = []
while True:
    s = input()
    if s == '':
        break
    ls.append(s)

count = 0
for i in range(len(ls)):
    for j in range(len(ls[0])):
        if ls[i][j] == 'X':
            for c in [(1,1), (-1,-1), (-1,1),(1,-1),(0,1), (1,0), (0,-1),(-1,0)]:
                if 0 <= i+c[0] < len(ls) and 0 <= j+c[1] < len(ls[0]):
                    if ls[i+c[0]][j+c[1]] == 'M':
                        if 0 <= i+2*c[0] < len(ls) and 0 <= j+2*c[1] < len(ls[0]):
                            if ls[i+2*c[0]][j+2*c[1]] == 'A':
                                if 0 <= i+3*c[0] < len(ls) and 0 <= j+3*c[1] < len(ls[0]):
                                    if ls[i+3*c[0]][j+3*c[1]] == 'S':
                                        count += 1
                                        continue

print(count)            