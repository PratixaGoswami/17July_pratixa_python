'''  Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
'''
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))


if a == b or b == c or a == c:
    sum = 0
else:
    sum = a + b + c

print(f"The sum is: {sum}")