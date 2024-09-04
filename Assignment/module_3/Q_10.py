# Write a Python program to count the frequency of words in a file. 

from collections import Counter

with open("studentdata.txt", "r") as f:
    words = f.read().lower().split()


word_count = Counter(words)
print(word_count)

# for word, count in word_count.items():
#     print(f"{word}: {count}")
    