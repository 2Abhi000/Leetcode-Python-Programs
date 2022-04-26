# Problem no. 1394. Find Lucky Integer in an Array
arr = [2,2,3,4]
d={}
ar=[]
for i in range(len(arr)):
    d[arr[i]]=arr.count(arr[i])
#print(d)
for i in d:
    if(i==d[i]):
        ar.append(i)
    
if(len(ar)==0):
    print(-1)
else:
    print(max(ar))
