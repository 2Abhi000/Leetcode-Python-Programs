# Problem no. Find Target Indices After Sorting Array
nums = [1,2,5,2,3]
target = 2
nums.sort()
ar=[]
for i in range(len(nums)):
    if(nums[i]==target):
        ar.append(i)
        
else:
    print(ar)

