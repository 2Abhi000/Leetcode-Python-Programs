# Problem no. 2264. Largest 3-Same-Digit Number in String
num = "42352338"
d={}
s=[]
for i in range(len(num)):
    d[num[i]]=num.count(num[i])
#print(d)
for i in d:
    if(d[i]==3):
        s.append(i)
m=max(s)
k=''
for i in range(3):
    k=k+str(m)
if(k in num):
    print("\""+k+"\"")
else:
    print("\""+"\"")
