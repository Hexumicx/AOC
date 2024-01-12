s=input()
m={}
while s!='':
    head, tail=s.split("=")
    head = head.strip()
    tail = tail.strip()
    tail = tail[1:-1]
    left, right=tail.split(",")
    left = left.strip()
    right = right.strip()
    m[head]=(left, right)
    s=input()

s=input("instructions")
cur='AAA'
steps=0
while(True):
    for i in s:
        steps+=1
        if i=='L':
            cur=m[cur][0]
        else:
            cur=m[cur][1]
        if cur=="ZZZ":
            print(steps)
            exit(0)