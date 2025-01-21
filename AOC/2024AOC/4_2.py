ls = []
while True:
    s = input()
    if s == '':
        break
    ls.append(s)

count = 0
for i in range(len(ls)):
    for j in range(len(ls[0])):
        if ls[i][j] == 'A':
            if 0 <= i-1 < len(ls) and 0 <= j-1 < len(ls[0]) and ls[i-1][j-1] == 'M':
                if 0 <= i+1 < len(ls) and 0 <= j+1 < len(ls[0]) and ls[i+1][j+1] == 'S':
                    if 0<=i-1<len(ls) and 0<=j+1<len(ls[0]) and ls[i-1][j+1] == 'M':
                        if 0<=i+1<len(ls) and 0<=j-1<len(ls[0]) and ls[i+1][j-1] == 'S':
                            count += 1
                    elif 0<=i-1<len(ls) and 0<=j+1<len(ls[0]) and ls[i-1][j+1] == 'S':
                        if 0<=i+1<len(ls) and 0<=j-1<len(ls[0]) and ls[i+1][j-1] == 'M':
                            count += 1
            elif 0 <= i-1 < len(ls) and 0 <= j-1 < len(ls[0]) and ls[i-1][j-1] == 'S':
                if 0 <= i+1 < len(ls) and 0 <= j+1 < len(ls[0]) and ls[i+1][j+1] == 'M':
                    if 0<=i-1<len(ls) and 0<=j+1<len(ls[0]) and ls[i-1][j+1] == 'M':
                        if 0<=i+1<len(ls) and 0<=j-1<len(ls[0]) and ls[i+1][j-1] == 'S':
                            count += 1
                    elif 0<=i-1<len(ls) and 0<=j+1<len(ls[0]) and ls[i-1][j+1] == 'S':
                        if 0<=i+1<len(ls) and 0<=j-1<len(ls[0]) and ls[i+1][j-1] == 'M':
                            count += 1
print(count)            