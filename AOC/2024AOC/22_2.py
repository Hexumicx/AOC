total = 0
cycles = 1999
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
        for j in range(3):
            arr[j] = arr[j+1]
        arr[3] = x%10-prev
        prev = x%10
        if (arr[0],arr[1],arr[2],arr[3]) in mp:
            pass
        elif i>=3:
            mp[(arr[0],arr[1],arr[2],arr[3])] = x%10
    for key, value in mp.items():
        mpp[key] = mpp.get(key,0) + value

mx = 0
ans = 0
for key, value in mpp.items():
    if value > mx:
        mx = value
        ans = key
print(ans, mx)