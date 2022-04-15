# Problem no 476. Number Complement
n=1
b=str(bin(n))
b=b.replace("0b", "")
s=''
for i in b:
    if(i=='0'):
        s=s+'1'
    if(i=='1'):
        s=s+'0'
a = int(s,2)
print(a)



