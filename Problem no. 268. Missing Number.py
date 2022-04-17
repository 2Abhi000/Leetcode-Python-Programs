# Problem no. 268. Missing Number
nums=[3,0,1]
nums.sort()
for i in range(len(nums)+1):
    if(i not in nums):
        print(i)
        
