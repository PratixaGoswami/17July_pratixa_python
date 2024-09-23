# Write a Python program to count the frequency of words in a file. 

from collections import Counter
   
f=open("studentdata.txt","r")
words=f.read().split()
word_count=Counter(words)
for word,count in word_count.items():
    print(f"{word}:{count}")

