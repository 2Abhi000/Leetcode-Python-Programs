# Problem no. 1967. Number of Strings That Appear as Substrings in Word
patterns = ["a","a","a"]
word = "ab"
a=[]
k=''
for i in range(len(word)):
    for j in range(i,len(word)):
        k=k+word[j]
        if(k in patterns):
            a.append(k)
    k=''            
p=set(a)
print(len(p))
