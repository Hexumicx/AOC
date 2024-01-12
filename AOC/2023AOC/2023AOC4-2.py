s = ""
ls = [1]*208
total = 0
curcard = 0
while(s.strip()!="end"):
    s = input()
    curcard += 1
    if s.strip() == "end":
        break
    card, nums = s.split(":")
    numcard, numcheck = nums.split("|")
    numcard = numcard.strip().split(" ")
    numcheck = numcheck.strip().split(" ")     
    correct = 0
    for i in numcard:
        if i=='':
            continue
        if i in numcheck:
            correct += 1
    print(correct)
    for i in range(1,correct+1):
        ls[curcard+i] += ls[curcard]
    total+=ls[curcard]
    
print(total)
    
