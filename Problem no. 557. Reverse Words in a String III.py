# Problem no. 557. Reverse Words in a String III
s= "God Ding"
k=''
s=s[::-1]
ar=s.split()
for i in ar[::-1]:
    k=k+i
    k=k+' '
print((k[0:(len(k)-1)]))




