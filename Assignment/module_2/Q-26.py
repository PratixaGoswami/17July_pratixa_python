""" Write a Python program to replace last value of tuples in a list."""
list=[(1,2,3),(4,5,6),(7,8,9)]
new_value=100
replace=[i[:-1]+(new_value,) for i in list]
print("original List:",list)
print("updated List:",replace)

