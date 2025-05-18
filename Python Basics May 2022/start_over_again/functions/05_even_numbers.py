def even_only(num):
    return num % 2 == 0


# numbers_as_string = input().split()
# numbers = []
# for num in numbers_as_string:
#     numbers.append(int(num))
numbers = [int(x) for x in input().split()] # same as lines from 5 to 8
# for x in filter(even_only, numbers): even.append(x)
print(list(filter(even_only, numbers)))

# print(list(filter(lambda x: x % 2 == 0, numbers)))
