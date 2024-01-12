s=input()
workflow = {}
while s!="":
    label, ins = s.split("{")
    ins = ins[:-1]
    ins = ins.split(",")
    workflow[label] = ins
    s=input()

ss=input()
count = 0
while ss!="":
    ss=ss[1:-1]
    x, m, a, s = ss.split(",")
    data = {}
    data["x"] = int(x[x.find("=")+1:])
    data["m"] = int(m[m.find("=")+1:])
    data["a"] = int(a[a.find("=")+1:])
    data["s"] = int(s[s.find("=")+1:])
    curloc="in"
    while curloc!="out":
        if curloc=="A":
            for info in data.values():
                count+=info
            break
        elif curloc=="R":
            break
        for i in workflow[curloc]:
            if i=="A":
                for info in data.values():
                    count+=info
                curloc="out"
                break
            elif i=="R":
                curloc="out"
                break
            elif i.find("<")!= -1:
                cond, res = i.split(":")
                v, num = cond.split("<")
                if data[v]<int(num):
                    curloc=res
                    break
                else:
                    continue
            elif i.find(">")!= -1:
                cond, res = i.split(":")
                v, num = cond.split(">")
                if data[v]>int(num):
                    curloc=res
                    break
                else:
                    continue
            else:
                curloc=i


    ss=input()

print(count)