time = 54708275
distance = 239114212951253
for i in range(time):
    if(i*(time-i)>=distance):
        print(i)
        print(time-i-i+1)
        break