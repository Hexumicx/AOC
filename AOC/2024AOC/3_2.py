import re
s=""
while True:
    try:
        x = input()
        if x=='':
            break
        s += x
    except:
        break
pattern = r"(mul\(\d+,\d+\)|don't\(\)|do\(\))"
ls = re.findall(pattern, s)
print(ls)
val = 0
enable = True
for l in ls:
    if l == "do()":
        enable = True
        continue
    if l == "don't()":
        enable = False
        continue
    if enable:
        s = l.split("(")[1].split(")")[0]
        n1, n2 = s.split(",")
        n1, n2 = int(n1), int(n2)
        val += n1*n2

print(val)
