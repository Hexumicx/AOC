mapp = []
while True:
    x = input()
    if x == '': break
    x = list(x)
    mapp.append(x)

commands = []
while True:
    x = input()
    if x == '': break
    x.replace('\n', '')
    commands+=list(x)

for i in range(len(mapp)):
    for j in range(len(mapp[i])):
        if mapp[i][j] == '@':
            x, y = i, j


def mov(x, y, move):
    global mapp
    # print(x, y, move)  
    if x<0 or y<0 or x>=len(mapp) or y>=len(mapp[0]):
        return False
    if move == '<':
        if 0 < y-1 < len(mapp[0]) and mapp[x][y-1] == '#':
            return False
        elif 0 < y-1 < len(mapp[0]) and mapp[x][y-1] == '.':
            mapp[x][y-1] = mapp[x][y]
            mapp[x][y] = '.'
            return True
        else:
            if mov(x, y-1, move):
                mapp[x][y-1] = mapp[x][y]
                mapp[x][y] = '.'
                return True
            else:
                return False
    elif move == '>':
        if 0 < y+1 < len(mapp[0]) and mapp[x][y+1] == '#':
            return False
        elif 0 < y+1 < len(mapp[0]) and mapp[x][y+1] == '.':
            mapp[x][y+1] = mapp[x][y]
            mapp[x][y] = '.'
            return True
        else:
            if mov(x, y+1, move):
                mapp[x][y+1] = mapp[x][y]
                mapp[x][y] = '.'
                return True
            else:
                return False
    elif move == "^":
        if 0<x-1<len(mapp) and mapp[x-1][y] == '#':
            return False
        elif 0<x-1<len(mapp) and mapp[x-1][y] == '.':
            mapp[x-1][y] = mapp[x][y]
            mapp[x][y] = '.'
            return True
        else:
            if mov(x-1, y, move):
                mapp[x-1][y] = mapp[x][y]
                mapp[x][y] = '.'
                return True
            else:
                return False
    elif move == "v":
        if 0<x+1<len(mapp) and mapp[x+1][y] == '#':
            return False
        elif 0<x+1<len(mapp) and mapp[x+1][y] == '.':
            mapp[x+1][y] = mapp[x][y]
            mapp[x][y] = '.'
            return True
        else:
            if mov(x+1, y, move):
                mapp[x+1][y] = mapp[x][y]
                mapp[x][y] = '.'
                return True
            else:
                return False
    
for move in commands:
    if mov(x, y, move):
        if move == '<':
            y-=1
        elif move == '>':
            y+=1
        elif move == '^':
            x-=1
        elif move == 'v':
            x+=1

v = 0
for i in range(len(mapp)):
    for j in range(len(mapp[i])):
        if mapp[i][j] == 'O':
            v += i*100 + j

print(v)