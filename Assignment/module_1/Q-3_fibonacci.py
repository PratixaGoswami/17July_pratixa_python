# Write a Python program to get the Fibonacci series of given range.

num=int(input("Enter Number:"))
a=0
b=1
print("Fibonaccci series:")
for i in range(1,num+1):
    print(a)
    c=a+b
    a=b
    b=c
