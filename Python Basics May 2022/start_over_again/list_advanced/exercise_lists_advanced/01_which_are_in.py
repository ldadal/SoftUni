first_string = input().split(", ")
second_string = input().split(", ")
result = []
result = list([x for x in first_string if any(x in w for w in second_string)])
# for i in range(len(second_string)):
#     result += (list(filter(lambda x: x in second_string[i], first_string)))
# #     for s_i in range(len(second_string)):
# #         if first_string[i] not in second_string[s_i]:
# #             result.pop(i)
# #             break
# result = list(set(result))
# answer = []
# for i in range(len(first_string)):
#     answer += list(filter(lambda x: x == first_string[i], result))
# # result.sort()
# print(answer)
print(result)
