time = input()
distance = input()
_ , time = time.split(":")
time = time.strip().split(" ")
time = [int(i) for i in time if i != ""]
_, distance = distance.split(":")
distance = distance.strip().split(" ")
distance = [int(i) for i in distance if i != ""]
count = 0
total = 1
for(i,j) in zip(time,distance):
    count = 0
    for t in range(i):
        if(t*(i-t)>=j):
            count+=1
    total*=count
print(total)
