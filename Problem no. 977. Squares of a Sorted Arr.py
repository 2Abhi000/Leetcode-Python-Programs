# Problem no. 977. Squares of a Sorted Array
num=[-4,-1,0,3,10]
def sq(n):
    return n*n
x=list(map(sq,num))
x.sort()
print(x)
