# Problem no. 2185. Counting Words With a Given Prefix
words = ["pay","attention","practice","attend"]
pref = "at"
l=slice(0,len(pref))
c=0
for i in words:
    if(i[l]==pref):
        c=c+1
print(c)
