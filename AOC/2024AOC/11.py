x = input()
ls = x.split()
ls = [int(i) for i in ls]

mp = {}
for i in range(25):
    ls2 = []
    for stone in ls:
        if stone == 0:
            ls2.append(1)
        elif len(str(stone))%2 == 0:
            fhalf = int(str(stone)[:len(str(stone))//2])
            bhalf = int(str(stone)[len(str(stone))//2:])
            ls2.append(fhalf)
            ls2.append(bhalf)
        else:
            ls2.append(stone*2024)
    ls = ls2.copy()

    print(ls)  
print(len(ls))