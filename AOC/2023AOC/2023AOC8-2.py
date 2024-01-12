s=input()
m={}
ghost=[]
while s!='':
    head, tail=s.split("=")
    head = head.strip()
    if head[-1] == 'A':
        ghost.append(head)
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
total = len(ghost)
cycle = [0] * len(ghost)
while(True):
    for i in s:
        steps+=1
        for j in range(len(ghost)):
            if(ghost[j][-1] != 'Z'):
                if i=='L':
                    ghost[j]=m[ghost[j]][0]
                else:
                    ghost[j]=m[ghost[j]][1]
                if ghost[j][-1] == 'Z':
                    cycle[j] = steps
                    total -= 1
        if total == 0:
            print(cycle)
            exit(0)