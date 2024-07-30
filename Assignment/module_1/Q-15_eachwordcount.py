# Write a Python program to count the occurrences of each word in a given sentence

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


   

