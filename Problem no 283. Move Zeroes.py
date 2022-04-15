# Problem no 283. Move Zeroes
a=[0,0,1]
def moveZeroes(a):
        """
        Do not return anything, modify nums in-place instead.
        """
        c=0
        while(0 in a):
            c+=1
            a.remove(0)
        for i in range(c):
            a.append(0)
        return a
x=moveZeroes(a)
print(x)
