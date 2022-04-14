# Problem no. 136,  Single Number
nums=[4,1,2,1,2]
d={}
for i in nums:
    d[nums.count(i)]=i
if(1 in d):
    print(d[1])
