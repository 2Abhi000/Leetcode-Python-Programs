# Problem no. 1796. Second Largest Digit in a String
s="abc1111"
n=[]
for i in s:
    if(i.isdigit()):
        n.append(i)
k=list(set(n))
x=max(k)
k.remove(x)
if(len(k)>=1):
    print(max(k))
else:
    print('-1')
