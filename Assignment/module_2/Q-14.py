""" Write a Python program to find the second smallest number in a list."""
def second_smallest_num(numbers):
    num=sorted(set(numbers))
    
    return num[1] if len(num)>= 2 else None

number=[2,3,4,5,6,7,8,9]
result=second_smallest_num(number)
print("numbers:",number)
print("second smallest number:",result)
  
