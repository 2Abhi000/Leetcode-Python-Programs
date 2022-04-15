# Problem no 448. Find All Numbers Disappeared in an Array
a=[1,1]
s=set(a)
n=[]
for i in range(1,len(a)+1):
    if(i not in a):
        n.append(i)
print(n)
