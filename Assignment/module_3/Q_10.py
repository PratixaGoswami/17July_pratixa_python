# Write a Python program to count the frequency of words in a file. 

from collections import Counter

<<<<<<< HEAD
with open("studentdata.txt", "r") as f:
    words = f.read().lower().split()
word_count = Counter(words)
for word, count in word_count.items():
    print(f"{word}: {count}")
=======
# with open("studentdata.txt", "r") as f:
#     words = f.read().lower().split()
# word_count = Counter(words)
# for word, count in word_count.items():
#     print(f"{word}: {count}")
>>>>>>> e87b1a4 (completed)
    
f=open("studentdata.txt","r")
words=f.read().split()
word_count=Counter(words)
for word,count in word_count.items():
    print(f"{word}:{count}")

