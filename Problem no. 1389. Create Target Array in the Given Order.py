# Problem no. 1389. Create Target Array in the Given Order
nums = [4,2,1,1]
index = [0,0,2,0]
target=[]
for i,j in zip(nums,index):
    target.insert(j,i)
print(target)
