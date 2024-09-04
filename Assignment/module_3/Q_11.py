# Write a Python program to write a list to a file. 
list=['milan','pratixa','veer','mahi']

f=open("listfile.txt","w")
for i in list:
    f.write(f"{list}\n")