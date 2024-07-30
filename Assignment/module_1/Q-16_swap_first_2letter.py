'''Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string.'''

str1=input("Enter the first string:")
str2=input("Enter the second string:")

n_str1=str2[:2]+str1[2:]
n_str2=str1[:2]+str2[2:]
result=n_str1+ " "+ n_str2

print("Result:",result)