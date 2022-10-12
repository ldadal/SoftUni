# first = list(input())
# second = list(input())
# counter=0
# for i in first:
#     if first[counter]==second[counter]:
#         counter+=1
#         continue
#     else:
#         first[counter]=second[counter]
#         counter+=1
#         print("".join(first))
first_string = input()
second_string = input()
last_printed_string = first_string
for character_in_string in range(len(first_string)):
    left_part = second_string[:character_in_string + 1]
    right_part = first_string[character_in_string + 1:]
    current_string = left_part + right_part
    if last_printed_string == current_string:
        continue
    print(current_string)
    last_printed_string = current_string
