# Write a Python program to read an entire text file. 
f=open("studentdaa.txt","r")
content=f.read()
if content:
    print(content)
else:
    print("File are not found")    
