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

vals = prog[::-1]
vals = [int(i) for i in vals]
vals = [2,4,1,1,7,5,4,0,0,3,1,6,5,5,3,0][::-1]
def evalstate(rega, regb, regc, idx):
    if idx == len(vals):
        return True
    regb = vals[idx]
    # 5 5
    regb = regb^6
    # 1 6
    rega *= 8
    # 0 3
    # 4 0
    done = False
    # print(i)
    matchs = set()
    for k in range(0,8):
        # guess a
        tempa = rega + k
        tempb = tempa%8
        tempb = tempb^1
        tempc = tempa//(2**tempb)
        # print(tempa,tempb,tempc, (tempc^tempb)%8, regb%8)
        if (tempc^tempb)%8 == regb%8:
            if evalstate(tempa, tempb^1, tempc, idx+1):
                return True
            else:
                continue
    return False
    
rega = 0
regb = 0
regc = 0
for idx, i in enumerate(vals):
    regb = i
    # 5 5
    regb = regb^6
    # 1 6
    rega *= 8
    # 0 3
    # 4 0
    done = False
    # print(i)
    matchs = set()
    for k in range(0,8):
        # guess a
        tempa = rega + k
        tempb = tempa%8
        tempb = tempb^1
        tempc = tempa//(2**tempb)
        # print(tempa,tempb,tempc, (tempc^tempb)%8, regb%8)
        if (tempc^tempb)%8 == regb%8:
            if evalstate(tempa, tempb^1, tempc, idx+1):
                done = True
                break   
    print(i,matchs)
    if done:
        rega = tempa
        regb = tempb
        regc = tempc
    #1 1
    regb = regb^1

print(rega)
    
    

        
    
