number_two = int(input())
number_two = str(number_two)
first_digit_from_number_one = int(number_two[0])
second_digit_from_number_one = int(number_two[1])
third_digit_from_number_one = int(number_two[2])
fourth_digit_from_number_one = int(number_two[3])
number_two = int(input())
number_two = str(number_two)
first_digit_from_number_two = int(number_two[0])
second_digit_from_number_two = int(number_two[1])
third_digit_from_number_two = int(number_two[2])
fourth_digit_from_number_two = int(number_two[3])
for x in range (first_digit_from_number_one,first_digit_from_number_two+1):
    for y in range(second_digit_from_number_one,second_digit_from_number_two+1):
        for z in range(third_digit_from_number_one,third_digit_from_number_two+1):
            for j in range(fourth_digit_from_number_one,fourth_digit_from_number_two+1):
                if y%2!=0 and x%2!=0 and z%2!=0 and j%2!=0:
                    print(f"{x}{y}{z}{j} ",end="")