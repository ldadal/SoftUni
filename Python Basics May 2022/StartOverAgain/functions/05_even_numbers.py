def even_only(num):
    if num % 2 == 0:
        return True
    else:
        return False


numbers_as_string = input().split()
numbers = []
for num in numbers_as_string:
    numbers.append(int(num))
even = []
for x in filter(even_only, numbers): even.append(x)
print(even)