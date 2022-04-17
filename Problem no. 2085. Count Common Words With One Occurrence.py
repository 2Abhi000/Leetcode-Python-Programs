# Problem no. 2085. Count Common Words With One Occurrence
words1 = ["a","ab"]
words2 = ["a","a","a","ab"]
d1={}
d2={}
ar=[]
for i in words1:
    d1[i]=words1.count(i)
for i in words2:
    d2[i]=words2.count(i)
for i in d1:
    if(i in d2):
        if(d1[i]==d2[i]==1):
            ar.append(1)
    else:
        pass

print(sum(ar))
