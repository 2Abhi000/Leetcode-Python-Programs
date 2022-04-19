# Problem no. 804. Unique Morse Code Words
d={'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",
   'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",
   'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
a=[]
k=''
words = ["gin","zen","gig","msg"]
for i in words:
    for j in i:
        k=k+d[j]
    a.append(k)
    k=''
#print(a)
s=set(a)
print(len(s))



