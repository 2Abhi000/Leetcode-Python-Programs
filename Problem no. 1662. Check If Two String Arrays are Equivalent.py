# Problem no. 1662. Check If Two String Arrays are Equivalent
word1 = ["ab", "c"]
word2 = ["a", "bc"]

s1=''
s2=''
for i in word1:
    s1=s1+i
for j in word2:
    s2=s2+j
if(s1==s2):
    print(True)
else:
    print(False)
