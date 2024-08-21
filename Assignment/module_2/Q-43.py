""" Write a Python program to find the highest 3 values in a dictionary"""
d={'a':1,'b':8,'c':3,'d':4,'e':5}
value=d.values()
highest3=sorted(value,reverse=True)[:3]
print("The highest three value are:",highest3)

