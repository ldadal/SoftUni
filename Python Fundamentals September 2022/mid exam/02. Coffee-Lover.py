coffees_names = input().split()
commands_number = int(input())


for command in range(commands_number):
    command_input = input().split()
    if "Include" in command_input:
        coffees_names.append(command_input[1])
    elif "Reverse" in command_input:
        coffees_names = coffees_names[::-1]
    else:
        command_type, index_one, index_two = [int(x) if x.isdigit() else x for x in command_input]
        if "Remove" in command_type:
            if 0 <= index_two < len(coffees_names):
                if "first" in index_one:
                    for coffee_to_remove in range(index_two):
                        del coffees_names[0]
                elif "last" in index_one:
                    for coffee_to_remove in range(index_two):
                        del coffees_names[-1]
        else:
            if 0 <= index_one < len(coffees_names) and 0 <= index_two < len(coffees_names):
                coffees_names[index_one], coffees_names[index_two] = \
                    coffees_names[index_two], coffees_names[index_one]

print(f"Coffees:\n", *coffees_names)
