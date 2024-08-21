""" Write a Python function that checks whether a passed string is
palindrome or not"""

def check_palindrome(word):
    word = word.lower()
    if word == word[::-1]:
        print("string is palindrome")
    else:
        print("string is not palindrome") 
    return word    

str=input("Enter string to check if it is a palindrome:")
check_palindrome(str)

