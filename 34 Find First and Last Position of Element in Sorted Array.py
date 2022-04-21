# Problem no. 34 Find First and Last Position of Element in Sorted Array
nums = [5,7,7,8,8,10]
target = 6
a=[]
d=[-1,-1]
t=0
for i in range(len(nums)):
    if(nums[i]==target):
        a.append(i)
        t=1

if(t):
    print(a)
else:
    print(d)
    
