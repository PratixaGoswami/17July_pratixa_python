# Write a python program to find the longest words. 
f=open("studentdata.txt","r")
word= f.read().split()
max_length=0
longest_word=""
for i in word:
    if len(i)>max_length:
        max_length=len(i)
        longest_word=i
print(longest_word)        
print(max_length)

