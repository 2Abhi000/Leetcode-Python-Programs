# Problem no 485. Max Consecutive Ones
n=[1,0,1,1,0,1]
s=''
for i in n:
    s=s+str(i)
j=s.split('0')
m=0
for i in j:
    if(len(i)>m):
        m=len(i)
print(m)



