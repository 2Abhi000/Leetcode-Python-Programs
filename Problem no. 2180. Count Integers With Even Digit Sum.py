# Problem no. 2180. Count Integers With Even Digit Sum
num=30
def su(n):
    k=[]
    for i in str(n):
        k.append(int(i))
    if(sum(k)%2==0):
        return(True)
    else:
        return(False)
        
c=0
for i in range(1,num+1):
    if(su(i)):
        c=c+1
print(c)
    
