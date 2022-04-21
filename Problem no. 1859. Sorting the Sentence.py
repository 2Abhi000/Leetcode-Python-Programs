# Problem no. 1859. Sorting the Sentence
s = "is2 sentence4 This1 a3"
no=[]
u=s.split()
b=[]
k=''
d={}
for i in s:
    for j in i:
        if(j.isdigit()):
            no.append(int(j))
no.sort()
for i in s:
    for j in no:
        if(str(j) in i):
            b.append(i)
            ind=s.index(str(j))
            s.replace(s[ind],'')

for i in range(len(b)):
    if(b[i] in u[i]):
        d[int(b[i])]=u[i].replace(b[i],'')

sd= dict(sorted(d.items(), key=lambda item: item[0]))

for i in sd:
    k=k+sd[i]
    k=k+' '
n=len(k)
print(k[:-1])
