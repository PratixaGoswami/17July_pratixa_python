"""Write a Python program to find the repeated items of a tuple."""

item=(1,2,2,3,3,4,5,6)
Repated_item=([i for i in item if item.count(i) > 1])
print(Repated_item)