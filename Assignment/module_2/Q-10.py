"""Write a Python program to generate and print a list of first and last 5
elements where the values are square of numbers between 1 and 30."""

n=[i**2 for i in range(1,31)]
first_5=n[:5]
last_5=n[-5:]
print("First 5 elements:", first_5)
print("Last 5 elements:", last_5)
