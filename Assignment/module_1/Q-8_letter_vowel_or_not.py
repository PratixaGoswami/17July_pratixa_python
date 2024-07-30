# Write a Python program to test whether a passed letter is a vowel or not.
vowel=('a','e','i','o','u','A','E','I','O','U')
letter=input("Enter any letter:")
if len(letter)== 1 and letter.isalpha():
    if letter in vowel:
        print("This letter is vowel")
    else:
        print("This letter is not vowel") 
else:
    print("please enter a single alphabet letter")           

