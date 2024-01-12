seedsoil=[]
soilfert=[]
fertwater=[]
waterlight=[]
lighttemp=[]
temphumid=[]
humidloca=[]

print("seedsoil:")
s = input()
s = input()
while(s != ""):
    source, dest, r = s.split(" ")
    seedsoil.append((int(source), int(dest), int(r)))
    s = input()

print("soilfert:")
s = input()
s = input()
while(s != ""):
    source, dest, r = s.split(" ")
    soilfert.append((int(source), int(dest), int(r)))
    s = input()

print("fertwater:")
s = input()
s = input()
while(s != ""):
    source, dest, r = s.split(" ")
    fertwater.append((int(source), int(dest), int(r)))
    s = input()

print("waterlight:")
s = input()
s = input()
while(s != ""):
    source, dest, r = s.split(" ")
    waterlight.append((int(source), int(dest), int(r)))
    s = input()

print("lighttemp:")
s = input()
s = input()
while(s != ""):
    source, dest, r = s.split(" ")
    lighttemp.append((int(source), int(dest), int(r)))
    s = input()

print("temphumid:")
s = input()
s = input()
while(s != ""):
    source, dest, r = s.split(" ")
    temphumid.append((int(source), int(dest), int(r)))
    s = input()

print("humidloca:")
s = input()
s = input()
while(s != ""):
    source, dest, r = s.split(" ")
    humidloca.append((int(source), int(dest), int(r)))
    s = input()

print("seed")
s = input()
seed = s.split(" ")
minval = 1e9
for i in range(len(seed)):
    curval = int(seed[i])
    for j in seedsoil:
        if(int(seed[i])>=j[1] and int(seed[i])<=j[1]+j[2]):
            curval = j[0] + int(seed[i])-j[1]
            break
    print(curval)
    for j in soilfert:
        if(curval>=j[1] and curval<=j[1]+j[2]):
            curval = j[0] + curval-j[1]
            break
    print(curval)
    for j in fertwater:
        if(curval>=j[1] and curval<=j[1]+j[2]):
            curval = j[0] + curval-j[1]
            break
    print(curval)
    for j in waterlight:
        if(curval>=j[1] and curval<=j[1]+j[2]):
            curval = j[0] + curval-j[1]
            break
    print(curval)
    for j in lighttemp:
        if(curval>=j[1] and curval<=j[1]+j[2]):
            curval = j[0] + curval-j[1]
            break
    print(curval)
    for j in temphumid:
        if(curval>=j[1] and curval<=j[1]+j[2]):
            curval = j[0] + curval-j[1]
            break
    print(curval)
    for j in humidloca:
        if(curval>=j[1] and curval<=j[1]+j[2]):
            curval = j[0] + curval-j[1]
            break
    print(curval)
    minval = min(minval, curval)
print(minval)
    