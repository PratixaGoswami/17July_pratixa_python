# Write a Python program to count the number of lines in a text file. 
f=open("Studentdata.txt","r")

count=0
for i in f:
    count+=1
print(count)    