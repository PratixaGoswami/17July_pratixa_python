"""Write a Python program to convert a list of characters into a string."""

def conver_char_str(list):
    nlist="".join(list)
    return nlist



list=['p','r','a','t','i','x','a']
result=conver_char_str(list)
print("characters list:",list)
print("convert a list of characters into a string:",result)

