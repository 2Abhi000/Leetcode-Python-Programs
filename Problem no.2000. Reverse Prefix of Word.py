# Problem no.2000. Reverse Prefix of Word
word="abcdefd"
ch="d"
if(ch in word):
    ind=word.index(ch)
    s=slice(0,ind)
    previousstring=word[s]
    s1=slice(ind+1,len(word))
    laststring=word[s1]
    k=ch+previousstring[::-1]+laststring
    print(k)
else:
    print(word)
