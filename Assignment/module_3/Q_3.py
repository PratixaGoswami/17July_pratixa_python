# Write a Python program to append text to a file and display the text. 
f=open("appendfile.txt","a")
f.write("hello"+"\n"+"how are you")
f=open("appendfile.txt","r")
content=f.read()
<<<<<<< HEAD
print(content)
=======
print(content)
>>>>>>> e87b1a4 (completed)
