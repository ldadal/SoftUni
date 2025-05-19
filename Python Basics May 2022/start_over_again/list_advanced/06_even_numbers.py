# nums_as_string = input().split(", ")
nums = [int(n) for n in input().split(", ")]
print([index for index in range(len(nums)) if nums[index]  % 2 == 0])
# for i in range(len(nums)):
#     if nums[i]%2==0:
#         print(i)