# Problem no. 645. Set Mismatch
nums = [1,1]
d={}
a=[]
for i in range(1,len(nums)+1):
    if(i not in nums):
        a.append(i)
for i in nums:
    d[nums.count(i)]=i
for i in d:
    if(i>1):
        a.insert(0,d[i])
print(a)


