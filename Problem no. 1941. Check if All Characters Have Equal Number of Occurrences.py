# Problem no. 1941. Check if All Characters Have Equal Number of Occurrences
s='aaabb'
d={}
for i in range(len(s)):
    d[s[i]]=s.count(s[i])
a=[]
for i in d:
    a.append(d[i])
t=a[0]
k=0
for i in a:
    if((i==t)):
        k=1
    else:
        k=0
        break
if(k):
    print('t')
else:
    print('f')
