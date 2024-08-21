""" Write a Python program to create a dictionary from a string."""

i_str='hello'

result={}

for i in i_str:
    if i in result:
        result[i]+=1
    else:
        result[i]=1
print(result)    
