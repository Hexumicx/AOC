ls = []
def rec(tar, ls, cur = -1):
    if len(ls) == 0:
        if cur == tar:
            return True
        else:
            return False
    if cur == -1:
        return rec(tar, ls[1:], ls[0])
    else:
        return rec(tar, ls[1:], cur*ls[0]) or rec(tar, ls[1:], cur+ls[0]) or rec(tar, ls[1:], int(str(cur)+str(ls[0])))
        
res = 0
while True:
    x = input()
    if x == "":
        break
    total, rest = x.split(":")
    total = int(total)
    rest = rest.strip().split(" ")
    rest = [int(i) for i in rest]
    if rec(int(total), rest, -1)==True:
        res += int(total)

print(res)
    