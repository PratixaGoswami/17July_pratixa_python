 
def is_perfect(number):
    return number == sum(i for i in range(1, number) if number % i == 0)

num = int(input("Enter a number: "))
if is_perfect(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
