a = input()
a = a.split(":")[1]
a = int(a.strip())
b = input()
b = b.split(":")[1]
b = int(b.strip())
c = input()
c = c.split(":")[1]
c = int(c.strip())
dump = input()
prog = input()
prog = prog.split(":")[1]
prog = prog.strip().split(",")

a = 247839653009594

it = 0
out = []
while True:
    if it>=len(prog):
        break
    opcode = int(prog[it])
    curoperand = prog[it+1]
    if curoperand=='4':
        combo = a
    elif curoperand=='5':
        combo = b
    elif curoperand=='6':
        combo = c
    else:
        combo = int(curoperand)   
    if opcode == 0:
        a = a//(2**combo)
    elif opcode == 1:
        b = b^int(curoperand)
    elif opcode == 2:
        b = combo%8
    elif opcode == 3:
        if a == 0:
            pass
        else:
            it = int(curoperand)
            continue
    elif opcode == 4:
        b = b^c
    elif opcode == 5:
        out.append(combo%8)
    elif opcode == 6:
        b = a//(2**combo)
    elif opcode == 7:
        c = a//(2**combo)
    print(opcode, curoperand, a, b, c)
    it+=2

for i in out:
    print(i,end=",")

        
    
