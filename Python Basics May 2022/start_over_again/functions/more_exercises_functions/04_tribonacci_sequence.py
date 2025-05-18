def tribonacci(num):
    result = [1,1,2]
    for n in range(num-3):
        result.append(result[n]+result[n+1]+result[n+2])
    return result


number = int(input())
sequence = tribonacci(number)

for i in range(len(sequence)):
    if i == len(sequence) - 1:
        print(sequence[i], end="")
    else:
        print(sequence[i], end=" ")


# def tribonacci_sequence(n):
#     result = [1, 1, 2]
#     for i in range(3, n):
#         result.append(result[i - 1] + result[i - 2] + result[i - 3])
#     print(" ".join(map(str, result[:n])))
#
#
# number = int(input("Enter a positive integer: "))
# if number > 0:
#     tribonacci_sequence(number)
# else:
#     print("Please enter a positive integer.")
