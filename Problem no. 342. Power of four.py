# Problem no. 342. Power of four
def isPowerOf4(n):
    a = 1
    while a < n:
        a *= 4
    if a == n:
        return True
    else:
        return False
n=int(input())
x=isPowerOf4(n)
print(x)
