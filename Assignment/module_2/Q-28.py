""" Write a Python program to remove an empty tuple(s) from a list of tuples."""
tuple_list=[(1,2,3),(),(4,5,6),(),(7,8,9)]
print(tuple_list)
new_list=[i for i in tuple_list if i]
print(new_list)
