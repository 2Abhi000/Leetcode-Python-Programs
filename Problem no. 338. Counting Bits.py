# Problem no. 338. Counting Bits
n=5
a=[]
for i in range(n+1):
    k=bin(i)
    k=k.replace('0b','')
    a.append(k.count('1'))
print(a)

