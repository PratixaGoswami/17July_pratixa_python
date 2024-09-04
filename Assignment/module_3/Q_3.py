# Write a Python program to append text to a file and display the text. 
# f=open("appendfile.txt","a")
# f.write("hello"+"\n"+"how are you")
# f=open("appendfile.txt","r")
# content=f.read()
# print(content)
def append_file(filepath,text):
    f=open(filepath,"a")
    f.write("\n"+text)
def read_file(filepath):
    f=open(filepath,"r")    
    content=f.read()
    print(content)
filepath='appendfile.txt'    
text='this is new line of text.'
append_file(filepath,text)
read_file(filepath)