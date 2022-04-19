# Problem no. 2053. Kth Distinct String in an Array
arr = ["aaa","aa","a"]
k = 1
d={}
for i in arr:
    d[i]=arr.count(i)
a=[]
for i in d:
    if(d[i]==1):
        a.append(i)
#print(a,d)
if(len(a)>=k):
    print(a[k-1])
else:
    print("")
