"""Write a Python program to print all unique values in a dictionary."""
dict1={'a':1,'b':2,'c':3,'d':1}
value=dict.values(dict1)
unique_value=set(value)
print(unique_value)
