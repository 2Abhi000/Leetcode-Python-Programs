# Problem no. 2255. Count Prefixes of a Given String
words = ["a","a"]
s = "aa"
t=0
for j in words:
    if(j[0]==s[0] and j in s):
        t=t+1
print(t)
