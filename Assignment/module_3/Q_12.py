# Write a Python program to copy the contents of a file to another file. 
f=open("copylistfile.txt","a")
c=open("listfile.txt","r")
content=c.read()
f.write(content)

