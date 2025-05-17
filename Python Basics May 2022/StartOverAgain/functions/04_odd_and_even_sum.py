def sum_of_even_and_odd(number_as_string):
    odd = 0
    even = 0
    result = []
    number = int(number_as_string)
    for _ in range(len(number_as_string)):
        if (number % 10) % 2 == 0:
            even += number % 10
        else:
            odd += number % 10
        number = number // 10
    # print(f"Odd sum = {odd}, Even sum = {even}")
    result.append(odd)
    result.append(even)
    return result


number_str = input()
print(f"Odd sum = {sum_of_even_and_odd(number_str)[0]}, Even sum = {sum_of_even_and_odd(number_str)[1]}")

