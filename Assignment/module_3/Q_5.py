# Write a Python program to read last n lines of a file.

f=open("table.txt","r")
lastline=f.readlines()
if lastline:
    line=lastline[-1]
    print(line)
else:
    print("The file is empty")    
