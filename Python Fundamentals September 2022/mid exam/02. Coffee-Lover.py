names_of_the_coffees = input().split()
number_of_commands = int(input())


def correct_index(index):
    if 0 <= index < len(names_of_the_coffees):
        return True


for command in range(number_of_commands):
    command_input = input().split()
    if "Include" in command_input:
        names_of_the_coffees.append(command_input[1])
    elif "Reverse" in command_input:
        names_of_the_coffees = names_of_the_coffees[::-1]
    else:
        command_type, index_one, index_two = [int(x) if x.isdigit() else x for x in command_input]
        if "Remove" in command_type:
            if 0 <= index_two < len(names_of_the_coffees):
                if "first" in index_one:
                    # names_of_the_coffees = names_of_the_coffees[first_or_last:]
                    for coffee_to_remove in range(index_two):
                        del names_of_the_coffees[0]
                elif "last" in index_one:
                    # names_of_the_coffees = names_of_the_coffees[:-first_or_last]
                    for coffee_to_remove in range(index_two):
                        del names_of_the_coffees[-1]
        else:
            if correct_index(index_one) and correct_index(index_two):
                names_of_the_coffees[index_one], names_of_the_coffees[index_two] = \
                    names_of_the_coffees[index_two], names_of_the_coffees[index_one]

print(f"Coffees:\n", *names_of_the_coffees)
