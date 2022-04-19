# Problem no. 2114. Maximum Number of Words Found in Sentences
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
a=[]
for i in sentences:
    l=len(i.split())
    a.append(l)
print(max(a))
