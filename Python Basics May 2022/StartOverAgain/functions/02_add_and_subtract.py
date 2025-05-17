def add_and_substract(num1, num2, num3):
    def sum_numbers(first, second):
        sum = first + second
        return sum

    def subtract(first, second, third):
        subtracted = sum_numbers(first, second) - third
        return subtracted

    return subtract(num1, num2, num3)


num_one = int(input())
num_two = int(input())
num_three = int(input())
print(add_and_substract(num_one, num_two, num_three))
