def smallest_num (numbers):
    # result = min(numbers)
    # return result
    min_num = float("Inf")
    for num in numbers:
        if min_num>num:
            min_num=num
    return min_num

num1 = int(input())
num2 = int(input())
num3 = int(input())
print(smallest_num([num1,num2,num3]))