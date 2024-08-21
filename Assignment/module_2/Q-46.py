""" Write a Python function to calculate the factorial of a number"""
def fac_num(n):
    if n<0:
        print("Input must be a nonnegative integer")

    f=1
    for i in range(1,n+1):
        f*=i
    print(f)    
    return f
    
n=int(input("Enter number:"))
fac_num(n)   




