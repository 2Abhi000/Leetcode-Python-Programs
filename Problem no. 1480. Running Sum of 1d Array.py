# Problem no. 1480. Running Sum of 1d Array
nums=[1,1,1,1]
s=0
a=[]
for i in range(len(nums)):
    s=s+nums[i]
    a.append(s)
print(a)
