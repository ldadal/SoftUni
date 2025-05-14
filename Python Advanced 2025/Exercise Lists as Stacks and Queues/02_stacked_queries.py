number_of_lines = int(input())
stack = []
while number_of_lines != 0:
    number_of_lines -= 1
    queries = input()
    if queries == "2":
        if len(stack) != 0:
            stack.pop()
        else:
            continue
    elif queries == "3":
        if len(stack) != 0:
            max_number = max(stack)
            print(max_number)
        else:
            continue
    elif queries == "4":
        if len(stack) != 0:
            min_number = min(stack)
            print(min_number)
        else:
            continue
    else:
        _, number_to_add = queries.split(" ")
        number_to_add = int(number_to_add)
        stack.append(number_to_add)
stack_for_print = []
while stack:
    stack_for_print.append(stack.pop())
print(", ".join(map(str, stack_for_print)))