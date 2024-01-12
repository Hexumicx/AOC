def dp(s, nums):
    # print(s, nums)
    if(len(nums)==0 and len(s)==0):
        return 1
    if(len(nums)==0 ):
        if('#' not in s):
            return 1
        else:
            return 0
    cur = 0
    ways = 0
    change = True
    for i in range(len(s)):
        if(s[i]=="#"):
            change = True
            for j in range(nums[0]):
                if((i+j)>=len(s)):
                    return 0
                if(s[i+j] == "?" or s[i+j] == "#"):
                    continue
                else:
                    return 0
            if((i+nums[0])<len(s)):
                if(s[i+nums[0]] == "#"):
                    return 0
                return dp(s[i+nums[0]+1:], nums[1:])
            else:
                return dp(s[i+nums[0]:], nums[1:])
        if(s[i]=="."):
            return dp(s[i+1:], nums)
        if(s[i]=="?"):
            change = True
            for j in range(nums[0]):
                if((i+j)>=len(s)):
                    return 0
                if(s[i+j] == "?" or s[i+j] == "#"):
                    continue
                else:
                    change = False
                    break
            if((i+nums[0])<len(s)):
                if(s[i+nums[0]] == "#"):
                    change = False
            if(change):
                if((i+nums[0])<len(s)):
                    ways += dp(s[i+nums[0]+1:], nums[1:])
                else:
                    ways += dp(s[i+nums[0]:], nums[1:])
            ways += dp(s[i+1:], nums)
            break

    return ways
           
s = input()
count = 0
while s!='':
    s, nums = s.split(" ")
    nums = nums.split(",")
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    s = list(s)
    count += dp(s, nums)
    print(count)
    s = input()
    
