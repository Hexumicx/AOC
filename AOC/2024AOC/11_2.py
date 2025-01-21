x = input()
ls = x.split()
ls = [int(i) for i in ls]

mp = {}
for stone in ls:
    mp[stone] = 1
for i in range(75):
    mp2 = {}
    for stone, counts in mp.items():
        if stone == 0:
            if mp2.get(1)==None:
                mp2[1] = counts
            else:
                mp2[1] += counts
        elif len(str(stone))%2 == 0:
            fhalf = int(str(stone)[:len(str(stone))//2])
            bhalf = int(str(stone)[len(str(stone))//2:])
            if mp2.get(fhalf)==None:
                mp2[fhalf] = counts
            else:
                mp2[fhalf] += counts
            if mp2.get(bhalf)==None:
                mp2[bhalf] = counts
            else:
                mp2[bhalf] += counts
        else:
            if mp2.get(stone*2024)==None:
                mp2[stone*2024] = counts
            else:
                mp2[stone*2024] += counts
    mp = mp2.copy()

cnts = 0
for i in mp.values():
    cnts += i
print(cnts)