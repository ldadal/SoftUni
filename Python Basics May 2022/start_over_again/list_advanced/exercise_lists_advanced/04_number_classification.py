numbers = [int(x) for x in input().split(", ")]
positive = [num for num in numbers if num >= 0]
print("Positive: ", end="")
print(*[num for num in numbers if num >= 0], sep=", ")
print("Negative: ", end="")
print(*[num for num in numbers if num < 0], sep=", ")
print("Even: ", end="")
print(*[num for num in numbers if num % 2 == 0], sep=", ")
print("Odd: ", end="")
print(*[num for num in numbers if num % 2 != 0], sep=", ")
