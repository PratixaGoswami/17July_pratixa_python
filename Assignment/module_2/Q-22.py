""" Write a Python program to check whether an element exists within a
tuple"""

my_tuple = (10,20,30,40,50,60)
element_check = 30

if element_check in my_tuple:
    print(f"element {element_check} exists in the tuple.")
else:
    print(f"element {element_check} does not exist in the tuple.")
