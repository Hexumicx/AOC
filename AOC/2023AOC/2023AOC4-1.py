s = ""
total = 0
while(s.strip()!="end"):
    s = input()
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
    if correct > 0:
        total += 2**(correct-1)
print(total)
    
