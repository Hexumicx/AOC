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
pattern = r"mul\(\d+,\d+\)"
ls = re.findall(pattern, s)
val = 0
for l in ls:
    s = l.split("(")[1].split(")")[0]
    n1, n2 = s.split(",")
    n1, n2 = int(n1), int(n2)
    val += n1*n2

print(val)
