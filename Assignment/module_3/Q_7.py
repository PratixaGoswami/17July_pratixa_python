# Write a Python program to read a file line by line store it into a variable. 

f=open("studentdata.txt","r")
content=f.readlines()
print(content)