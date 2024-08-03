'''
 Write a Python program to count the number of characters (character
frequency) in a string
'''
str1 = input("Enter string: ")

<<<<<<< HEAD
for char in (str1):
=======
for char in set(str1):
>>>>>>> 4c93994b6e4ae4db622e2e2f48fd0f7d7e16db57
   
    print(char, ":", str1.count(char))

