# Write a Python program to count the occurrences of each word in a given sentence

<<<<<<< HEAD
str1 = input("Enter string: ")
word=str1.split()

for char in (word):
   
    print(char, ":", str1.count(char))
  
=======
sen = input("Enter sentence: ")
words=sen.split()
w_count={}
for word in words:
    if word in w_count:
        w_count[word] += 1
    else:
        w_count[word] = 1

for w, c in w_count.items():
    print(f"{w}: {c}")


>>>>>>> 4c93994b6e4ae4db622e2e2f48fd0f7d7e16db57
   

