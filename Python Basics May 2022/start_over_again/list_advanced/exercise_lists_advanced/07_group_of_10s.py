# numbers = [int(num) for num in input().split(", ")]
# result = []
# group_count = 0
# for i in range(0, 10, 1):
#     result.append([x for x in numbers if i * 10 < x <= i * 10 + 10])
# for i in range(9, 0, -1):
#     if len(result[i]) > 0:
#         for index in range(0, i+1, 1):
#             print(f"Group of {index*10+10}'s: [",end="")
#             print(*result[index], sep=", ",end="")
#             print("]")
#
#         break
#     else:
#         result.pop()
# #
# # print(*range(1, 101), sep=", ")


numbers = [int(num) for num in input().split(", ")]
max_group = (max(numbers) - 1) // 10 + 1
for i in range(1, max_group + 1):
    group = [x for x in numbers if (i - 1) * 10 < x <= i * 10]
    print(f"Group of {i*10}'s: {group}")
