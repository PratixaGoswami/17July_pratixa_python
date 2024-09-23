# Write a Python program to read last n lines of a file.

f=open("table.txt","r")
lastline=f.readlines()
if lastline:
    line=lastline[-1]
    print(line)
else:
<<<<<<< HEAD
    print("The file is empty")    
=======
    print("The file is empty")    
>>>>>>> e87b1a4 (completed)
