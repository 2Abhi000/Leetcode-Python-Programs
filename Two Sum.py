#Two Sum
size=int(input("Enter the size of array: "))
nums=[]
target=int(input("Enter the target variable: "))
s=[]
for i in range(size):
    nums.append(int(input("Enter the number: ")))
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if(nums[i]+nums[j]==target):
            s.append(i)
            s.append(j)
print(s)
