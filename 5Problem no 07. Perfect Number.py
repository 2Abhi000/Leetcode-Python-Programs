# 5Problem no 07. Perfect Number
num=7
s=0
for i in range(1,num):
    if(num%i==0):
        s=s+i
if(s==num):
    print('True')
else:
    print('False')





