s = input()
ss = ""
while s!="end":
    ss += s
    s = input()

instructions = ss.split(",")


res = 0
for i in instructions:
    total = 0
    for c in i:
        total += ord(c)
        total *= 17
        total %= 256
    res += total

print(res)