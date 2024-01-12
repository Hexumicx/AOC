def dp(s, nums):
    # print(s, nums)
    if(len(nums)==0 and len(s)==0):
        m[(tuple(s), tuple(nums))] = 1
        return 1
    if(len(nums)==0 ):
        if('#' not in s):
            m[(tuple(s), tuple(nums))] = 1
            return 1
        else:
            m[(tuple(s), tuple(nums))] = 0
            return 0
    if(m.get((tuple(s), tuple(nums)))!=None):
        return m[(tuple(s), tuple(nums))]
    cur = 0
    ways = 0
    change = True
    for i in range(len(s)):
        if(s[i]=="#"):
            change = True
            for j in range(nums[0]):
                if((i+j)>=len(s)):
                    m[(tuple(s), tuple(nums))] = 0
                    return 0
                if(s[i+j] == "?" or s[i+j] == "#"):
                    continue
                else:
                    m[(tuple(s), tuple(nums))] = 0
                    return 0
            if((i+nums[0])<len(s)):
                if(s[i+nums[0]] == "#"):
                    m[(tuple(s), tuple(nums))] = 0
                    return 0
                m[(tuple(s), tuple(nums))] = dp(s[i+nums[0]+1:], nums[1:])
                return dp(s[i+nums[0]+1:], nums[1:])
            else:
                m[(tuple(s), tuple(nums))] = dp(s[i+nums[0]:], nums[1:])
                return dp(s[i+nums[0]:], nums[1:])
        if(s[i]=="."):
            m[(tuple(s), tuple(nums))] = dp(s[i+1:], nums)
            return dp(s[i+1:], nums)
        if(s[i]=="?"):
            change = True
            for j in range(nums[0]):
                if((i+j)>=len(s)):
                    m[(tuple(s), tuple(nums))] = 0
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
    m[(tuple(s), tuple(nums))] = ways
    return ways
           
m = {}
s = input()
count = 0
while s!='':
    s, nums = s.split(" ")
    nums = nums.split(",")
    s = s+'?'+s+'?'+s+'?'+s+'?'+s
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    nums = nums*5
    s = list(s)
    count += dp(s, nums)
    print(count)
    s = input()
    
