lsl = []
lsr = []
while True:
    try:
        n = input()
        if n == "":
            break
        n1, n2 = n.split()[0], n.split()[-1]
        lsl.append(int(n1))
        lsr.append(int(n2))
    except:
        break

lsl = sorted(lsl)
lsr = sorted(lsr)
dist = 0
for i, j in zip(lsl, lsr):
    dist += abs(i - j)
print(dist)