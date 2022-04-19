# Problem no. 1528. Shuffle String
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
l=[]

for i in s:
    l.append(i)
d=dict(zip(indices,l))
an=''
for i in sorted(d):
    an=an+d[i]
print(an)

