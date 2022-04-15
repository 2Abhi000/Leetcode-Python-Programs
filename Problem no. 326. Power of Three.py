# Problem no. 326. Power of Three
def isPowerOf3(n):
    a = 1
    while a < n:
        a *= 3
    if a == n:
        return True
    else:
        return False
n=int(input())
x=isPowerOf3(n)
print(x)
