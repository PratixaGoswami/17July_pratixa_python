'''
Write a Python function to reverses a string if its length is a multiple of
4.'''
str=input("Enter string:")

if  len(str) % 4 == 0:
    reversed_s = str[::-1]
    print("Reversed string:", reversed_s)
else:
    print("original string:",str)    