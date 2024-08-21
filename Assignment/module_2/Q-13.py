"""Write a Python program to select an item randomly from a list."""
import random
def select_random_item(input_list):   
    return random.choice(input_list)



element=(input("Enter list of element:")).split()

print("list of item:",element)
result=select_random_item(element)
print("randomly selected item:",result)
