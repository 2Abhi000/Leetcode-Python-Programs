# Merged Sorted Array Problem=88
a=[1,2,3,0,0,0]
m=3
n=3
b=[2,5,6]
c=[]
a=a+b
a.sort()
while(0 in a):
    a.remove(0)
return(a)
