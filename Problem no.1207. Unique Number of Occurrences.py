# Problem no.1207. Unique Number of Occurrences
arr=[1,2,2,1,1,3]
d={}
a=[]
for i in arr:
    d[i]=arr.count(i)
for i in d:
    a.append(d[i])
aa=list(set(a))
if(len(a)==len(aa)):
    print('True')
else:
    print('False')
