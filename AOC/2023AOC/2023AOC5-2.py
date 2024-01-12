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
seedstart = []
for i in range(0,len(seed),2):
    seedstart.append(("ss",int(seed[i]), int(seed[i])+int(seed[i+1])))
for str, start, end in seedstart:
        print(str, start, end)
        curval = start
        for j in seedsoil:
            if(str!="ss"):
                break
            if(start>=j[1] and start<=j[1]+j[2]):
                start = j[0] + start-j[1]
                if(end>=j[1] and end<=j[1]+j[2]):
                    end = j[0] + end-j[1]
                else:
                    seedstart.append(("ss",j[1]+j[2]+1, end))
                    end = j[0] + j[2]
                str = "sf"
                break
            if(end>=j[1] and end<=j[1]+j[2]):
                end = j[0] + end-j[1]
                seedstart.append(("ss",start, j[1]-1))
                start = j[0]
                str = "sf"
                break
            if(start<j[1] and end>j[1]+j[2]):
                seedstart.append(("ss",start, j[1]-1))
                start = j[0]
                seedstart.append(("ss",j[1]+j[2]+1, end))
                end = j[0] + j[2]
                str = "sf"
                break
            if(j==seedsoil[-1] and str=="ss"):
                str = "sf"
                break
        print(str, start, end)    
        for j in soilfert:
            if(str!="sf"):
                break
            if(start>=j[1] and start<=j[1]+j[2]):
                start = j[0] + start-j[1]
                if(end>=j[1] and end<=j[1]+j[2]):
                    end = j[0] + end-j[1]
                else:
                    seedstart.append(("sf", j[1]+j[2]+1, end))
                    end = j[0] + j[2]
                str = "fw"
                break
            if(end>=j[1] and end<=j[1]+j[2]):
                end = j[0] + end-j[1]
                seedstart.append(("sf",start, j[1]-1))
                start = j[0]
                str = "fw"
                break
            if(start<j[1] and end>j[1]+j[2]):
                seedstart.append(("sf",start, j[1]-1))
                start = j[0]
                seedstart.append(("sf",j[1]+j[2]+1, end))
                end = j[0] + j[2]
                str = "fw"
                break
            if(j==soilfert[-1] and str=="sf"):
                str = "fw"
                break
        print(str, start, end)
        for j in fertwater:
            if(str!="fw"):
                break
            if(start>=j[1] and start<=j[1]+j[2]):
                start = j[0] + start-j[1]
                if(end>=j[1] and end<=j[1]+j[2]):
                    end = j[0] + end-j[1]
                else:
                    seedstart.append(("fw", j[1]+j[2]+1, end))
                    end = j[0] + j[2]
                str = "wl"
                break
            if(end>=j[1] and end<=j[1]+j[2]):
                end = j[0] + end-j[1]
                seedstart.append(("fw",start, j[1]-1))
                start = j[0]
                str = "wl"
                break
            if(start<j[1] and end>j[1]+j[2]):
                seedstart.append(("fw",start, j[1]-1))
                start = j[0]
                seedstart.append(("fw",j[1]+j[2]+1, end))
                end = j[0] + j[2]
                str = "wl"
                break
            if(j==fertwater[-1] and str=="fw"):
                str = "wl"
                break
        print(str, start, end)
        for j in waterlight:
            if(str!="wl"):
                break
            if(start>=j[1] and start<=j[1]+j[2]):
                start = j[0] + start-j[1]
                if(end>=j[1] and end<=j[1]+j[2]):
                    end = j[0] + end-j[1]
                else:
                    seedstart.append(("wl", j[1]+j[2]+1, end))
                    end = j[0] + j[2]
                str = "lt"
                break
            if(end>=j[1] and end<=j[1]+j[2]):
                end = j[0] + end-j[1]
                seedstart.append(("wl",start, j[1]-1))
                start = j[0]
                str = "lt"
                break
            if(start<j[1] and end>j[1]+j[2]):
                seedstart.append(("wl",start, j[1]-1))
                start = j[0]
                seedstart.append(("wl",j[1]+j[2]+1, end))
                end = j[0] + j[2]
                str = "lt"
                break
            if(j==waterlight[-1] and str=="wl"):
                str = "lt"
                break
        print(str, start, end)
        for j in lighttemp:
            if(str!="lt"):
                break
            if(start>=j[1] and start<=j[1]+j[2]):
                start = j[0] + start-j[1]
                if(end>=j[1] and end<=j[1]+j[2]):
                    end = j[0] + end-j[1]
                else:
                    seedstart.append(("lt", j[1]+j[2]+1, end))
                    end = j[0] + j[2]
                str = "th"
                break
            if(end>=j[1] and end<=j[1]+j[2]):
                end = j[0] + end-j[1]
                seedstart.append(("lt",start, j[1]-1))
                start = j[0]
                str = "th"
                break
            if(start<j[1] and end>j[1]+j[2]):
                seedstart.append(("lt",start, j[1]-1))
                start = j[0]
                seedstart.append(("lt",j[1]+j[2]+1, end))
                end = j[0] + j[2]
                str = "th"
                break
            if(j==lighttemp[-1] and str=="lt"):
                str = "th"
                break
        print(str, start, end)
        for j in temphumid:
            if(str!="th"):
                break
            if(start>=j[1] and start<=j[1]+j[2]):
                start = j[0] + start-j[1]
                if(end>=j[1] and end<=j[1]+j[2]):
                    end = j[0] + end-j[1]
                else:
                    seedstart.append(("th", j[1]+j[2]+1, end))
                    end = j[0] + j[2]    
                str = "hl"
                break
            if(end>=j[1] and end<=j[1]+j[2]):
                end = j[0] + end-j[1]
                seedstart.append(("th",start, j[1]-1))
                start = j[0]
                str = "hl"
                break
            if(start<j[1] and end>j[1]+j[2]):
                seedstart.append(("th",start, j[1]-1))
                start = j[0]
                seedstart.append(("th",j[1]+j[2]+1, end))
                end = j[0] + j[2]
                str = "hl"
                break
            if(j==temphumid[-1] and str=="th"):
                str = "hl"
                break
        print(str, start, end)
        for j in humidloca:
            if(str!="hl"):
                break
            if(start>=j[1] and start<=j[1]+j[2]):
                start = j[0] + start-j[1]
                if(end>=j[1] and end<=j[1]+j[2]):
                    end = j[0] + end-j[1]
                else:
                    seedstart.append(("hl", j[1]+j[2]+1, end))
                    end = j[0] + j[2]
                str = "ll"
                break
            if(end>=j[1] and end<=j[1]+j[2]):
                end = j[0] + end-j[1]
                seedstart.append(("hl",start, j[1]-1))
                start = j[0]
                str = "ll"
                break
            if(start<j[1] and end>j[1]+j[2]):
                seedstart.append(("hl",start, j[1]-1))
                start = j[0]
                seedstart.append(("hl",j[1]+j[2]+1, end))
                end = j[0] + j[2]
                str = "ll"
                break
            if(j==humidloca[-1] and str=="hl"):
                str = "ll"
                break

        print(seedstart)
        print(start, end)
        minval = min(minval, start, end)
print(minval)
    