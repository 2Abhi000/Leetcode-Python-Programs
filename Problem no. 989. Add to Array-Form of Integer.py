# Problem no. 989. Add to Array-Form of Integer
num = [1,2,0,0]
k = 34
num_string=[]
for i in num:
    num_string.append(str(i)) 
            
num_string = "".join(num_string)
num_string = int(num_string) + k    
new_list=[]
for i in str(num_string):
    new_list.append(int(i))
print(new_list)
