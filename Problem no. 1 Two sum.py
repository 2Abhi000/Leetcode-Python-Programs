# Problem no. 1 Two sum
num=[3,3]
target=6
ar=[]
for i in range(0,len(num)):
    for j in range(i+1,len(num)):
        if(num[i]+num[j]==target):
            ar.append(i)
            ar.append(j)
print(ar)

