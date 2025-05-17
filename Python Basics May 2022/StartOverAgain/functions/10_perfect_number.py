def perfect_number(number):
    sum = 0
    for num in range(1,number):
        if number % num == 0:
            sum += num
    if sum == number:
        return True
    else:
        return False


number = int(input())
if perfect_number(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")