""" Write a Python program to returns sum of all divisors of a number"""
number=int(input("enter number:"))
sum=0
for i  in range(1,number+1):
    if number % i==0:
        sum+=i
print("The sum of all divisor is :",sum)        
