s = input()
count = 0
while s != "end":
    arr = []
    while s!="":
        arr.append(s)
        s = input()
    for i in range(len(arr)-1):
        if(arr[i] == arr[i+1]):
            paired = True
            low = i
            high = i+1
            while(low>=0 and high<len(arr)):
                if(arr[low] != arr[high]):
                    paired = False
                low-=1
                high+=1
            if(paired):
                count += (i+1)*100
    for i in range(len(arr[0])-1):
        same = True
        for j in range(len(arr)):
            if(arr[j][i] != arr[j][i+1]):
                same = False
                break
        if(same):
            low = i
            high = i+1
            while(low>=0 and high<len(arr[0])):
                paired = True
                for j in range(len(arr)):
                    if(arr[j][low] != arr[j][high]):
                        paired = False
                        break
                if not paired:
                    break
                low-=1
                high+=1
            if(paired):
                count += i+1
    s = input("Next")
    
print(count)

        
