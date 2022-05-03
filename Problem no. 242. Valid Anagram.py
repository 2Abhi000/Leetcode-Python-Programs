# Problem no. 242. Valid Anagram
s='anagram'
t='nagaram'
a=1
if(len(s)!=len(t)):
    a=0
    
else:
    for i in s:
        for j in t:
            if(i==j):
                a=1
            else:
                a=0
if(a):
    print(True)
else:
    print(False)
