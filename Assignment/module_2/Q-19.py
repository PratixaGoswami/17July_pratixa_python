""" Write a Python program to create a tuple with different data types."""

my_tuple=(112,"Hello",3.14,True,[1,2,3,4],{'name':'pratixa','subject':'python'})

print('the tuple is:',my_tuple)
for i in my_tuple:
    print(f"{i} : {type(i)}")
