total = 0
cycles = 2000
mpp = {}
while True:
    x = input()
    if x =="": break
    x = int(x)
    prev = x%10
    arr = [0,0,0,0]
    mp = {}
    for i in range(cycles):
        num1 = x * 64
        x = num1 ^ x
        x = x % 16777216
        num2 = x // 32
        x = x ^ num2
        x = x % 16777216
        num3 = x*2048
        x = num3 ^ x
        x = x % 16777216
    total += x
   
print(total)