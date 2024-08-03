'''Write a Python function to insert a string in the middle of a string.'''
o_str=input("Enter the original string:")
i_str=input("Enter the insert string:")

mid_str=len(o_str)//2

n_str=o_str[:mid_str]+i_str+o_str[mid_str:]
print(n_str)

