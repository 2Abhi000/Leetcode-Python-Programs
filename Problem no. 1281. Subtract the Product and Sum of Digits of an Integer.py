# Problem no. 1281. Subtract the Product and Sum of Digits of an Integer
n=234
summ=0
prod=1
for i in str(n):
    summ=summ+int(i)
    prod=prod*int(i)
ans=prod-summ
print(ans)
