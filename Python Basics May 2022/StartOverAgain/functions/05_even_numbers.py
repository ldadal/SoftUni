def even_only(num):
    return num % 2 == 0

numbers_as_string = input().split()
numbers = []
for num in numbers_as_string:
    numbers.append(int(num))
even = []
for x in filter(even_only, numbers): even.append(x)
print(even)