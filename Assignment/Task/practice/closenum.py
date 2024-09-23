


numbers = [3, 9, 50, 15, 99, 7,8, 98, 65]
numbers.sort()
closest_pair = min(zip(numbers, numbers[1:]), key=lambda x: x[1] - x[0])
print(list(closest_pair))