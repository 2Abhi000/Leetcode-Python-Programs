# Problem no. 1460. Make Two Arrays Equal by Reversing Sub-arrays
target = [1,2,3,4]
arr = [2,4,1,3]

p=list(sorted(arr))
d={}
d1={}
for i in range(len(target)):
    d[target[i]]=target.count(target[i])
for i in range(len(p)):
    d1[p[i]]=p.count(p[i])
if(d==d1):
    print(True)
else:
    print(False)
