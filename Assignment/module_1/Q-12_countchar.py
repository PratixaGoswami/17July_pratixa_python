'''
 Write a Python program to count the number of characters (character
frequency) in a string
'''
str1 = input("Enter string: ")
for char in (str1):
    print(char, ":", str1.count(char))

