# Problem no. 33. Search in Rotated Sorted Array
nums = [4,5,6,7,0,1,2]
target = 0
d={}
for i in range(len(nums)):
    d[nums[i]]=i
if(target in d):
    print(d[target])
else:
    print('-1')
