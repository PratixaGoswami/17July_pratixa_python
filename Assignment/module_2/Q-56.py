""" Write a Python program to read a random line from a file."""
import random

file=open("studentdata.txt","r")
line = file.readlines()
random_line=random.choice(line)
print(random_line.strip())