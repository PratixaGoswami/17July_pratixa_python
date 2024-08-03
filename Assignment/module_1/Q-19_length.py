'''
Write a Python function that takes a list of words and returns the length
of the longest one'''
word=input("enter words:")
word=word.split()
max_length=0
for i in word:
    if len(i)>max_length:
        max_length=len(i)
print("length of longest word:",max_length) 


