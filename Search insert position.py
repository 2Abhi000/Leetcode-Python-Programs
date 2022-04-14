 #Search Insert Position
def searchInsert(nums, target: int) -> int:
    for i in (nums):
        if(target not in nums):
            nums.append(target)
            nums.sort()
            return(nums.index(target))
        else:
            return nums.index(target)
a=[1,3,5,6]
target=2
x=searchInsert(a,target)
print(x)
            
        
