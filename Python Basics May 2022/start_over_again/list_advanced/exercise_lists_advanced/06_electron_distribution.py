number_of_electrons = int(input())
max_number_of_electrons = 0
shell_with_electrons = []
count_of_shells = 0
while number_of_electrons > 0:
    count_of_shells += 1
    max_number_of_electrons = 2 * count_of_shells ** 2
    shell_with_electrons.append(max_number_of_electrons if max_number_of_electrons<number_of_electrons else number_of_electrons)
    # if max_number_of_electrons < number_of_electrons:
    #     shell_with_electrons.append(max_number_of_electrons)
    # else:
    #     shell_with_electrons.append(number_of_electrons)
    number_of_electrons -= max_number_of_electrons
print(shell_with_electrons)
