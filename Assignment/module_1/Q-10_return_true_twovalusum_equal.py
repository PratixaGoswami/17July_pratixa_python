''' Write a Python program that will return true if the two given integer
values are equal or their sum or difference is 5.'''

a=int(input("enter value of A:"))
b=int(input("enter value of B:"))

if a == b:
    result = True
elif a+b == 5:
    result =  True
elif abs(a - b) == 5:
    result = True    
else:
    result = False    
print(result)   




