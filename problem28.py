#leetcode problem 28
haystack="aaaaaaaaaa"
needle="bba"
def strStr(haystack,needle):
    
    if(needle in haystack):
        ind=haystack.index(needle)
        return(ind)
    else:
        return -1
print(strStr(haystack,needle))
