''' Write python program that swap two number with temp variable and
without temp variable.
'''


'''a=int(input("Enter value of A:"))
b=int(input("Enter value of B:"))
temp=a
a=b
b=temp
print(f"After swaping:A={a} and B={b}")'''


a=10
b=15

print(f"Before swaping : A is {a} and B is {b}")
a=a+b
b=a-b
a=a-b
print(f"after swaping : A is {a} and B is {b}")