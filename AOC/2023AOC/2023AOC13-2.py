from copy import copy, deepcopy
s = input()
count = 0
while s != "end":
    arr = []
    while s!="":
        arr.append(list(s))
        s = input()
    for i in range(len(arr)-1):
        if(arr[i] == arr[i+1]):
            paired = True
            low = i
            high = i+1
            while(low>=0 and high<len(arr)):
                if(arr[low] != arr[high]):
                    paired = False
                    break
                low-=1
                high+=1
            if(paired):
                x = i
                y = -1
                break
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
                y = i
                x=-1
    for a in range(len(arr)):
        for b in range(len(arr[0])):
            arr2 = deepcopy(arr)
            if(arr2[a][b]=="#"):
                arr2[a][b]="."
            elif(arr2[a][b]=="."):
                arr2[a][b]="#"
            for i in range(len(arr)-1):
                if(arr2[i] == arr2[i+1]):
                    paired = True
                    low = i
                    high = i+1
                    while(low>=0 and high<len(arr)):
                        if(arr2[low] != arr2[high]):
                            paired = False
                            break
                        low-=1
                        high+=1
                    if(paired and i!=x):
                        print(i)
                        count += (i+1)*100
                        break
            for i in range(len(arr2[0])-1):
                same = True
                for j in range(len(arr2)):
                    if(arr2[j][i] != arr2[j][i+1]):
                        same = False
                        break
                if(same):
                    low = i
                    high = i+1
                    while(low>=0 and high<len(arr[0])):
                        paired = True
                        for j in range(len(arr2)):
                            if(arr2[j][low] != arr2[j][high]):
                                paired = False
                                break
                        if not paired:
                            break
                        low-=1
                        high+=1
                    if(paired):
                        if(i!=y):
                            count += i+1
                            break
    print(count/2)    
    s = input("Next")
    
print(count/2)

        
