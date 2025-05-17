def add_and_substract(num1, num2, num3):
    return subtract(num1, num2, num3)


def add(first, second):
    sum = first + second
    return sum


def subtract(first, second, third):
    subtracted = add(first, second) - third
    return subtracted


num_one = int(input())
num_two = int(input())
num_three = int(input())
print(add_and_substract(num_one, num_two, num_three))
