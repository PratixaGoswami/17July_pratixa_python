"""Write a Python program to unzip a list of tuples into individual lists"""
t_list=[(1,'a'),(2,'b'),(3,'c')]
a,b=zip(*t_list)
print(list(a),list(b))