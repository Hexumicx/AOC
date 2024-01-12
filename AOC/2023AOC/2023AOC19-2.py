from queue import Queue
s=input()
workflow = {}
while s!="":
    label, ins = s.split("{")
    ins = ins[:-1]
    ins = ins.split(",")
    workflow[label] = ins
    s=input()

q = Queue()
val = {"loc":"in", "x":(1,4000), "m":(1,4000), "a":(1,4000), "s":(1,4000)}
q.put(val)
count = 0
while not q.empty():
    cur = q.get()
    print(cur, "currs")
    curloc = cur["loc"]
    if curloc=="A":
        count += (cur["x"][1]-cur["x"][0]+1)*(cur["m"][1]-cur["m"][0]+1)*(cur["a"][1]-cur["a"][0]+1)*(cur["s"][1]-cur["s"][0]+1)
        continue
    elif curloc=="R":
        continue
    for i in workflow[curloc]:
        if i=="A":
            count += (cur["x"][1]-cur["x"][0]+1)*(cur["m"][1]-cur["m"][0]+1)*(cur["a"][1]-cur["a"][0]+1)*(cur["s"][1]-cur["s"][0]+1)
        elif i=="R":
            break
        elif i.find("<")!= -1:
            cond, res = i.split(":")
            v, num = cond.split("<")
            print(cur[v])
            if cur[v][0]<int(num)<cur[v][1]:
                temp = {"loc":res, "x":cur["x"], "m":cur["m"], "a":cur["a"], "s":cur["s"]}
                temp[v] = (cur[v][0], int(num)-1)
                q.put(temp)
                cur[v] = (int(num), cur[v][1])
                continue
            elif cur[v][1]<int(num):
                cur["loc"] = res
                break
            else:
                continue
        elif i.find(">")!= -1:
            cond, res = i.split(":")
            v, num = cond.split(">")
            if cur[v][0]<int(num)<cur[v][1]:
                temp = {"loc":res, "x":cur["x"], "m":cur["m"], "a":cur["a"], "s":cur["s"]}
                temp[v] = (int(num)+1, cur[v][1])
                q.put(temp)
                cur[v] = (cur[v][0], int(num))
                continue
            elif cur[v][0]>int(num):
                cur["loc"] = res
                break
            else:
                continue
        else:
            temp = {"loc":i, "x":cur["x"], "m":cur["m"], "a":cur["a"], "s":cur["s"]}
            q.put(temp)
            break

print(count)